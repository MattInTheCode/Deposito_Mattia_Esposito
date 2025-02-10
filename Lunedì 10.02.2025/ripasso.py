'''
def frequenza_di_comparsa(stringa):
    frequenza = {}
    for carattere in stringa:
        if carattere in frequenza:
            frequenza[carattere] += 1
        else:
            frequenza[carattere] = 1
    return frequenza

stringa = input("Inserisci una stringa: ")

risultato = frequenza_di_comparsa(stringa)

print(risultato)
'''



#Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti, quando l’utente scrive media il programma andrà a stampare i nomi di tutti  gli alunni e per ogni alunno
# la media dei voti. Esempio: Nome: Giovanni , Media: 7.5 Nome: Alfredo , Media: 9 Nome: Michela, Media 10


def calcolo_media_voti(voti,nome):
    if nome in voti:
        return sum(voti[nome])/len(voti[nome])
    else:
        return None
    



voti_studenti = {
    
}


while True:
    print("Menu")
    print("1. Aggiungi studente")
    print("2. Media voti ")
    print("3. Esci")
    
    scelta = input("Seleziona un numero corrispettivo all'opzione:")
    
    
    if scelta == "1":
        
        nome_studente = input("Inserire nome dello studente da aggiungere:")
        voti = input("inserire i voti dello studente separati da spazio").split()
        voti_studenti[nome_studente] = [int(voto) for voto in voti]
        print("I voti di:",nome_studente)
    elif scelta == "2":
        studente= input("inserire il nome dello studente:")
        media = calcolo_media_voti(voti_studenti,studente)
        if media is not None:
            print("Media",media, "di" ,studente)
    
    elif scelta == "2":
        print("chiusura script.")
        break
    else:
        print("scelta non valida.")