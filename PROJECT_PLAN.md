# Projektplan: testautomatisierung

> **Lebendes Dokument** – Status wird während der Umsetzung fortlaufend aktualisiert.
> Legende: ⬜ offen · 🔄 in Arbeit · ✅ erledigt · ⏸ pausiert · ❌ verworfen

---

## 0. Rahmengedanken (extrahierte Rahmenbedingungen)

> Implizite Rahmenbedingungen aus der Aufgabenstellung/Diskussion, die den Plan tragen,
> aber nicht als konkreter Plan-Inhalt auftauchen. Sie bilden den Denkrahmen, in dem alle
> folgenden Punkte zu lesen sind.

- **Prozess-, kein Testfall-Plan**: Es geht nicht um eine Liste von Testfällen, sondern um den **Lifecycle einer neuen Version** (Eingang → Deployment → Durchführung → Umfang → Feedback).
- **Zeitrahmen-Restriktion**: Ein vollständiger Test-Plan für **jede** Komponente ist im aktuellen Zeitrahmen **nicht machbar** → bewusste Reduktion auf einen **Beispiel-Plan für 1 (oder mehr) Komponente(n)** (vereinbart, „as discussed / we agreed").
- **Zwei Ebenen gleichzeitig**: Fach-Ebene (**Komponente testen**) und Meta-Ebene (**den Plan selbst validieren** — ist er nützlich/handhabbar?). Der Pilotlauf bedient beide.
- **Erfolgskriterium = Erfahrungsrückfluss vor Abschluss**: Maßstab ist nicht nur ein bestandener Test, sondern dass **Erfahrungen/Erkenntnisse noch VOR Abschluss der Arbeiten in die Entwicklung einfließen** (laufender Rückfluss, nicht erst am Ende).
- **Nachvollziehbarkeit/Reproduzierbarkeit als Prinzip**: Ergebnisse müssen belastbar und rekonstruierbar sein → daher Doku als durchgehender Strang (siehe Abschnitt 3).
- **Schablonen-Charakter**: Der Beispiel-Plan ist zugleich **Vorlage** — konkret genug für den einen Pilotlauf, aber übertragbar auf weitere Komponenten.
- **Plan ist zugleich Quelle und Arbeitsziel**: Quelle, weil er das gemeinsame Verständnis und die eingearbeiteten Erkenntnisse bereitstellt, aus denen weitergearbeitet wird; Arbeitsziel, weil er selbst beständig befüllt, erweitert und abgearbeitet wird (lebendes Dokument).

---

## 1. Ist-Zustand
- Projekt initialisiert (Meta-Ebene/Regeln aus mec_demo übernommen, Code nicht).
- Plan-Phase: Struktur eines **Beispiel-Test-Plans** wird gemeinsam erarbeitet (lebender Entwurf, wird mit jeder Erkenntnis erweitert).

## 2. Ziel
- **Beispiel-Test-Plan** für 1 (oder mehr) repräsentative Komponente(n), der den kompletten Lifecycle einer neuen Version beschreibt: Eingang → Deployment → Test-Durchführung → Test-Umfang → Feedback-Rückkanal.
- Plan mind. **einmal real ausführen** → Engineering-Feedback zur Nützlichkeit einholen.
- Doppelzweck des Pilotlaufs: (a) Komponente testen, (b) den **Plan selbst** auf Nützlichkeit/Handhabbarkeit prüfen.
- Plan als übertragbare **Vorlage/Schablone** bauen (konkret für den Pilotlauf, wiederverwendbar für weitere Komponenten).

## 3. Struktur des Beispiel-Test-Plans (lebender Entwurf)

### Querschnitt: Dokumentation („Doku-als-Querschnitt")
- Doku ist **kein Endschritt**, sondern ein **durchgehender Strang**: jeder Schritt (1–4) erzeugt Doku-Artefakte, Schritt 5 bündelt sie.
- Grundsatz: **Test ohne Doku ist nicht belastbar.**

### 1. Wie die Info über eine neue Version „zu dir kommt"
- **Bereichsabhängigkeit** als Klassifikations-/Routing-Merkmal: **Fachbereich** (motion control, robot integration, ndx, …). Die Bereichsliste ist eine **noch zu entwickelnde Liste** (nicht abschließend).
- Bewusst **eindimensional**: kein zusätzlicher Pfad „Änderungsart". Bugs entstehen **funktionsbezogen** innerhalb der Fachbereiche.
- Angaben werden **Teil der Doku zur Nachvollziehbarkeit** (Wer/Was löst aus, Kanal, Versionsnummer, Changelog, Artefakt-Ort, Fachbereich).

### 2. Wie sie deployed wird
- **Ziele**: Cloud-Instanz, VM, IPC (Industrie-PC).
- **Versionsstände** der drei Ziele werden in den **Testbedingungen** definiert (nicht pauschal gleich/verschieden).
- **Reproduzierbarkeits-Snapshot** als Doku: genutzte Plattform, SW-Versionen, **SW-Abbild des Systems** (Diagnose-Package, exportierte Konfiguration, Programme in VS Code, installierte Apps).

### 3. Wie getestet wird
- **Soweit wie möglich automatisieren.**
- **Manuelles Verproben** ist zum Verstehen und Wissenserwerb notwendig.
- Reihenfolge manuell/automatisiert **kontextabhängig** — keine feste Vorgabe.
- Kein starres „automatisierbar ab X"-Kriterium — **kontextabhängig**.

### 4. Was getestet wird
- **Analyse der User Story** als Quelle für: Zielfunktionen / zu testende Funktionen, **Ergebnisse die nicht auftreten dürfen**, Implementierungsrahmen/Abhängigkeiten. (Pattern/Beispiel: SSOT in [userstory_pattern.md](userstory_pattern.md))
- User Stories liegen **teils/teils** strukturiert vor → Plan wirkt als **Schablone**, die **Lücken/Differenzen/fehlende Infos sichtbar macht** und als Feedback zurückspielt.
- Testarten: **Wiederholungen, Einzel- und Dauertests, Bruchfestigkeit**.
- Gegensatzpaar: **„Happy path" ↔ „try to break"**.
- **Bruchfestigkeit** = beides: Last/Stress bis Fehlerfall **und** Grenzwert-/Robustheitstests (ungültige Eingaben, Randbedingungen).

### 5. Wie Feedback zurückgespielt wird
- Umfasst die **Dokumentation des gesamten Prozesses** (Bündelung des Querschnitt-Strangs).
- Zu bedienen: **Feedbackkanal, Bug-Reporting, Review-/Retry-Loops**.
- **Erweiterter Retry-Gedanke**: Fehler**struktur** erkennen → in **anderen Testszenarien nachziehen** → aus erworbenem Wissen auf **vergleichbare Strukturen** achten und testen („über den Tellerrand schauen"): prüfen, ob **periphere oder direkte Komponenten Störeinflüsse** verursachen.
- **Retry-Loop-Umfang** hängt von der **Komplexität des Fixes** ab (kompletter Durchlauf vs. gezielter Nachtest).
- **Bug-Reporting-Tool/Kanal**: später **separat** befüllen.

## 4. Offene Punkte (mit Kollegen zu klären)
- Welche **konkrete Komponente** (repräsentativ, nicht trivial/nicht komplexeste); realer Kandidat für den Pilotlauf.
- **Rollen**: „you" (Empfänger/Testende) vs. „main contributor/team".
- Werden **Version/Artefakte** bereitgestellt? Wo liegt der **Funktionsrahmen**? Umgang mit **Zusatzinformationen**?
- Sammlung in [Anforderungen.md](Anforderungen.md).

## 5. Arbeitspakete
- ⬜ Basis-Fragen (Komponente/Rollen) mit Kollegen klären — Abklärung erfolgt im Rahmen von [Anforderungen.md](Anforderungen.md)
- ⬜ Bug-Reporting-Tool/Kanal festlegen
- ⬜ Testbedingungen (u. a. Versionsstände der Ziele) definieren
- ⬜ Pilotlauf durchführen und Engineering-Feedback einholen
