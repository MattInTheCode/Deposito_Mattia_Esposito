# Lista numeri pari
numeri_pari = []
count_pari

def è_pari(n):
    return n % 2 == 0

while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))

    if è_pari(numero):
        numeri_pari.append(numero)
        print(f"{numero} è pari.")
        
    else:
        print(f"{numero} è dispari")

print("Hai trovato 5 numeri pari:", numeri_pari)