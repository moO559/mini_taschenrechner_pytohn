print("Willkommen beim Mini-Rechner!")

# Die Hauptschleife
while True:
    try:
        # Eingaben vom Benutzer 
        zahl1 = float(input("Gib die erste zahl ein: "))
        operator = input("Gib den operator ein (+, -, *, /): ")
        zahl2 = float(input("Gib die zweite zahl ein: "))

        # Rechnen 
        if operator == "+": 
            ergebnis = zahl1 + zahl2
        elif operator == "-":
            ergebnis = zahl1 - zahl2
        elif operator == "*":
            ergebnis = zahl1 * zahl2
        elif operator == "/":
            if zahl2 != 0:
                ergebnis = zahl1 / zahl2
            else: 
                ergebnis = "Fehler: Division durch 0"
        else:
            ergebnis = "Ungültiger Operator"
    except ValueError:
        ergebnis = "Bitte gib gültige zahlen ein!"

        # Ergebnis anzeigen 
        print("Ergebnis:", ergebnis)


        nochmal = input("Möchtest du nochmal rechnen? (ja/nein): ")
        if nochmal.lower() != "ja":
            print("Danke für die Nutzung! Tschüss.")
            break