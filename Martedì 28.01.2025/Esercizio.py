utente_esistente = "Aldo"
password_esistente = "aldomoro00"
id_utente = 0

utente_esistente_1 = "MarcheroZuchembergo"
password_esistente_1 = "metatema"
id_utente_1 = 1

utente = input("Inserisci nome utente: ")
password = input("Inserisci la password: ")

if utente != utente_esistente:
    nuovo_id = id_utente + 1
    print("Creazione account in corso. . .")
    print("Account creato con successo!")
else:
    print("Questo nome utente è già registrato nel sistema.")
    print("Utilizza un nome utente differente.")