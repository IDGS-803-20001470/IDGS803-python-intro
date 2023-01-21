

num1=int(input("Dame el primer numero: "))

#Tabla de multiplicar
def multiplicar(num):
    cont=1
    while cont<11:
     print(num," * ",cont,"=", num*cont)
     #print("{1} * {2} = {2} ".format(num1,cont,(num1*cont)))
     cont=cont+1 



multiplicar(num1)

