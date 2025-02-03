# Chiedere all'utente di inserire i due numeri e l'operazione
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")

# Lista delle operazioni valide
operazioni = ["+", "-", "*", "/"]

# Se l'operazione non utilizza quelle in operazioni  non funzionerà
if operazione in operazioni:
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
else:
    print("Operazione non valida")