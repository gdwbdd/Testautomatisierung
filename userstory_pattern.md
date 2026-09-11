# User Story – Pattern (SSOT)

> **Single Source of Truth** für User Stories in diesem Projekt.
> Alle anderen Dateien (PROJECT_PLAN.md, Anforderungen.md, …) **referenzieren nur** hierauf —
> Inhalt wird ausschließlich hier gepflegt, nicht kopiert.

---

## Zweck
- Konkretes Beispiel/Muster einer User Story, um die **Analysefähigkeit** zu erhöhen:
  Zielfunktionen / zu testende Funktionen, **Ergebnisse die nicht auftreten dürfen**,
  Implementierungsrahmen/Abhängigkeiten aus einer User Story herausarbeiten.

## Ausgangspunkt
- Product Owner formulieren in User Storys die Wünsche und Anforderungen der Anwender für
  Software oder andere Leistungen, die in einem Funktion/Projekt realisiert werden sollen.

## Merkmale einer User Story
- **Nutzerzentriert**: beschreibt einen Wunsch/Bedarf aus Sicht des Anwenders, nicht als technische Spezifikation. Formulierung siehe Pattern.
- **Kurz & einfach**: ein bis wenige Sätze, in natürlicher Sprache, ohne Fachjargon.
- **Wert-orientiert**: benennt den **Nutzen/Grund** hinter dem Wunsch (das „Warum").
- **Verhandelbar**: kein fixer Vertrag, sondern Ausgangspunkt für ein Gespräch (Details werden gemeinsam geschärft).
- **Testbar**: mit **Akzeptanzkriterien**, an denen prüfbar ist, wann sie erfüllt ist.
- **Eigenständig & klein**: möglichst unabhängig und so geschnitten, dass sie in einem Zyklus umsetzbar ist.
- (Orientierung: **INVEST** – Independent, Negotiable, Valuable, Estimable, Small, Testable.)

## Wie werden User Storys richtig formuliert?
- **Standard-Satzschablone**:
  > **Als** \<Rolle/Anwender\> **möchte ich** \<Ziel/Funktion\>, **um** \<Nutzen/Grund\>.
- Die drei Bestandteile:
  - **Rolle** – wer hat den Bedarf (Anwendertyp)?
  - **Ziel** – was will diese Rolle erreichen (Funktion)?
  - **Nutzen** – warum, welcher Mehrwert entsteht?
- Ergänzt um **Akzeptanzkriterien** (z. B. „Gegeben … / Wenn … / Dann …"), die den Erfüllungsrahmen und
  prüfbare Bedingungen festlegen — inkl. **Ergebnisse, die nicht auftreten dürfen**.

## Pattern (Struktur einer User Story)
- **Titel**: kurze Bezeichnung
- **Story**: „Als \<Rolle\> möchte ich \<Ziel\>, um \<Nutzen\>." : "Als Nutzer möchte ich, dass Punkt1 erfüllt wird. Als Nutzer..." --> Klare Beschreibung der gewünschten Funktion. Genauso, wie definiert sein sollte, was bei der Ausführung der Funktionalität nicht auftreten darf.
- **Akzeptanzkriterien**: prüfbare Bedingungen (positiv + Ausschluss) - Genauso, wie definiert sein sollte, was bei der Ausführung der Funktionalität nicht auftreten darf.
- **Rahmen/Abhängigkeiten**: Implementierungsrahmen, abhängige Komponenten
  - Es müssen **Abhängigkeiten/Schnittstellen zu anderen Modulen/Funktionen** benannt werden.

## Beispiel
- (Beispiel-User-Story hier einfügen)
