class Calcolatrice:
    @staticmethod
    def somma(valore1, valore2):
        return valore1 + valore2
    
    def differenza(valore1, valore2):
        return valore1 - valore2 


valore_somma=float(input("inserisci un valore:"))
valore_somma2=float(input("inserisci un valore:"))

valore_differenza=float(input("inserisci un valore:"))
valore_differenza2=float(input("inserisci un valore:"))

# Utilizzo:
print("La somma dei 2 numeri è:",Calcolatrice.somma(valore_somma, valore_somma2))  # Output: 8

print(Calcolatrice.differenza(valore_differenza,valore_differenza2))