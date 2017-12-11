# Benutzung

## Installation
Dieses Spiel benötigt die unter `requirements.txt` aufgeführten Pytho-Module. Installierbar durch:
```shell
pip(3) install -r requirements.txt
```

Außerdem benötigt das Spiel Python3.

## Starten
Das Spiel muss aus dem `src` Ordner heraus mit Python3 über `main.py` gestartet werden, um alle relativ geladenen Ressourcen finden zu können.

Beispiel für POSIX:
```shell
user@pc /pfad/zum/spiel $ cd src
user@pc /pfad/zum/spiel/src $ python3 main.py
```

## Bedienung
Die Menüs / Dialogfelder können mit Enter bestätigt werden. Im "Setup" Menü können die einzelnen Kurven gemäß der Mitspielerzahl mit den Tasten `1`, `2`, `3` und `4` aktiviert (farbig) und deaktiviert (grau) werden.
Hinter aktivierten Kurven stehen die Tasten zum Steuern (Format: "links + rechts"). Nach bestätigung des Menüs beginnt das Spiel. Nach Beendigung dessen erscheint das Dialog-Feld zum Abschluss. Enter startet erneut mit dem Setup.
