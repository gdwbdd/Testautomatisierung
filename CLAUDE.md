# CLAUDE.md

Diese Datei wird von Claude Code automatisch bei Sessionstart geladen. Sie enthält keinen
eigenen Regeltext, nur Importe und Leseordnung.

## Geteilte Regeln (Single Source of Truth, Submodul `docs/shared_rules_knowledge/`)
@docs/shared_rules_knowledge/rules/codex.md
@docs/shared_rules_knowledge/rules/lernprozesse.md

Ist das Submodul leer: `git submodule update --init`. Repo: https://github.com/gdwbdd/shared_rules_knowledge

## Zuerst lesen (in dieser Reihenfolge)
1. `docs/workbasis/codex.md` — projektspezifische Regeln (Python/pytest, Plan-Pflege)
2. `docs/workbasis/open_points.md` — offene Punkte/Wiedervorlage. Session-Start: ZUERST lesen. Session-Ende: ZULETZT aktualisieren.
3. `docs/workbasis/chat_log.md` — Chatverlauf/Kontext (selbstständig pflegen)
4. `docs/workbasis/knowledge/INDEX.md` — Projektwissen; `knowledge/terminologie.md` — Projektglossar
5. `docs/shared_rules_knowledge/knowledge/terminologie.md` — Domänenglossar + Invarianten (geteilt)
6. `docs/workbasis/adr/README.md` — Projektentscheidungen; Prozess in `docs/shared_rules_knowledge/adr/README.md`
7. `PROJECT_PLAN.md` — lebendes Dokument, Quelle und Arbeitsziel zugleich (Abschnitt 0: Rahmengedanken)

## Geltungsbereich
Dieselben Regeln gelten für GitHub Copilot (`.github/copilot-instructions.md`) — ein gemeinsames
Regelwerk, keine Doppelpflege. Repo-Dateien (Submodul + `docs/workbasis/`) sind autoritativ; der
Memory-Store des Assistenten ist nur Zeiger. Der frühere Copilot-Memory-Seed `memory/repo/` ist am
2026-09-11 nach `docs/workbasis/` überführt worden.

## Handoff-Pflicht
Jede "speichern & später vorlegen"-Zusage sofort in `docs/workbasis/open_points.md` ablegen. Neue
mögliche Regel erkannt → erst prüfen, ob im geteilten oder im Projekt-Codex vorhanden, sonst beim
User nachfragen, ob sie gilt.
