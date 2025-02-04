class Pokemon:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print("il pokemon emette un suono generico.")

class Dialga(Pokemon):
    def fai_suono(self):
        print(self.nome, "GRGRRGRGRGDFH!")
    
    def azione(self):
        print(self.nome, "Usa iperraggio!")

class Palkia(Pokemon):
    def fai_suono(self):
        print(self.nome, "osdudowowudo")
    
    def azione2(self):
        print(self.nome, "Usa dragospiro!")

class Giratina(Pokemon):
    def fai_suono(self):
        print(self.nome, "wriiii!")
    
    def azione3(self):
        print(self.nome, "Usa dragartigli")

# Esempio di utilizzo
Dialga = Dialga("Dialga", 999)
Palkia = Palkia("Palkia", 998)
Giratina = Giratina("Giratina", 997)

Dialga.fai_suono()
Dialga.azione()

Palkia.fai_suono()
Palkia.azione2()

Giratina.fai_suono()
Giratina.azione3()
