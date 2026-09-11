# Anforderungen

> **Zweck**: Strukturierte Schablone, die die **Zuarbeit anderer Abteilungen** ermöglicht.
> Zunächst **eine gemeinsame Schablone** (um Differenzen zwischen den Arbeitsstrukturen zu erkennen).
> Vorgehen: erstmal **reine Sammlung** der Fragen — Antworten werden danach eingepflegt.
> Jede Frage wird mit den Kollegen erörtert; das Ergebnis wird Teil dieses Arbeitsrahmens.
> Grundhaltung: **vorhandene/gelebte Strukturen begleiten und erweitern**, nicht neu erfinden.

---

## A. Anzusprechende Personen (Vorgespräche)

> Persönliche Vorgespräche zur **Evaluierung und Einordnung** je Fachbereich.
> Die Fachbereichsliste ist eine **noch zu entwickelnde Liste** (nicht abschließend).

| Fachbereich | Person | Rolle | Kontakt/Kanal | Status Vorgespräch | Notiz |
|---|---|---|---|---|---|
| motion control |  |  |  | ⬜ offen |  |
| robot integration |  |  |  | ⬜ offen |  |
| ndx |  |  |  | ⬜ offen |  |
| … |  |  |  | ⬜ offen |  |

---

## B. Komponentenauswahl

- Ich würde **eine** repräsentative Komponente wählen (nicht die trivialste, nicht die komplexeste) — Repräsentativität entscheidet, ob das Engineering-Feedback aussagekräftig ist.
- Welche **Kandidaten** kommen in Frage?
- Nach welchen **Auswahlkriterien** entscheiden wir (Repräsentativität, anstehende neue Version, Zugänglichkeit der Artefakte)?
- Gibt es einen realen Kandidaten mit **demnächst anstehender Version** für den Pilotlauf?

---

## C. Inhaltliche Fragen je Lifecycle-Punkt (an vorhandene Strukturen anknüpfen)

> Leitfrage vor jedem Punkt: **Welche gelebte Struktur existiert hier schon** — und wie begleiten/erweitern wir sie, statt etwas Neues danebenzustellen?

### 1. Versions-Eingang (Wie kommt die Info über eine neue Version?)
> **Essenzielle Frage an ALLE Gesprächspartner.**
- Wie werdet ihr heute über eine neue Version informiert (Push/Pull, Kanal)?
- Welche **Metadaten** liegen bei (Versionsnummer, Changelog, Fachbereich, Artefakt-Ort)?
- Werden **Version/Artefakte** zur Verfügung gestellt? Wo/wie?
- Besteht ein **main**, der **automatisiert informieren** kann?
- Wie finden **Zweige, Sonderlösungen, Kundenlösungen** den Weg zur Prüfung?

### 2. Deployment (Cloud-Instanz, VM, IPC)
- Welche gelebte Deployment-Struktur gibt es je Ziel (Cloud, VM, IPC)?
- Wie wird der **Reproduzierbarkeits-Snapshot** heute erfasst (Diagnose-Package, exportierte Konfiguration, VS-Code-Programme, installierte Apps)?
- Wie sind **Versionsstände** der Ziele definiert (Testbedingungen)?

### 3. Test-Durchführung
- Welche Test-/Verproben-Praxis existiert bereits (manuell, automatisiert, Tooling)?
- Was ist heute schon automatisiert, was bewusst manuell?

### 4. Test-Umfang
- Wo finde ich den **Funktionsrahmen** (Quelle für Zielfunktionen/zu testende Funktionen)?
- Wo sind **Ergebnisse dokumentiert, die nicht auftreten dürfen**?
- Liegen **User Stories** vor — strukturiert mit Akzeptanzkriterien, oder lückenhaft?
- Was ist mit **Zusatzinformationen** (Implementierungsrahmen, Abhängigkeiten, periphere Komponenten)?

### 5. Feedback-Rückkanal
- Welcher **Feedbackkanal / Bug-Reporting** ist gelebte Praxis (Tool/Kanal)?
- Wie laufen **Review-/Retry-Loops** heute ab?
- Wie kommt das Ergebnis zurück zum **main contributor/team**?
- Welche **Informationen benötigt die Entwicklung** von uns, damit das Feedback/der Bug-Report verwertbar ist (z. B. Reproduktionsschritte, SW-Abbild, Umgebungsdaten)?

---

## D. Erörterung & Ergebnis (wird Teil des Arbeitsrahmens)

> Jede Frage aus A–C wird mit den Kollegen erörtert; das Ergebnis wird hier festgehalten
> und fließt in den Plan zurück.

- (noch keine Ergebnisse — wird nach den Vorgesprächen befüllt)

---

## E. Beispiel einer User Story

> Gepflegt als **SSOT** in [userstory_pattern.md](userstory_pattern.md) — hier nur Referenz, kein kopierter Inhalt.
