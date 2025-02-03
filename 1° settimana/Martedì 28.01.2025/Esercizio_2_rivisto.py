# definizione base delle variabili
operazione = ""
numero1 = 0
numero2 = 0

# questo ciclo permettera al programma di continuare a eseguire il codice finche l'utente non utilizzera gli operatori giusti.
while operazione not in ["+", "-", "*", "/"]:
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))
    operazione = input("Inserisci l'operazione (+, -, *, /): ")

    if operazione not in ["+", "-", "*", "/"]:
        print("Operazione non valida. Riprova.")

# Esegue l'operazione
if operazione == "+":
    risultato = numero1 + numero2
    print("Risultato: " + str(risultato))
elif operazione == "-":
    risultato = numero1 - numero2
    print("Risultato: " + str(risultato))
elif operazione == "*":
    risultato = numero1 * numero2
    print("Risultato: " + str(risultato))
elif operazione == "/":
    risultato = numero1 / numero2
    print("Risultato: " + str(risultato))