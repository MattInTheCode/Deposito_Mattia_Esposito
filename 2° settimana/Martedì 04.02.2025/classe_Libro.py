class Libro:
    
    isbn = 0
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn + 1
        isbn += 1
        
    
    def descrizione(self):
        bio = self.titolo + " di " + self.autore + ", " + "il codice isbn è:" + self.isbn
        return bio
