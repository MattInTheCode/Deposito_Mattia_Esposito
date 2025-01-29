Anni = int(input("Inserire età: "))

if Anni >= 18:
    print("Puoi vedere questi film:")
else:
    print("Mi dispiace, sei minorenne e non puoi accedere.")
    
# Lista dei film
lista_film = ["The Mask", "Interstellar", "Bad Boys"]

# Ciclo per i film + scelta
if Anni >= 18:
    film = 0   
    
    #ogni numero è associato a un film
    while film < len(lista_film):
        print(str(film + 1) + ". " + lista_film[film]) 
        film += 1  
    
    
    scelta = int(input("Scegli un numero per vedere il film: "))
    
    #
    if 1 <= scelta <= len(lista_film):
        print("Hai scelto: ", lista_film[scelta - 1])  
    else:
        print("Scelta non valida.")