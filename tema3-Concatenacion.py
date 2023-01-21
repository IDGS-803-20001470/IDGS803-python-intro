#Concatenar cadenas de caracteres
#Autor: Ricardo Reyna Martinez IDGS803

dato1="Hola"
dato2="Mundo"

datoFinal=dato1+" "+dato2
print(datoFinal)

#Imprimir al concatenar
print("El saludo es: %s %s" %(dato1,dato2))

saludo="Saludo2 {0} {1} ".format(dato1,dato2)
print(saludo)

saludo3="Saludo3 {1} {0} ".format(dato1,dato2)
print(saludo3)

saludo4="Saludo4 {a} {b} ".format(a=dato1,b=dato2)
print(saludo4)