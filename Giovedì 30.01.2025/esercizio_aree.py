risultati = []

def area_triangolo():
    base = float(input("Inserire base del triangolo: "))
    altezza = float(input("Inserire altezza del triangolo: "))
    return (base * altezza) / 2


def area_quadrato():
    lato = float(input("Inserire il lato  del quadrato: "))
    return (lato * lato) 


def area_rettangolo():
    base = float(input("Inserire base del rettangolo: "))
    altezza = float(input("Inserire altezza del rettangolo: "))
    return (base * altezza) 


ripetizione = True

while ripetizione:
    print("Che area vuoi calcolare?")
    print("1. triangolo")
    print("2. quadrato")
    print("3. rettangolo")
    print("4. esci")
    
    scelta = input("Inserisci il numero corrispondente alla figura geometrica che vuoi calcolare, o se vuoi  uscire il numero uscita:")
    
    if scelta == "1":
        area_trn = area_triangolo()
        print("L'area del triangolo è: ", area_trn)
        risultati.append(("Triangolo", area_trn))
    
    elif scelta == "2":
        area_qdr = area_quadrato()
        print("L'area del quadrato è: ", area_qdr)
        risultati.append(("quadrato", area_qdr))
    
    elif scelta == "3":
        area_rtn = area_rettangolo()
        print("L'area del rettangolo è:", area_rtn)
        risultati.append(("Rettangolo", area_rtn))
        
    elif scelta == "4":
        ripetizione = False
        print("Uscita dal programma.")
    
    else:
        print("scelta non valida")
        
    
    
print(risultati)

    