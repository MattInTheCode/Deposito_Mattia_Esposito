lista_valori=[]

valore1 = int(input("Aggiungi valore numerico"))
valore2 = int(input("Aggiungi valore numerico"))
valore3 = int(input("Aggiungi valore numerico"))

if valore1 > 0 and valore2 > 0 and  valore3 >0 :
    lista_valori.append(valore2)
    lista_valori.append(valore3)
    lista_valori.append(valore1)
   
    if len(lista_valori) > 0 :
        lista_valori.sort()
        print(lista_valori)