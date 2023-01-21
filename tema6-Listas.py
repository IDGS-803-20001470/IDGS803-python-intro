#Autor: 
lista1=[1,2,3,4,5]

lista2=[1,3,5,"Ricardo",True,2.3]

print(lista1[-1])
print(lista1[:2])
print(lista1[1:3])
print(lista1[3:])
print("Lista 2",lista2)

lista2.append("Jessica")
print("Lista 2 Actualizada",lista2)

lista2.insert(3,"Valencia")
print("Lista 2 Actualizada 2.0",lista2)

lista2.remove("Valencia")
print("Lista 2 Actualizada 3.0",lista2)

lista2.pop()
print("Lista 2 Actualizada 4.0",lista2)

#Elimina algo en concreto
del lista2[2]
print("Lista 2 Actualizada 5.0",lista2)