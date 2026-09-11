# Codex — projektspezifische Regeln (testautomatisierung)

> Die generischen Regeln der Zusammenarbeit stehen in `docs/shared_rules_knowledge/rules/codex.md`
> (Single Source of Truth, Submodul) und werden hier NICHT wiederholt. Bis 2026-09-11 lagen sie als
> Kopie (Stand Juli 2026) in `.github/copilot-instructions.md`; die Kopie hatte alle seit August
> ergänzten Regeln nicht. Diese Datei enthält nur, was für dieses Projekt gilt. Abweichungen von
> den geteilten Regeln wären ausdrücklich als **Abweichung** markiert.

## Projekt-Kontext
- Gegenstand: Prozess-Plan für die Test-Automatisierung einer neuen Version (Lifecycle Eingang →
  Deployment → Durchführung → Umfang → Feedback), kein Testfall-Katalog. Beispiel-Plan für eine
  Komponente als Schablone; Erfolgskriterium ist der Erfahrungsrückfluss VOR Abschluss.
  *Quelle:* `PROJECT_PLAN.md` Abschnitt 0 (Rahmengedanken), `Anforderungen.md`, `Vorarbeiten.md`.
- Technik (Stand Initialisierung): Python / pytest; Dependencies über `pyproject.toml` und `uv`
  (`vs_code_setup.py` richtet die VS-Code-Instanz ein). Noch kein Anwendungscode.
- Von mec_demo wurde bewusst nur die Meta-Ebene (Regeln, Einstellungen) übernommen, kein Code.

## Architektur-Regeln
- `PROJECT_PLAN.md` ist lebendes Dokument, **Quelle und Arbeitsziel zugleich**: alles zur
  Weiterentwicklung dort dokumentieren, Status-Legende ⬜ 🔄 ✅ ⏸ ❌ verwenden.
- `knowledge/architektur.md` bei jeder strukturellen Änderung (neue Datei, verschobene Funktion,
  geänderte Import-Kette, gelöschte/umbenannte Datei) aktualisieren.
- User-Stories nach `userstory_pattern.md`.

## Dev-Umgebung, Tests
- Venv: `.\.venv\Scripts\Activate.ps1`; Test-Suite: `pytest` in der `.venv` ausführen.
- Nach Code-Änderungen: Fehlerfreiheit prüfen und pytest laufen lassen (geteilte Regel);
  Debug-Konfigurationen für pytest liegen in `.vscode/launch.json`.
- Kein Deploy-Skript vorhanden.

## Abweichungen von den geteilten Regeln
- *(keine)*
