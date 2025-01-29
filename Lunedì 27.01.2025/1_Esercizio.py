nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
eta = int(input("Inserisci la tua età: "))
altezza = float(input("Quanto sei alto? "))
lavori = bool(input("Lavori? (1/0): ")) 


risposta = "Ciao, " + nome + " " + cognome + ", hai " + str(eta) + " anni, sei alto " + str(altezza) + " metri e lavori: " + str(lavori) + "."

print(len(risposta.upper()))
print(risposta.replace('anni', 'mesi'))