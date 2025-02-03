#Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto
# da 'autore' e ha 'pagine' pagine.".

class Libro:

    def __init__ (self, titolo, autore, pagine, editore):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        #ho aggiunto editore di mio per una miglior comprensione degli attributi
        self.editore = editore
        
    def descrizione(self):
        bio = self.titolo + " di " + self.autore + ", " + str(self.pagine) + " pagine" + " ed'è edito da " + self.editore 
        return bio

libro1 = Libro("Il Grande Gatsby", "F. Scott Fitzgerald", 180, "Feltrinelli Editore.")
libro2 = Libro("Il Signore degli anelli","J. R. R. Tolkien",1221, "Giunti, 2012")
print(libro1.descrizione())
print(libro2.descrizione())