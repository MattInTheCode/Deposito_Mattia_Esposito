
#utente 0

utente_esistente = "Aldo"
password_esistente = "aldomoro00"
id_utente = 0


#utente 1

utente_esistente_1 = "MarcheroZuchembergo"
password_esistente_1 = "metatema"
id_utente_1 = 1



#Input utente Login

utente = input("Inserisci nome utente: ")
password = input("Inserisci la password: ")
login_successful = False


#Risposta al login

if (utente.lower() == utente_esistente.lower() and password == password_esistente):
    input("Benvenuto a bordo! Ora manca un ultimo step!")
    login_successful = True
elif(utente.lower() == utente_esistente_1.lower() and password == password_esistente_1):
    print("Benvenuto a bordo! Ora manca un ultimo step!")
    login_successful = True

else:
    print("Questo account non è nel database")

#Cambio nome utente o password

if login_successful:
    print("vuoi cambiare credenziali?")
    credenziali = input("Sì o No :")
    
    if(credenziali.upper() == "Sì"):
        print("Scegli nuovo NomeUtente")
        nuovonomeutente = input()
        nuovonomeutente = utente.replace()
    
    else:
        print("Puoi procedere!")
        

#KYC Utente se login andato a buon fine

if login_successful:
    print("Verifica KYC quale scegli fra A o B")
    scelta = input("A o B?")

    if(scelta.upper() == "A"):
        print("Qual'è la tua città preferita?")
        kyc = input()
        if kyc.lower() == "santorini":
            print("Risposta corretta!")
        else:
            print("Risposta errata.")
    elif(scelta.upper() == "B"):
        print("Il nome del tuo gatto?")
        kyc = input()
        if kyc.lower() == "gianfranco":
            print("Risposta corretta!")
        else:
            print("Risposta errata.")
    else:
         print("Errore nella risposta")  
                  
#nel caso non sia andato a buon fine.   
       
else:
    print("Login errato, verifica KYC annullata.")   
  

