#
#Autor: Ricardo Reyna Martinez IDGS803

texto="Universidad tecnologica de León"

print(type(texto))
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("de"))
print(texto.count("a"))

texto2=texto.replace("e","3")
print(texto2)
texto3=texto.split(" ")
print(texto3)
print(texto.capitalize())