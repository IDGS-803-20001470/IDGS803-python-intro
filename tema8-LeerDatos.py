#

print("Bienvenido al programa de lectura de datos")
#Operaciones con en enteros
num1=int(input("Dame el primer numero: "))
num2=int(input("Dame el segundo numero: "))

print("La suma de los numeros de {0} + {1} = {2} ".format(num1,num2,(num1+num2)))

#Operacion con float (numeros con punto decimal)
num3=float(input("Dame el primer numero Decimal: "))
num4=float(input("Dame el segundo numero Decimal: "))
print("La suma de los numeros de {0} + {1} = {2} ".format(num3,num4,(num3+num4)))

#
dato=100
print(len(str(dato))) #Convierte el dato a cadena y calcula la longitud

dato2="2005"
print(int(dato2)) #Convierte el dato a entero y calcula la longitud

dato3="20.05"
print(float(dato3)) #Convierte el dato a flotante y calcula la longitud