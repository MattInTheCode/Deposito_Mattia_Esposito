class Ristorante:
    def __init__(self,nome,tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu_piatti = []
        self.menu_prezzi = []

    # funzione che stamperà la bio del ristorante
    def descrivi_ristorante(self):
        desc = "Il ristorante " + self.nome + " si occupa di cucina " + self.tipo_cucina  
        return desc
    
    # funzione che ci dice se è chiuso o aperto 
    def stato_apertura(self):
        if self.aperto:
            stato = "Il ristorante è aperto"
        else:
            stato = "È chiuso"
        print(stato)  
        return stato
    
    # funzione che apre il ristorante
    def apri_ristorante(self):
        apertura_ristorante = input("Vuoi aprire il ristorante? si/no ").lower()
        
        if apertura_ristorante == "si":
            self.aperto = True
            print("Il ristorante è ora aperto")
        
        elif apertura_ristorante == "no":
            self.aperto = False 
            print("Il ristorante rimane chiuso")
        else:
            print("Scelta non valida")

    # funzione che aggiunge piatti e prezzo al menu
    def aggiungi_al_menu(self):
        nuovo_piatto = input("Inserisci il nome del piatto da aggiungere al menu: ")
        nuovo_prezzo = input("Inserisci il prezzo del piatto: ")
    
        self.menu_piatti.append(nuovo_piatto)
        self.menu_prezzi.append(nuovo_prezzo)
        
        print("Il piatto aggiunto è:", nuovo_piatto, "al prezzo di:", nuovo_prezzo, "€")
    
    # funzione che rimuove dal menu
    def togli_dal_menu(self):
        piatto = input("Inserisci il nome del piatto da rimuovere dal menu: ")
        
        #codice copiato da chatgpt per il del che elimina direttamente il piatto
        
        if piatto in self.menu_piatti:
            indice = self.menu_piatti.index(piatto)
            del self.menu_piatti[indice]
            del self.menu_prezzi[indice]
            
            print("Piatto:", piatto, "rimosso dal menu.")
        else:
            print("Il piatto non è presente nel menu.")
            
    # stampa finale
    def stampa_menu(self):
        if not self.menu_piatti: 
            print("Nel menù non c'è nulla")
            return
        print("Menù:")
        for i in range(len(self.menu_piatti)):
            print(self.menu_piatti[i], self.menu_prezzi[i], "€")


# Creiamo un'istanza del ristorante
mio_ristorante = Ristorante("Thaistafermo", "Thai")

# Stampiamo la descrizione del ristorante
print(mio_ristorante.descrivi_ristorante())

# Controlliamo se il ristorante è aperto o chiuso
mio_ristorante.stato_apertura()

#scelta se aprire il ristorante
mio_ristorante.apri_ristorante()

# Aggiungiamo piatti al menu
mio_ristorante.aggiungi_al_menu()
mio_ristorante.aggiungi_al_menu()

# Stampiamo il menu
mio_ristorante.stampa_menu()

# Rimuoviamo un piatto dal menu
mio_ristorante.togli_dal_menu()

# Stampiamo di nuovo il menu aggiornato
mio_ristorante.stampa_menu()