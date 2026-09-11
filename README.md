# testautomatisierung

Prozess-Plan für die Test-Automatisierung einer neuen Version: Lifecycle Eingang → Deployment →
Durchführung → Umfang → Feedback, als Beispiel-Plan für eine Komponente und Schablone für weitere.
Kein Testfall-Katalog. Details und Rahmengedanken: [PROJECT_PLAN.md](PROJECT_PLAN.md),
Quellen: `Anforderungen.md`, `Vorarbeiten.md`, `userstory_pattern.md`.

## Klonen (Submodul erforderlich)

Das Regelwerk und Domänenwissen für KI-Assistenten liegt als Git-Submodul unter
`docs/shared_rules_knowledge/` (Quelle: <https://github.com/gdwbdd/shared_rules_knowledge>).
Ohne das Submodul ist der Ordner leer und `CLAUDE.md`/`.github/copilot-instructions.md`
laufen ins Leere.

```powershell
# Neu klonen, Submodul direkt mit
git clone --recurse-submodules https://github.com/gdwbdd/Testautomatisierung.git

# Bereits geklont, Ordner docs/shared_rules_knowledge ist leer
git submodule update --init

# Geteilten Stand nachziehen (nur auf Absprache, erzeugt einen Commit)
git submodule update --remote docs/shared_rules_knowledge
```

## Arbeitsbasis

`docs/workbasis/` (Codex, offene Punkte, Chatverlauf, Wissen, ADRs) ist git-versioniert und
autoritativ; Leseordnung in `CLAUDE.md`.

## Entwicklung

- Python / pytest; Venv `.\.venv\Scripts\Activate.ps1`
- VS-Code-Einrichtung: `python vs_code_setup.py` (Dependencies aus `pyproject.toml` per `uv`,
  empfohlene Extensions)
