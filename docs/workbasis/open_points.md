# Offene Punkte / Wiedervorlage (testautomatisierung)

> Session-Start: ZUERST lesen. Session-Ende: ZULETZT aktualisieren. Neueste Abschnitte oben.
> Handoff-Pflicht: jede "speichern & später vorlegen"-Zusage SOFORT hier ablegen.
> Entscheidungen verweisen auf das ADR; hier bleiben nur Status und Wiedervorlage.
> Übernommen aus dem früheren Copilot-Memory-Seed `memory/repo/open_points.md` (dort: keine Einträge).

## 2026-09-11 — Git-Repo angelegt, geteiltes Regelwerk eingebunden (User: "A auf github")
- [x] `git init` (Branch `main`), `.gitignore`, Submodul `docs/shared_rules_knowledge/`,
      `CLAUDE.md` mit `@`-Importen, `copilot-instructions.md` nur Leseordnung, `codex.md`
      Projektteil, `docs/workbasis/` aus `memory/repo/` überführt (Seed gelöscht), `adr/README.md`,
      `knowledge/terminologie.md`, `README.md` mit Klonabschnitt. Begründung: geteiltes ADR 001.
- [ ] **GitHub-Repo `gdwbdd/testautomatisierung` existiert noch nicht** (verifiziert per
      `git ls-remote`: "Repository not found"). Der Assistent kann es nicht anlegen (kein `gh`,
      kein Token). User legt es leer an (ohne README/.gitignore), danach `git push -u origin main`.
- [ ] Prüfen (neue Session, `/context`): werden die zwei `@`-Importe aus dem Submodul geladen?
- [ ] `PROJECT_PLAN.md` Abschnitte ab 1 fortschreiben; `Anforderungen.md`/`Vorarbeiten.md` sind
      die Quellen.

## Offen (aus dem Seed)
- (noch keine)

## Erledigt (aus dem Seed)
- (noch keine)
