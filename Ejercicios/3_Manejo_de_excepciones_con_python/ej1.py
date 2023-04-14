try:
    while True:
        n1 = int(input("Ingresa el primer numero:\n>>> "))
        n2 = int(input("Ingresa el segundo numero:\n>>> "))

        print(n1+n2)


        opcion = input("Deseas agregar mas numeros? Y/N")
        
        if(opcion == "y" or opcion == "Y"):
            pass
        elif(opcion == "n" or opcion == "N"):
            print("Hasta Luego!")
            break
        else:
            print("Opcion Incorrecta")
            break


except ValueError:
    print("Error")