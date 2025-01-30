risultati = []


def quadrato(numero):
    return numero * numero 

num = int(input("Inserisci un numero che vuoi al quadrato:"))
risultato1 = quadrato(num)
risultati.append(risultato1)
print(risultato1)


def cubo(n):
    return n * n * n

num = int(input("Inserisci un numero che vuoi al cubo:"))
risultato2= cubo(num)
risultati.append(risultato2)
print(risultato2)

def quarta(n):
    return n * n * n * n

num = int(input("Inserisci un numero che vuoi alla quarta:"))
risultato3= quarta(num)
risultati.append(risultato3)
print(risultato3)


def quinta(n):
    return n * n * n * n * n 

num = int(input("inserisci un numero che vuoi alla quinta:"))
risultato4= quinta(num)
risultati.append(risultato4)
print(risultato4)


print("Tutti i risultati:", risultati)