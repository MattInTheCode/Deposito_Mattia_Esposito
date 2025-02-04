import classe_Libro


class Libreria:
    
    
    
    def __init__(self, classe_Libro):
        self.catalogo = catalogo
        catalogo = []
        
        
        
    
    
    def aggiungi_libro(self):
        
        titolo = input("Titolo del libro: ")
        autore = input("Autore del libro: ")
        isbn = input("Codice ISBN:")
    
        nuovo_libro = classe_Libro.Libro(titolo, autore, isbn)
        self.catalogo.append(nuovo_libro)
        print("Libro aggiunto al catalogo.")
    
    def rimuovi_libro(isbn):
        
        rimuovi_isbn = input("inserisci il codice isbn")
        
        for libro in self.catalogo:
            if libro.isbn == rimuovi_isbn:
                self.catalogo.remove(libro)
                print("Libro rimosso dal catalogo.")
                return
        
        
        else:
            print("Libro non trovato nel catalogo.")
            
            
    def cerca_per_titolo(self):
        
        cerca_titolo = input("Inserisci il titolo del libro che cerchi: ")
    
    for libro in self.catalogo:
        
        if libro.titolo.lower() == cerca_titolo.lower():
            
            print("Il libro:", cerca_titolo, "è nel catalogo.")
            return libro 

        else:
            print("libro non trovato")
            break
    
           
            
    def mostra_catalogo(self):
        if not self.catalogo:
            print("Il catalogo è vuoto.")
        else:
            print("Catalogo della libreria:")
            for libro in self.catalogo:
                print(libro.descrizione())
            