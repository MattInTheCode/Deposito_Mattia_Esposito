class Persona:
    
    def __init__(self, nome, eta):
        self.__nome = nome  
        self.__eta = eta
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome    
    
    def get_eta(self):
        return self.__eta    
    
    def set_eta(self, nuova_eta):
        self.__eta = nuova_eta
        
    def presentazione(self):

        return("Sono",self.__nome,"e ho", self.__eta ,"anni")

presentazione1 = Persona("Antonio", 20)
print(presentazione1.presentazione())

'''
print("Nome:", presentazione1.get_nome())
print("Età:", presentazione1.get_eta())
presentazione1.set_nome("Marco")
presentazione1.set_eta(25)
print(presentazione1.presentazione())
'''
class Studente(Persona):
    def __init__(self, nome, eta, voti=None):
        
        super().__init__(nome, eta)
        if voti is None:
            self.__voti = []  
        else:
            self.__voti = voti
            
            
    def aggiungi_voto(self, voto):
        if 0 <= voto <= 10:  
            self.__voti.append(voto)
        else:
            print("Errore: Il voto deve essere tra 0 e 10.")    
    def get_voti(self):
        return self.__voti

    def calcolo_media_voti(self):
        if len(self.__voti) >= 1:
            return sum(self.__voti) / len(self.__voti)
        
        else: 
            print("Lo studente non ha voti registrati")
            return 
    
    def presentazione(self):
        media = self.calcolo_media_voti()
        return(super().presentazione(), "e questa è la mia media:",media, )
        
s = Studente("Marco", 20)

s.aggiungi_voto(8)
s.aggiungi_voto(9)
s.aggiungi_voto(0)
s.aggiungi_voto(10)
s.aggiungi_voto(5)
  

print(s.presentazione())

class Professore(Persona):
    def __init__(self,nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
    def get_materia(self):
        return self.__materia
    
    def set_materia(self, nuova_materia):
        self.__materia = nuova_materia            
            
    pass
    

