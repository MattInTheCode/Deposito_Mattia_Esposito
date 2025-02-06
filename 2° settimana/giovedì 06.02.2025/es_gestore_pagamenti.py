#classe genitrice metodo di pagamento
class MetodoPagamento:
    def __init__(self):
        self._transazioni = []  

    def _aggiungi_transazione(self, importo):
        self._transazioni.append(importo)

    def get_transazioni(self):
        return self._transazioni

    # l'ho utilizzato come sorta di "placeholder"
    def effettua_pagamento(self, importo):
        pass

#sottoclasse di pagamento carta
class CartaDiCredito(MetodoPagamento):
    #sovrascriviamo effettua_pagamento
    def effettua_pagamento(self, importo):
        self._aggiungi_transazione(importo)
        return str(importo)+"€ con carta di credito andato a buon fine."

#metodo paypal
class PayPal(MetodoPagamento):
    #sovrascriviamo effettua_pagamento
    def effettua_pagamento(self, importo):
        self._aggiungi_transazione(importo)
        return str(importo)+"€ con PayPal andato a buon fine."

#metodo bonifico
class BonificoBancario(MetodoPagamento):
    #sovrascriviamo effettua_pagamento
    def effettua_pagamento(self, importo):
        self._aggiungi_transazione(importo)
        return "Il bonifico di" +str(importo)+ "€ è andato a buon fine."

#classe che Inizializza l'oggetto GestorePagamenti con un'istanza di un metodo di pagamento
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self._metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        return self._metodo_pagamento.effettua_pagamento(importo)

    def storico_transazioni(self):
        return self._metodo_pagamento.get_transazioni()

    def set_metodo_pagamento(self, metodo_pagamento: MetodoPagamento):
        self._metodo_pagamento = metodo_pagamento

    def get_metodo_pagamento(self):
        return self._metodo_pagamento


class GestoreMenu:
    def __init__(self):
        self._metodi = {
            "1": CartaDiCredito(),
            "2": PayPal(),
            "3": BonificoBancario()
        }
        self._gestore_pagamenti = None

    def mostra_menu(self):
        while True:
            print("Seleziona il metodo di pagamento:")
            print("1 - Carta di Credito")
            print("2 - PayPal")
            print("3 - Bonifico Bancario")
            print("4 - Esci")
            scelta = input("Scelta: ")

            if scelta == "4":
                print("Uscita dal sistema di pagamento.")
                break

            if scelta not in self._metodi:
                print("Scelta non valida. Riprova.")
                continue

            importo = float(input("Inserisci l'importo: "))
            self._gestore_pagamenti = GestorePagamenti(self._metodi[scelta])
            print(self._gestore_pagamenti.paga(importo))
            print("Storico transazioni:", self._gestore_pagamenti.storico_transazioni())

# facciamo partire il tutto 
gestore_menu = GestoreMenu()
gestore_menu.mostra_menu()
