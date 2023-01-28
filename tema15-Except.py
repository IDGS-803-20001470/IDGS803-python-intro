num1=2
num2=0




#Try Catch por si hay exceptciones en el programa
try:
    x=num1/num2
    print("La division es",x)
   
except:
    print("Error en el Programa de try")

finally: #Siempre se ejecuta, no importa si colapsa el programa o no
    print("Programa de try")



    