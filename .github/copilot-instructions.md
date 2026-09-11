# Copilot Instructions – testautomatisierung

Dieselben Regeln wie für Claude Code (`CLAUDE.md`) — kein eigener Regeltext hier, um Drift zu
vermeiden. Die bis 2026-09-11 hier inline kopierten Regeln (Stand Juli 2026) stehen jetzt aktuell
im geteilten Codex; der frühere Repo-Memory-Seed `memory/repo/` ist nach `docs/workbasis/` überführt.

## Zuerst lesen (in dieser Reihenfolge)
1. `docs/shared_rules_knowledge/rules/codex.md` — geteilte Regeln der Zusammenarbeit (Single Source of Truth, Submodul)
2. `docs/shared_rules_knowledge/rules/lernprozesse.md` — gelernte Lektionen
3. `docs/workbasis/codex.md` — projektspezifische Regeln (Python/pytest, Plan-Pflege)
4. `docs/workbasis/open_points.md` — offene Punkte. Session-Start: ZUERST lesen. Session-Ende: ZULETZT aktualisieren.
5. `docs/workbasis/chat_log.md` — Chatverlauf/Kontext
6. `docs/workbasis/knowledge/INDEX.md`, `knowledge/terminologie.md`, `knowledge/architektur.md` — Projektwissen
7. `docs/shared_rules_knowledge/knowledge/terminologie.md` — Domänenglossar + Invarianten
8. `docs/workbasis/adr/README.md` — Projektentscheidungen
9. `PROJECT_PLAN.md` — lebendes Dokument (Rahmengedanken, Ist-Zustand, Plan)

Ist `docs/shared_rules_knowledge/` leer: `git submodule update --init`.

## Handoff-Pflicht
Jede "speichern & später vorlegen"-Zusage sofort in `docs/workbasis/open_points.md` ablegen. Neue
mögliche Regel erkannt → erst prüfen, ob vorhanden, sonst beim User nachfragen, ob sie gilt.
