
weitermachen = "y"

while weitermachen.lower() == "y":
    print("Geben Sie den Namen vom Raum ein")
    raum_name1 = (input())
    
    print("Wenn der Raum rechteckig ist, geben Sie 'r' ein")
    if input == r 
        print("Geben Sie die Länge der Seite A in Metern an")
        seite_a = int(input())
        print("Geben Sie die Länge der Seite B in Metern an")
        seite_b = int(input())
        raum_fläche1 = seite_a * seite_b 
        print(raum_name1, raum_fläche1)
    else
        print("Teile den Raum in zwei Rechtecke ein. Geben Sie die zwei Seiten vom ersten Rechteck an.")
        print("Geben Sie die Länge der Seite A in Metern an")
        seite_a = int(input())
        print("Geben Sie die Länge der Seite B in Metern an")
        seite_b = int(input())
        print("Geben Sie die zwei Seiten des zweiten Rechtecks an.")
        print("Geben Sie die Länge der Seite C in Metern an")
        seite_c = int(input())
        print("Geben Sie die Länge der Seite D in Metern an")
        seite_d = int(input())
        raum_fläche1 = (seite_a * seite_b) + (seite_c * seite_d)
        print(raum_name1, raum_fläche1) # Variable raum_name1 und raum_fläche1 sollen für jeden Durchlauf hochgezählt werden, damit nicht immer die selbe Variable genutztz wird

    print("Wenn Sie einen weiteren Raum eingeben wollen, geben Sie 'y' ein.")
    print("Wenn Sie keinen weiteren Raum eingeben wollen, geben Sie 'n' ein.")
    weitermachen = input()
    if weitermachen == n
        print(raum_name1, raum_fläche1) # alle Raumnamen mit Flächen sollen ausgegeben werden
