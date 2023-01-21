
#Tabla de multiplicar
def multiplicar(num):
    cont=1
    while cont<11:
     print(num," * ",cont,"=", num*cont)
     #print("{1} * {2} = {2} ".format(num1,cont,(num1*cont)))
     cont=cont+1 

def saludo():
    print("Hola desde my Program")
    return True

def despedida():
    print("Adios desde my Program")
    return True

def main():
    print("Hola desde main de My program")

    saludo()
    despedida()


if __name__=="__main__":
    main()