"""
VS Code Workspace-Setup für das Projekt "testautomatisierung"
=============================================================

Dieses Skript richtet eine neue VS Code Instanz vollständig ein:
  - Liest Python-Dependencies aus pyproject.toml
  - Installiert sie via uv (oder pip als Fallback)
  - Installiert empfohlene VS Code Extensions
  - Vergleicht lokale und remote VS Code Instanzen

Ausführung:
    python vs_code_setup.py                            # Setup
    python vs_code_setup.py --compare --remote <url>   # Vergleich lokal ↔ remote
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PYPROJECT = PROJECT_ROOT / "pyproject.toml"
EXTENSIONS_JSON = PROJECT_ROOT / ".vscode" / "extensions.json"

# Kein Default-Remote — beim Vergleich per --remote angeben.
DEFAULT_REMOTE_URL = ""


def load_jsonc(path: Path) -> dict:
    """Liest eine JSONC-Datei (JSON mit Kommentaren)."""
    text = path.read_text(encoding="utf-8")
    # Einzeilige Kommentare entfernen (// ...)
    text = re.sub(r"//.*?$", "", text, flags=re.MULTILINE)
    # Mehrzeilige Kommentare entfernen (/* ... */)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return json.loads(text)


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    print(f"  → {' '.join(cmd)}")
    # shell=True nötig unter Windows für .cmd/.bat (z.B. code.cmd)
    return subprocess.run(cmd, check=check, capture_output=True, text=True, shell=True)


def install_python_deps():
    """Liest dependencies aus pyproject.toml und installiert sie."""
    print("\n[1/2] Python-Dependencies installieren...")

    if not PYPROJECT.exists():
        print("  ⚠ pyproject.toml nicht gefunden – überspringe.")
        return

    # uv bevorzugen, pip als Fallback
    if shutil.which("uv"):
        result = run(["uv", "sync"], check=False)
        if result.returncode == 0:
            print("  ✓ Dependencies via uv installiert.")
        else:
            print(f"  ✗ uv sync fehlgeschlagen:\n{result.stderr}")
    else:
        # Prüfe ob pip verfügbar ist
        pip_check = run([sys.executable, "-m", "pip", "--version"], check=False)
        if pip_check.returncode == 0:
            result = run(
                [sys.executable, "-m", "pip", "install", "-e", "."],
                check=False,
            )
            if result.returncode == 0:
                print("  ✓ Dependencies via pip installiert.")
            else:
                print(f"  ✗ pip install fehlgeschlagen:\n{result.stderr}")
        else:
            print("  ⚠ Weder uv noch pip gefunden.")
            print("    Bitte installieren: https://docs.astral.sh/uv/getting-started/installation/")
            print("    Danach: uv sync")


def install_vscode_extensions():
    """Liest Extensions aus .vscode/extensions.json und installiert sie."""
    print("\n[2/2] VS Code Extensions installieren...")

    code_cmd = shutil.which("code")
    if not code_cmd:
        print("  ⚠ 'code' CLI nicht gefunden. Bitte VS Code zum PATH hinzufügen:")
        print("     VS Code → Strg+Shift+P → 'Shell Command: Install code in PATH'")
        return

    if not EXTENSIONS_JSON.exists():
        print("  ⚠ .vscode/extensions.json nicht gefunden – überspringe.")
        return

    data = load_jsonc(EXTENSIONS_JSON)
    extensions = data.get("recommendations", [])

    if not extensions:
        print("  Keine empfohlenen Extensions gefunden.")
        return

    for ext in extensions:
        result = run(["code", "--install-extension", ext], check=False)
        if result.returncode == 0:
            print(f"  ✓ {ext}")
        else:
            print(f"  ✗ {ext}: {result.stderr.strip()}")


# ============================================================================
# Vergleich zweier VS Code Instanzen
# ============================================================================

def get_local_extensions() -> set[str]:
    """Gibt die lokal installierten VS Code Extensions zurück."""
    code_cmd = shutil.which("code")
    if not code_cmd:
        print("  ⚠ 'code' CLI nicht gefunden.")
        return set()
    result = run(["code", "--list-extensions"], check=False)
    if result.returncode != 0:
        return set()
    return {ext.strip().lower() for ext in result.stdout.splitlines() if ext.strip()}


def get_local_settings() -> dict:
    """Liest die lokalen VS Code User-Settings."""
    # Windows-Standard-Pfad
    settings_path = Path.home() / "AppData" / "Roaming" / "Code" / "User" / "settings.json"
    if not settings_path.exists():
        # Linux/macOS Fallback
        for alt in [
            Path.home() / ".config" / "Code" / "User" / "settings.json",
            Path.home() / "Library" / "Application Support" / "Code" / "User" / "settings.json",
        ]:
            if alt.exists():
                settings_path = alt
                break
    if not settings_path.exists():
        print(f"  ⚠ Lokale settings.json nicht gefunden.")
        return {}
    return json.loads(settings_path.read_text(encoding="utf-8"))


def get_remote_extensions(remote_url: str) -> set[str]:
    """Holt die Extension-Liste von einer Remote VS Code Instanz (code-server API)."""
    # code-server: GET /api/applications
    # vscode-server: versuche verschiedene API-Endpunkte
    api_paths = [
        "/api/extensions",
        "/api/applications",
        "/extensionsGallery/extensions",
    ]
    for api_path in api_paths:
        url = remote_url.rstrip("/") + api_path
        try:
            req = urllib.request.Request(url, method="GET")
            req.add_header("Accept", "application/json")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if isinstance(data, list):
                    # Verschiedene Formate je nach Server
                    extensions = set()
                    for item in data:
                        if isinstance(item, str):
                            extensions.add(item.lower())
                        elif isinstance(item, dict):
                            ext_id = (
                                item.get("identifier", {}).get("id", "")
                                or item.get("id", "")
                                or item.get("name", "")
                            )
                            if ext_id:
                                extensions.add(ext_id.lower())
                    return extensions
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError):
            continue

    # Fallback: SSH-basiert (falls code CLI auf Remote verfügbar)
    print(f"  ⚠ API-Endpunkte nicht erreichbar. Versuche SSH-Fallback...")
    parsed = urllib.request.urlparse(remote_url)
    host = parsed.hostname
    result = run(
        ["ssh", "-o", "ConnectTimeout=5", host,
         "code", "--list-extensions"],
        check=False,
    )
    if result.returncode == 0:
        return {ext.strip().lower() for ext in result.stdout.splitlines() if ext.strip()}

    print(f"  ✗ Konnte Extensions von {remote_url} nicht abrufen.")
    return set()


def get_remote_settings(remote_url: str) -> dict:
    """Versucht die Settings von der Remote-Instanz zu lesen."""
    api_paths = [
        "/api/settings",
        "/api/user/settings",
    ]
    for api_path in api_paths:
        url = remote_url.rstrip("/") + api_path
        try:
            req = urllib.request.Request(url, method="GET")
            req.add_header("Accept", "application/json")
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError):
            continue
    return {}


def print_diff_table(title: str, only_local: set, only_remote: set, common: set):
    """Gibt eine Vergleichstabelle aus."""
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")
    print(f"  Gemeinsam:        {len(common)}")
    print(f"  Nur lokal:        {len(only_local)}")
    print(f"  Nur remote:       {len(only_remote)}")

    if only_local:
        print(f"\n  ▸ Nur LOKAL vorhanden:")
        for item in sorted(only_local):
            print(f"    + {item}")

    if only_remote:
        print(f"\n  ▸ Nur REMOTE vorhanden:")
        for item in sorted(only_remote):
            print(f"    - {item}")

    if not only_local and not only_remote:
        print("\n  ✓ Keine Unterschiede gefunden.")


def print_settings_diff(local_settings: dict, remote_settings: dict):
    """Vergleicht zwei Settings-Dictionaries und zeigt Differenzen."""
    print(f"\n{'─' * 60}")
    print(f"  Settings-Vergleich")
    print(f"{'─' * 60}")

    if not remote_settings:
        print("  ⚠ Remote-Settings konnten nicht abgerufen werden – überspringe.")
        return

    all_keys = sorted(set(local_settings.keys()) | set(remote_settings.keys()))
    diffs = []
    for key in all_keys:
        local_val = local_settings.get(key, "⟨nicht gesetzt⟩")
        remote_val = remote_settings.get(key, "⟨nicht gesetzt⟩")
        if local_val != remote_val:
            diffs.append((key, local_val, remote_val))

    if not diffs:
        print("  ✓ Settings sind identisch.")
        return

    print(f"  {len(diffs)} Unterschied(e) gefunden:\n")
    for key, local_val, remote_val in diffs:
        print(f"  [{key}]")
        print(f"    Lokal:  {json.dumps(local_val, ensure_ascii=False)}")
        print(f"    Remote: {json.dumps(remote_val, ensure_ascii=False)}")
        print()


def compare_instances(remote_url: str):
    """Vergleicht lokale VS Code Instanz mit einer Remote-Instanz."""
    if not remote_url:
        print("  ⚠ Keine Remote-URL angegeben. Nutze: --compare --remote <url>")
        return

    print("=" * 60)
    print(f"VS Code Instanz-Vergleich")
    print(f"  Lokal:  diese Maschine")
    print(f"  Remote: {remote_url}")
    print("=" * 60)

    # Extensions vergleichen
    print("\nExtensions abrufen...")
    local_ext = get_local_extensions()
    remote_ext = get_remote_extensions(remote_url)

    if local_ext or remote_ext:
        only_local = local_ext - remote_ext
        only_remote = remote_ext - local_ext
        common = local_ext & remote_ext
        print_diff_table("Extensions-Vergleich", only_local, only_remote, common)

    # Settings vergleichen
    print("\nSettings abrufen...")
    local_settings = get_local_settings()
    remote_settings = get_remote_settings(remote_url)
    print_settings_diff(local_settings, remote_settings)

    print(f"\n{'=' * 60}")
    print("Vergleich abgeschlossen.")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="VS Code Workspace-Setup & Vergleich")
    parser.add_argument(
        "--compare", action="store_true",
        help="Vergleiche lokale VS Code Instanz mit einer Remote-Instanz",
    )
    parser.add_argument(
        "--remote", type=str, default=DEFAULT_REMOTE_URL,
        help="URL der Remote-Instanz (z.B. http://host:port)",
    )
    args = parser.parse_args()

    if args.compare:
        compare_instances(args.remote)
    else:
        print("=" * 60)
        print("VS Code Workspace-Setup für 'testautomatisierung'")
        print("=" * 60)

        install_python_deps()
        install_vscode_extensions()

        print("\n" + "=" * 60)
        print("Setup abgeschlossen!")
        print("Öffne den Projektordner in VS Code:")
        print(f"  code {PROJECT_ROOT}")
        print("=" * 60)


if __name__ == "__main__":
    main()
