class OperacionesBasicas:
    num1=0
    num2=0
    res=0

    def suma(self):
       
        #print("La suma es",self.num1+self.num2)
        self.res=self.num1+self.num2
        #return True

    def resta(self):
        self.res=self.num1-self.num2

    def Multiplicacion(self):
        self.res=self.num1*self.num2

    def Division(self):
        self.res=self.num1/self.num2

    def despedida():
        print("Adios vuelve pronto")
        return True 


def menu():
        opcion=int(input("Elija la opcion 1-Suma 2-Resta 3-Multiplicacion 4-Division 5-Salir "))
        #while opcion<5:
        if opcion>=5 or opcion<1:
            print("Adios vuelve pronto")
        else:
            x=int(input("Ingrese el primer numero "))
            y=int(input("Ingrese el segundo numero "))
            ob=OperacionesBasicas()
            ob.num1=x
            ob.num2=y
            #OperacionesBasicas.num2=y
            if opcion==1:
                    ob.suma()
                    print("El resultado es",ob.res)
                    menu()
            elif opcion==2:
                    ob.resta()
                    print("El resultado es",ob.res)
                    menu()
            elif opcion==3:
                    ob.Multiplicacion()
                    print("El resultado es",ob.res)
                    menu()
            elif opcion==4:
                    ob.Division()
                    print("El resultado es",ob.res)
                    menu()
            elif opcion==5:
                    ob.despedida()
            elif opcion>5 or opcion<1:
                print("Introduce una opcion correcta")
                menu()


    
    



if __name__=="__main__":
    menu()