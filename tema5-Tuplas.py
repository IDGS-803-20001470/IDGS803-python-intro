#Autor: Ricardo Reyna Martinez IDGS803
#Las tuplas se definen mediante un parentesis, a diferencia de un array con corchetes[]

tupla=(1,2,3,4)
print(type(tupla))
print(tupla)

tupla2=(7,"rICARDO",True,23.9,12+3j)
print(tupla2)

tupla3=tupla+tupla2
print(tupla3)

print(tupla2[1])
print(tupla2[:])
print(tupla2[1:3])
print(tupla2[:4])
print(tupla2[0:])
print(tupla2[-1])
print(tupla2[-2])

a,b,c=tupla


