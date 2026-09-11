# Themen-Wissen — Index (testautomatisierung)

> Nur Projektfakten. Generisches (Nova, Isaac, Claude Code) steht in
> `docs/shared_rules_knowledge/knowledge/INDEX.md` und wird hier nicht wiederholt.
> Jede Aussage: verifiziert (wie/wann) oder Annahme. Übernommen aus `memory/repo/knowledge/INDEX.md`.

## Verifizierte Fakten (Umgebung)
- Git: lokal `main`, Remote `https://github.com/gdwbdd/testautomatisierung.git` (2026-09-11 gesetzt,
  Repo auf GitHub noch anzulegen).
- Python / pytest; Venv `.\.venv\Scripts\Activate.ps1` (noch nicht angelegt, Stand 2026-09-11);
  `vs_code_setup.py` installiert Dependencies aus `pyproject.toml` per `uv` (Datei `pyproject.toml`
  existiert noch nicht).
- VS Code: empfohlene Extensions in `.vscode/extensions.json` (python, debugpy, pylance);
  pytest-Debug-Konfigurationen in `.vscode/launch.json`.

## Architektur-Stichworte
- siehe [architektur.md](architektur.md) (Stand Initialisierung, noch zu definieren)

## Themen-Dateien
- [architektur.md](architektur.md) — Zweck, Schichten, Datenfluss (Pflicht-Update bei Strukturänderung)
- [terminologie.md](terminologie.md) — Projektglossar (angelegt 2026-09-11)
- [../adr/README.md](../adr/README.md) — Projektentscheidungen (noch leer)
- geteilt: [../../shared_rules_knowledge/knowledge/INDEX.md](../../shared_rules_knowledge/knowledge/INDEX.md)
