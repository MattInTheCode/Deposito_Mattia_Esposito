



class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome 
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.lista_prodotti = []
        self.prezzo_prodotti = []
        
    def calcola_profitto(self):   
        return self.prezzo_vendita - self.costo_produzione
        
    def calcola_profitto(self):   
       
        return self.prezzo_vendita - self.costo_produzione
    
    
    def descrizione(self):
        
        desc = "prodotto: " ,self.nome , "costo di produzione:" , self.costo_produzione, "€",  
        return desc
        


class elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
        
        
        pass

    def descrizione(self):
        
        desc = "prodotto: " ,self.nome , "Durata garanzia:" , self.garanzia, 
        return desc


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
    
    
    def descrizione(self):
        
        desc = "prodotto: " ,self.nome , "Materiale:" , self.materiale, 
        return desc      
      



        
        
    def calcola_profitto(self):   
       
        return self.prezzo_vendita - self.costo_produzione
    
    
    def descrizione(self):
        
        desc = "prodotto: " ,self.nome , "costo di produzione:" , self.costo_produzione, "€",  
        return desc
        


class elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, marca):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.marca = marca
        pass

class Abbigliamento:
    def __init__(self):
        pass



class Fabbrica:
    def __init__():
        pass
    