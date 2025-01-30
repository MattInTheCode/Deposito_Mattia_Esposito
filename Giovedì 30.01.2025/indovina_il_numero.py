# Funzione per creare un numero casuale tra 1 e 100
def randomizzatore():
    
    # utilizza il tempo attuale per generare un numero random
    
    tempo_decimale = int(str(time.time()).split('.')[1])
    
    # Qui invece usiamo una serie di numero random
    moltiplicatore = 432454364379  
    
    # Operazioni per combinare le variabili
    
    # avremo così il resto della divisione x 100
    
    risultato = (tempo_decimale * moltiplicatore) % 100  
    #per comprendere 1 e 100 
    return risultato + 1 

# Importiamo il modulo time per ottenere il tempo corrente
import time

# Esecuzione del randomizzatore
numero_casuale = randomizzatore()

#Messaggio di benvenuto

print("Benvenuto!")


#ciclo finche l'utente non indovina il numero
Controllore = True

while Controllore:
    
    Numero_Utente = int(input("Scegli un numero da 1 a 100:"))

    #se l'utente indovina il numero
    if Numero_Utente == numero_casuale: 
        print("Congratulazioni sei riuscito a indovinare il numero!")
        
        #Si stoppa se finisce
        Controllore = False
    
    # se il Numero è più alto 
    elif Numero_Utente > numero_casuale:
        print("Sbagliato il numero è più piccolo")
    # se è più basso  
    elif Numero_Utente < numero_casuale:
        print("Sbagliato il numero è più grande")
    
    
    
    


