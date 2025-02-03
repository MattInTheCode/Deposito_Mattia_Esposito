#Crea una classe chiamata Punto. Questa classe dovrebbe avere:
#Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
#Un metodo muovi che prenda in input un valore per dx e un valore per dy 
#e modifichi le coordinate del punto di questi valori.
#Un metodo distanza_da_origine che restituisca la distanza del punto 
#dall'origine (0,0) del piano.

class Punto:
    def __init__(zona, x=0, y=0):
        zona.x = x
        zona.y = y

    def muovi(zona):  
        dx = float(input("Inserisci il valore dell'asse x: "))
        dy = float(input("Inserisci il valore dell'asse y: "))
        zona.x += dx
        zona.y += dy

    def distanza_da_origine(zona):
        dx = zona.x
        dy = zona.x
        return dx,dy 
    

p = Punto()
p.muovi()
dx, dy = p.distanza_da_origine()

print("lo spostamento sull'asse x:",dx)
print("lo spostamento sull'asse y:",dy)