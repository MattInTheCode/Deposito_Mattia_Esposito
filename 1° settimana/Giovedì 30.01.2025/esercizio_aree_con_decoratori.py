aree_calcolate = []

def calcola_area(figura):
    def wrapper():
        misure = figura()
        
        #la divisione per 2 è solo quella del triangolo
        area = misure[0] * misure[1] / misure[2]  
        
        #Salva il nome della figura e l'area
        
        #la funzione __name__ l'ho trovata online, semplicemente contiene il nome della funzione come stringa
        
        aree_calcolate.append((figura.__name__, area))  
        
        return area
    return wrapper

@calcola_area
def area_triangolo():
    base = float(input("Inserire base del triangolo: "))
    altezza = float(input("Inserire altezza del triangolo: "))
   
    # Il 2 serve per dividere l'area del triangolo

    return base, altezza, 2  

@calcola_area
def area_quadrato():
    lato = float(input("Inserire il lato del quadrato: "))

#utilizziamo l'1 poichè il 2 è riservato all'area del triangolo
    return lato, lato, 1  


@calcola_area
def area_rettangolo():
    base = float(input("Inserire base del rettangolo: "))
    altezza = float(input("Inserire altezza del rettangolo: "))
    return base, altezza, 1

#richiamo le funzioni

area_triangolo()
area_quadrato()
area_rettangolo()

#stampiamo la lista

print(aree_calcolate)