

def suma():
    x=int(input("Ingrese el primer numero "))
    y=int(input("Ingrese el segundo numero "))
    print("La suma es",x+y)
    menu()
    return True

def resta():
    x=int(input("Ingrese el primer numero "))
    y=int(input("Ingrese el segundo numero "))
    print("La resta es",x-y)
    menu()
    return True

def Multiplicacion():
    x=int(input("Ingrese el primer numero "))
    y=int(input("Ingrese el segundo numero "))
    print("La suma es",x*y)
    menu()
    return True

def Division():
    x=int(input("Ingrese el primer numero "))
    y=int(input("Ingrese el segundo numero "))
    print("La Division es",x/y)
    menu()
    return True

def despedida():
    print("Adios vuelve pronto")
    return True 

def menu():
        opcion=int(input("Elija la opcion 1-Suma 2-Resta 3-Multiplicacion 4-Division 5-Salir "))
        #while opcion<5:
        if opcion==1:
                suma()
        elif opcion==2:
                resta()
        elif opcion==3:
                Multiplicacion()
        elif opcion==4:
                Division()
        elif opcion==5:
                despedida()
        elif opcion>5 or opcion<1:
            print("Introduce una opcion correcta")
            menu()


def main():
    menu()



if __name__=="__main__":
    main()