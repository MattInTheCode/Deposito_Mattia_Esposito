class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
        
    def __metodo_privato(self):
        return "questo è un metodo privato"
    

obj = MiaClasse()

print(obj._MiaClasse__variabile_privata)