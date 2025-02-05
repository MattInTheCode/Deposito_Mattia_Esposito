#Classe Genitrice che conterra per tutti il costruttore con i parametri eta e nome memorizzati come variabili d'istanza

class MembroSquadra:
    
    #costruttore della classe che dara nome e eta come attributi a ogni giocatore
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    #descrizione del giocatore che entrerà in campo
    def descrizione(self):
        return self.nome, "età:", self.eta, "si prepara ad entrare in campo."



#1° classe figlia Giocatore tutte e 3 le classi estenderanno MembroSquadra

class Giocatore(MembroSquadra):
    #con super prendiamo il costruttore __init__ della classe base e gli aggiungiamo l'attributo numero_maglia e i ruoli possibili
    def __init__(self, nome, eta, numero_maglia):
        super().__init__(nome, eta)
        self.numero_maglia = numero_maglia
        self.ruoli = []
    
    #metodo per aggiungere ruoli alla lista 
    
    def aggiungi_ruolo(self, ruolo):
        self.ruoli.append(ruolo)

    #ci mostrera la lista dei ruoli assegnati
    
    def mostra_ruoli(self):
        return self.ruoli

    #ci restituirà il nome del giocatore numero maglia e il ruolo
    
    def gioca_partita(self):
        return self.nome, "numero", self.numero_maglia, "giocherà come:", self.mostra_ruoli()

#2° classe figlia  Allenatore


class Allenatore(MembroSquadra):
    #stessa cosa del super di sopra solo che aggiungiamo anni_di_esperienza.
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    #ci restituira la stringa con gli anni maturati dall'allenatore + il suo nome
    def dirige_allenamento(self):
        return self.nome, "colui che ha maturato:", self.anni_di_esperienza, "prepara insieme alla squadra un piano d'attacco."

#3° classe figlia  Assistente


class Assistente(MembroSquadra):
    #idem delle altre classi
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    
    
    def supporta_allenamento(self):
        return self.nome, "supporta durante gli allenamenti."

#funzione che richiede all'utente l'inserimento di nome età e n°maglia

def crea_giocatore():
    nome = input("Inserisci il nome del giocatore: ")
    eta = input("Inserisci l'età del giocatore: ")
    numero_maglia = input("Inserisci il numero di maglia: ")
    giocatore = Giocatore(nome, eta, numero_maglia)

#ciclo che aggiunge ruoli finche non dice stop se non ha un ruolo assegnato solo stop
    while True:
        ruolo = input("Inserisci un ruolo per il giocatore (o 'stop' per terminare): ")
        if ruolo.lower() == 'stop':
            break
        giocatore.aggiungi_ruolo(ruolo)

    return giocatore

#funzione che richiede all'utente l'inserimento uguale a crea giocatore solo che al posto di n°maglia chiede anni di esperienza

def crea_allenatore():
    nome = input("Inserisci il nome dell'allenatore: ")
    eta = input("Inserisci l'età dell'allenatore: ")
    anni_di_esperienza = input("Inserisci gli anni di esperienza dell'allenatore: ")
    allenatore = Allenatore(nome, eta, anni_di_esperienza)
    return allenatore

#funzione che richiede all'utente l'inserimento uguale ai precedenti solo che da anche la tipologia d'assistenza

def crea_assistente():
    nome = input("Inserisci il nome dell'assistente: ")
    eta = input("Inserisci l'età dell'assistente: ")
    tipo_assistente = input("Inserisci il tipo di assistente")
    assistente = Assistente(nome, eta,tipo_assistente)
    return assistente

#funzione menu  dove  nel ciclo ogni numero avra una scelta
def mostra_menu():
    print( "Menu" )
    print("1. Crea un giocatore")
    print("2. Crea un allenatore")
    print("3. Crea un assistente")
    print("4. Mostra tutti i giocatori")
    print("5. Mostra tutti gli allenatori")
    print("6. Mostra tutti gli assistenti")
    print("7. Esci")


#facciamo partire i dizionari per memorizzare 
giocatori = {}
allenatori = {}
assistenti = {}

# Ciclo per il menumenu
while True:
    mostra_menu()
    scelta = input("Scegli un'opzione: ")

#scelta 1 richiamera il crea_giocatore

    if scelta == "1":
        giocatore = crea_giocatore()
        giocatori[giocatore.nome] = giocatore

#scelta 2 creera l'allenatore richiamando come il primo
    elif scelta == "2":
        allenatore = crea_allenatore()
        allenatori[allenatore.nome] = allenatore
# e così via per le altre scelte
    elif scelta == "3":
        assistente = crea_assistente()
        assistenti[assistente.nome] = assistente

    elif scelta == "4":
        if giocatori:
            for nome, giocatore in giocatori.items():
                print(giocatore.nome, "numero", giocatore.numero_maglia, "giocherà come:", giocatore.ruoli)
        else:
            print("Nessun giocatore creato.")

    elif scelta == "5":
        if allenatori:
            for nome, allenatore in allenatori.items():
                print(allenatore.nome, "età:", allenatore.eta, "con", allenatore.anni_di_esperienza, "anni di esperienza.")
                print(allenatore.dirige_allenamento())
        else:
            print("Nessun allenatore creato.")

    elif scelta == "6":
        if assistenti:
            for nome, assistente in assistenti.items():
                print(assistente.nome, "età:", assistente.eta, "è un assistente.")
                print(assistente.supporta_allenamento())
        else:
            print("Nessun assistente creato.")

    elif scelta == "7":
        print("Uscita dal programma.")
        break

    else:
        print("Opzione non valida, riprova.")
