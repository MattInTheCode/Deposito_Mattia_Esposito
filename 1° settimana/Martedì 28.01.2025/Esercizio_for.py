while True:
    numero = int(input("Inserisci il primo numero: "))
    
    # Con il ciclo for e range facciamo il conto alla rovescia
    for n in range(numero, -1, -1):  # si parte dal numero fino ad'arrivare a 0
        print(n)
    
    # Chiediamo se l'utente vuole ripetere il programma
    risposta = input("Vuoi ripetere? (sì/no): ")
    if risposta.lower() != "sì":
        break