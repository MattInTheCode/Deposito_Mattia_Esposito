ista_utenti=[]
id = 0

aggiunte= int(input("quanti utenti vuoi aggiungere"))

while(len(lista_utenti )<=aggiunte):
utente2=[]
nome = input("isnerisci il tuo nome")
utente2.append(nome)
password = input("isnerisci la password")
utente2.append(password)
id +=1
utente2.append(id)

lista_utenti.append(utente2)
print(utente2)
print(lista_utenti)

print(lista_utenti)