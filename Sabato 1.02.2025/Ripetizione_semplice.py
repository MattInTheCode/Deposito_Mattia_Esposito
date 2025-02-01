#Chieda all’utente il proprio nome e la propria età.


#iniziamo creando una variabile con all'interno l'input dell'utente

credenziale_nome = input("inserisci il tuo nome:")

credenziale_età = int(input("Inserisci la tua età:"))

#poi stampiamo un basico messaggio richiamando le variabili nella funzione print

print("ti chiami",credenziale_nome, "e hai",credenziale_età,"anni")


#Richieda all’utente di inserire tre numeri interi.

#anche qui creiamo 3 variabili con input

num1 = int(input("Inserisci un numero intero:"))
num2 = int(input("inserisci il 2° numero intero:"))
num3 = int(input("Inserisci il 3° numero intero:"))

#Calcoli e stampi la somma e il prodotto di questi numeri.

somma = num1 + num2 + num3
prodotto = num1 * num2 * num3

print("questa è la somma:",somma, "questo invece il prodotto:",prodotto,)

#Crea una stringa che dica, ad esempio, "Ciao [nome]! Hai [età] anni."
#Puoi usare la concatenazione o il metodo format()

messaggio = "Ciao ",credenziale_nome,  "! Hai " + str(credenziale_età) + " anni."

print(messaggio)

#Metti i tre numeri in una lista. Modifica il secondo numero (ad es. moltiplicandolo per 2) e stampa la lista modificata.

lista_numeri = []
lista_numeri.append(num1)
lista_numeri.append(num2)
lista_numeri.append(num3)

print (lista_numeri)

scelta=input("vuoi modificare un numero della lista?").strip().lower()

#scelta2=int(input("Va bene, quale numero numero della lista vuoi modificare?"))

if scelta == "si":
    
    scelta2 = int(input("Va bene, quale numero della lista vuoi modificare? "))
    # Verifichiamo che la scelta sia valida:
    
    if 1 <= scelta2 <= len(lista_numeri):
        nuovo_valore = int(input("Inserisci il nuovo valore: "))
        indice = scelta2 - 1  # Per ottenere l'indice corretto (0-based)
        lista_numeri[indice] = nuovo_valore
    
    else:
        print("Scelta non valida.")

print(lista_numeri)

#Crea una tupla con due numeri fissi (ad es. coordinate = (10, 20)) 
# oppure puoi usare valori derivati (ad es. la somma e il prodotto).
# Poi, accedi ai singoli elementi della tupla e stampali.

cordinate= (20, 40)
print("queste sono le cordinate:",cordinate)

scelta3=input("Vuoi stamparle?")

if scelta3 == "si":
    print(cordinate)

elif scelta3 == "no":
    print("va bene.")

else:
    print("scelta non valia")
    

#Usa un’istruzione if per verificare se la somma dei tre numeri è maggiore di 100 e stampare il messaggio corrispondente.

if somma >= 100: 
    print("la somma dei 3 numeri è superiore a 100")

else:
    print("è inferiore")

        
    

