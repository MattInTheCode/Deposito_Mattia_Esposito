controllore = True 

while controllore:
    

    scelta = input("vuoi continuare? (scrivi 'esci' per uscire o si per continuare): ").lower()   
    
     
    if scelta == "esci":
        
        controllore = False
        print("Uscita dal programma...")
    
    elif scelta == "si":
        
        menu_attivo = True 
        
        while controllore:
            print("Benvenuto nel menù. Scegli un numero di una delle opzioni")
            print("tranello 1.")
            print("somma numeri pari 2.")
            print("ciclo for 3.")
            print("Verifica numero primo 4.")
            
        
            scelta_menu = input("Scegli un'opzione: ")
            
        
        #punto 1 
            if scelta_menu == "1":
                print("hai scelto il tranello! ")
                
                while True:
                       

                        if int(numero_input) > 0:
                            numero = int(numero_input)
                            print("Il numero scelto è:" + str(numero) + ".")
                            break
                        
                        else:
                            print("Errore: Il numero che devi inserire è un intero positivo")
        
        
        
         #punto 2 somma numeri pari   
        
            elif scelta_menu == "2":
                print("Hai scelto la somma dei numeri pari...")
                
                numero_input = int(input("Inserisci un numero intero positivo: "))
                
                
                somma = 0 
                
                for i in range(numero_input +1): 
                    
                    
                    if i %2 == 0:
                        
                        somma += i
                
                print("La somma dei numeri pari fino a", numero_input, "è:", somma) 
                
                break      
            
            
        #punto 3 ciclo for
        
            elif scelta_menu == "3":  
                numero_input = int(input("Inserisci un numero intero positivo: "))
                
                while numero_input <= 0:  
                    print("Errore: Il numero che devi inserire è un intero positivo")
                    numero_input = int(input("Inserisci un numero intero positivo: "))
                
                print("Hai scelto di stampare i numeri dispari...")
                
                # Ciclo per stampare i numeri dispari da 1 a numero_input
                
                for i in range(1, numero_input + 1):
                    if i % 2 != 0:  
                        print(i, end=" ")
                print()  
                
                print("Uscendo dal programma...")
                controllore = False  
                
                
            #punto 4 verifica numero primo
                
            elif scelta_menu == "4":
                print("Hai scelto di determinatore numero primo:")
            
                numero_input = int(input("Inserisci un numero intero positivo: "))
                
                while numero_input <= 0:  
                    print("Errore: Il numero che devi inserire è un intero positivo")
                    numero_input = int(input("Inserisci un numero intero positivo: "))
                    
                print("verifichiamo se il numero è primo:")
                
                if numero_input <= 1:
                    print("", numero_input, "non è un numero primo")
                else:
                    
                    è_primo = True
                    
                    for i in range(2, numero_input):
                        if numero_input %i == 0:
                            è_primo = False
                            controllore = False
                            break
                            

                    if è_primo:
                        print(numero_input, "è un numero primo")
                    else:
                        print(numero_input, "non è un numero primo")
                        
                    
                
                   
            else:
                print("Errore, inserire scelta valida.")
                