# Dokumentation

## main

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 11 | import von verwendeten Modulen |
| 13 - 20 | Enum-Klasse für den Status des Spiels |
| 23 | Laden der Konfiguration |
| 26 | main-Funktion (Ausführung wenn Python bereit) |
| 27 - 36 | Erstellung und Konfiguration der PyGame-Objekte |
| 45 - 48 | Menü-Musik spielen |
| 51 | unendliche Schleife, die das Spielgeschehen steuert |
| 53 | Abfrage eingegangener Events |
| 55 - 59 | Abbruch, wenn Schließen |
| 61 - 67 | Startmenü, Erstellung, Zeichnung und Verarbeitung |
| 71 - 74 | Menü-Musik spielen |
| 76 - 89 | Erstellung Kurven für Konfiguration |
| 91 - 96 | Setup-Menü, Erstellung mit Konfigurations-Kurven, Zeichnung und Verarbeitung |
| 98 - 110 | Spiel: Spiel-Musik, Spiel-"Brett" Erstellung, Zeichnung und Verarbeitung |
| 112- 121 | Abschluss-Menü mit Kurven des Spiels, Erstellung, Zeichnung und Verarbeitung |
| 123 - 125 | Abbruch, wenn Schließen |
| 128 | gezeichnete Objekte sichtbar machen |
| 131 | Zyklus der Schleife passend zu vorgegebenen FPS halten |
| 133 - 134 | Aufräumen, wenn Schließen |


## audio

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 3 | import von verwendeten Modulen |
| 5 - 10 | Enum-Klasse für Status des Audio-Outputs |
| 12 - 22 | Music-Klasse, Grundlage für folgend |
| 25 - 32 | Menü- und Spiel-Musik durch Pfade zu MP3s |


## geometry

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 4 | import von verwendeten Modulen |
| (generell) | Klassen, die grafische Objekte darstellen. Werden mit Werten erstellt und besitzen jediglich eine Funktion zum Darstellen auf dem Display. |
| 6 - 14 | Line-Klasse, einfache Linie |
| 17 - 34 | Path-Klasse, Pfad aus mehrerern Linien |
| 27 - 34 | Zeichnen einer Linie nach der anderen |
| 37 - 51 | Rect-Klasse, Rechteck, gefüllt oder ungefüllt |
| 54 - 71 | Circle-Klasse, Kreis, gefüllt oder ungefüllt |


## curve

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 8 | import von verwendeten Modulen |
| 10 - 26 | ConfigCurve-Klasse, einfache Kurve zum Einstellen |
| 22 - 23 | (De-)Aktivierung der Kurve |
| 25 - 26 | Konvertierung zur "richtigen" Kurve |
| 29 - 86 | Curve-Klasse, eigentliche Kurve |
| 46 - 59 | Methoden zum Steuern der Kurve |
| 61 - 64 | Vorwärtsbewegung um Streck in Wegrichtung |
| 66 - 79 | Aktualisierung der Kurve, Bewegung |
| 81 - 86 | Zeichnen der Kurve |


## game

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 2 | import von verwendeten Modulen |
| 4 - 84 | Game-Klasse |
| 12 - 28 | Reaktion auf Tastendrücke -> an Kurven weiterleiten |
| 30 - 75 | wenn Kurve nicht kollidiert, updaten, ansonsten nicht mehr verfolgen und dem Stand beitragen |
| 77 - 84 | Zeichnen des gesamten Spielfeldes |


## menu

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 6 | import von verwendeten Modulen |
| 8 - 27 | Menu-Klasse, Grundmenü, Event-Handling (wird von Aufbauenden weitergeführt) und Zeichnen |
| 30 - 45 | Start-Klasse, Startmenü, Text als Elemente |
| 48 - 115 | Setup-Klasse, Konfigurationsmenü |
| 63 - 81 | Darstellung der Spieler, nach Aktivität unterschieden |
| 85 - 92 | Umwandlung in tatsächliche Kurven |
| 100 - 115 | (De-) Aktivierung der Kurven |
| 118 - 159 | End-Klasse, End-Menü |
| 132 - 153 | Darstellung der Spieler, nach und mit Rang unterschieden |


## text

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 3 | import von verwendeten Modulen |
| 5 - 11 | Text-Klasse, stellt Text mit Schrift dar, Grundlage |
| 13 - 16 | FileText-Klasse, Text, der Schriftart aus Datei lädt |
| 19 - 46 | verschiedene Text(Schrift)-Arten |


## util

| Zeile(n) | Erklärung |
|:-:|:-|
| 1 - 2 | import von verwendeten Modulen |
| 4 - 8 | Funktion zum Laden der Konfiguration |
