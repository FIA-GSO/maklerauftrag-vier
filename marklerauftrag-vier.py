
#Tool zur Berechnung von Räumen, Ausgabe von Raumname mit jeweiliger Fläche in m²
#Programm mit einer while Schleife, alle schon eingegebenen Räume werden in einer Tupel/Liste zwischengespeichert
#Fragt erst Raumname ab, dann muss der User gucken, ob der Raum einfach rechteckig ist oder nicht
#wenn er rechteckig ist wird einfach die Raumgröße durch die eingabe der beiden Seiten ausgerechnet
#wenn er nicht recheckig ist, wird der User aufgefordert, ihn in 2 Rechtecke aufzuteilen und dann wird daraus gerechnet
#am Ende wird der User gefragt ob ein weiterer Raum ausgerechnet werden soll
#bei yes startet die Schleife von vorne, bei no Endet die Schleife und alle gespeicherten Räume werden ausgegeben

weitermachen = "y" #Variable für eine Schleife

räume = [] #hier werden alle Räume als Tupel (unveränderbare Liste) gespeichert

while weitermachen.lower() == "y": #while Schleife, 'y' und 'Y' wird akzeptiert
    print("Geben Sie den Namen vom Raum ein:") #Abfrage Name vom Raum
    raum_name = input() #Benutzer gibt Name ein
    
    print("Wenn der Raum rechteckig ist, geben Sie 'r' ein:") #Abfrage, ob der Raum Rechteckig ist
    form = input().lower() #in Variable gespeichert, 'r' und 'R'  wird akzeptiert

    if form == 'r': #Prüfung ob der Nutzer 'r' eingegeben hat
        print("Geben Sie die Länge der Seite A in Metern an:") 
        seite_a = int(input()) #Nutzer gibt Zahl ein, int() wandelt es in ganze Zahl um
        print("Geben Sie die Länge der Seite B in Metern an:")
        seite_b = int(input()) #dasselbe für Seite b
        raum_fläche = seite_a * seite_b #beide Seiten werden multipliziert für die Quadratmeter
    else:
        print("Teile den Raum in zwei Rechtecke ein. Geben Sie die zwei Seiten vom ersten Rechteck an.") #Hinweis für den Nutzer zum rechnen
        print("Geben Sie die Länge der Seite A in Metern an")
        seite_a = int(input())
        print("Geben Sie die Länge der Seite B in Metern an")
        seite_b = int(input()) #gibt Seiten für das erste Rechteck an
        print("Geben Sie die zwei Seiten des zweiten Rechtecks an.")
        print("Geben Sie die Länge der Seite C in Metern an")
        seite_c = int(input())
        print("Geben Sie die Länge der Seite D in Metern an")
        seite_d = int(input()) #gibt Seiten für das zweite Rechteck an
        raum_fläche = (seite_a * seite_b) + (seite_c * seite_d) #beide Seiten werden multipliziert und die beiden Räume addiert für die Quadratmeter

    räume.append((raum_name, raum_fläche)) #Name und Fläche werden in der Tupel Liste gespeichert

    print(f"{raum_name}: {raum_fläche} m²") #greade errechneter Raum wird mit Name und Fläche ausgegeben, f-String, Einheit m² wird gesetzt

    print("Wenn Sie einen weiteren Raum eingeben wollen, geben Sie 'y' ein.") #Abfrage ob ein Neuer Raum hinzugefügt werden soll
    print("Wenn Sie keinen weiteren Raum eingeben wollen, geben Sie 'n' ein.") #wenn 'n' endet die Schleife
    weitermachen = input() #neue Eingabe für 'weitermachen'

print("--- Alle Räume und Flächen ---") #Ausgabe aller eingespeicherten Räume und deren Fläche aus der Tupel
for name, fläche in räume: #aus Tupel 'Räume', gibt die jeweils gespeicherten Werte für 'Name' und 'Fläche'
    print(f"{name}: {fläche} m²") #Ausgabe, setzt m² als Einheit
