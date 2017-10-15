## Spielidee

Für mein Spiel habe ich als Vorlage das Spiel bzw. das Spielprinzip “Achtung, die Kurve!”, auch bekannt als “Curve Fever”, gewählt. Bei diesem Arcade-Spiel wird die eigene (sich immer verlängernde) “Kurve” über die Spielfläche gesteuert. Das Spiel wird mit mehreren Spielern gespielt (am selben Computer oder über ein Netzwerk), das Ziel besteht dabei darin, nicht auf eine andere oder die eigene Kurve zu treffen. Daraus resultiert auch das hauptsächliche Mittel des Spiels, andere Spieler verlieren zu lassen: Wenn man einem Gegenspieler den Weg abschneidet, so lässt man ihn unweigerlich in die eigene Kurve fahren. Das fertige Spiel soll zusätzlich Gegenstände auf dem Spielfeld generieren, die den Verlauf des Spiels beeinflussen, z.B. die Geschwindigkeit verändern. Des weiteren werde ich noch den Mehrspielermodus über einen Server hinzufügen.
<br>
<br>
Für die Programmierung werde ich die Bibliothek PyGame verwenden, die sehr viele Freiräume bei dem Zeichnen der Oberfläche bietet und eine klare Trennung zwischen Spiellogik und grafischer Darstellung ermöglicht.
<br>
<br>
Außerdem werde ich für die Entwicklung nicht Jython benutzen, sondern einen selbstständigen Editor (Visual Studio Code) und den Code mittels Python3 (Referenzimplementierung CPython) auf einer Linux-Distribution ausführen. Am Ende wird auch eine selbstständige ausführbare Datei verfügbar sein, für die kein Python auf dem Rechner von Nöten sein wird.
<br>
<br>
Ich habe vor, alle Komponenten des Spiels als Klassen darzustellen, die eigene Funktionen für die Berechnung ihrer Geometrie besitzen. Aus diesen berechneten Daten soll am Ende eine einzige Funktion alle Elemente zeichnen.
<br>
<br>
Als Schwierigkeit sehe ich vor allem die Kollisionsberechnung der Kurven an, hier werde ich eine möglichst einfache und zugleich effizient Methode suchen, die Kurven miteinander abzugleichen.
<br>
<br>
Das Spiel wird auf [https://github.com/flyingP0tat0/curve](https://github.com/flyingP0tat0/curve) entwickelt.

> Jan Baudisch, 11/info1
