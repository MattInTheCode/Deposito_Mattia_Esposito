'''
#punto 1
controllore = true

#Input per chiedere numero all'utente
while controllore:
    
    numero = int(input("Inserisci un numero: "))


    #codice per definire se è pari o dispari

    #ci stampera a schermo se è pari
    if numero % 2 == 0:
        print(str(numero) + ":" + "è pari.")
    
    #ci stampera a schermo se è dispari
    else:
        print(str(numero) + ":" + "è dispari")
    
    scelta=input("no per uscire")
    
    if(scelta == "no"):
        controllore = False
'''
    

#Punto 2


n2 = int(input("Inserisci un numero: "))

#con questo for decrementiamo comprendendo lo 0 dato dai 2 -1 -1 
for n in range(n2, -1, -1):
    print(":", n)
    
    
    
#Punto 3

#lista numerica

serienumerica = []


for n3 in range(4):
    numeroutente = int(input("Inserisci un numero:"))

    while serienumerica.append(numeroutente):
            serienumerica.sort()
    
            for n3 in serienumerica:
                print(n3**2)
        
    
    





    