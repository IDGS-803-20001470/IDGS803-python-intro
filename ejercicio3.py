
import claseOperacionesBasicas as op


def menu():
        opcion=int(input("Elija la opcion 1-Suma 2-Resta 3-Multiplicacion 4-Division 5-Salir "))
        #while opcion<5:
        if opcion==1:
                op.suma()
                menu()
        elif opcion==2:
                op.resta()
                menu()
        elif opcion==3:
                op.Multiplicacion()
                menu()
        elif opcion==4:
                op.Division()
                menu()
        elif opcion==5:
                op.despedida()
        elif opcion>5 or opcion<1:
            print("Introduce una opcion correcta")
            menu()


def main():
    menu()



if __name__=="__main__":
    main()