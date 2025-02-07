#classe genitrice
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome 
        self.numero_soldati= numero_soldati
        
        
    
    def muovi(self):
        print("La squadra",self.nome,"si muove verso l'obbiettivo")
        
    
    def attacca(self):
        print(self.nome,"si appostano per attaccare")
    
    def ritira(self):
        print(self.nome,"RITIRATA!! RITIRATA!! RITIRATA!!")


#classi figlie: 

class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def costruisci_trincea(self):
        print(self.nome, "non avete vie di fuga preparate una trincea!")



class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati) 
           
    def calibra_artiglieria(self):
        print(self.nome, "Calibrate l'artigleria!")



class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def esplora_terreno(self):
        print(self.nome, "vanno in avanscoperta in cerca di tracce")
    



class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def rifornisci_unita(self):
        print(self.nome, "rifornisce l'unità")        



class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def conduci_ricognizione(self):
        print(self.nome, "Conduce momentaneamente la ricognizione")


# classe con ereditarieta multipla da  fanteria e ricognizione
class FanteriaRicognizione(Fanteria, Ricognizione):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

#classe non figlia ma che controlla        
class ControlloMilitare:
    def __init__(self):
        self.unita_registrate = {}

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print("Unità " , unita.nome , " registrata con successo.")

    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        else:
            print("Unità registrate:")
            for nome, unita in self.unita_registrate.items():
                print("- " + nome + ": " + str(unita.numero_soldati) + " soldati.")

    def dettagli_unita(self, nome):
        if nome in self.unita_registrate:
            unita = self.unita_registrate[nome]
            print("Dettagli dell'unità " ,nome , ":")
            print("Numero di soldati: " , str(unita.numero_soldati))
        else:
            print("Unità " , nome , " non trovata.")



controllo = ControlloMilitare()

#richieste all'utente

nome_fanteria= input("Nome da dare alla fanteria:")
numero_soldati_fanteria = int(input("Numero di soldati:"))

fanteria = Fanteria(nome_fanteria, numero_soldati_fanteria)
controllo.registra_unita(fanteria)



nome_artiglieria= input("Nome da dare all'artiglieria':")
numero_soldati_artiglieria = int(input("Numero di soldati:"))

artiglieria = Artiglieria(nome_artiglieria, numero_soldati_artiglieria)
controllo.registra_unita(artiglieria)



nome_sqr_mist = input("nome della squadra mista fanteria + ricognizione:")
numero_sqr_mist = int(input(" numero di soldati della squadra mista: "))

sqr_mist = FanteriaRicognizione(nome_sqr_mist,numero_sqr_mist)
controllo.registra_unita(sqr_mist)

controllo.registra_unita(fanteria)
controllo.registra_unita(artiglieria)

controllo.mostra_unita()

richiesta_unita = input("Nome dell'unità da controllare:")
controllo.dettagli_unita(richiesta_unita)


#esecuzioni


fanteria.muovi()
fanteria.costruisci_trincea()
artiglieria.calibra_artiglieria()


sqr_mist.muovi() 
sqr_mist.costruisci_trincea()
sqr_mist.conduci_ricognizione()