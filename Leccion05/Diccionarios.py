#Para definir un diccionario
diccionario={
    "IDE":"Integrated Development Enviroment",
    "OOP": "Oriented Objected Programming",
    "DBMS": "Database Managment System"
}

print(diccionario)

#Para conocer el largo del diccionario
print(len(diccionario))

#Para acceder a los elementos del diccionario
print(diccionario["IDE"])
print(diccionario.get("OOP"))

#Para modificar un elemento
diccionario["IDE"]="integrated development enviroment"
print(diccionario)

#Para recorrer los elementos de un diccionario
for d, valor in diccionario.items():
    print(d, valor)

for termino in diccionario.keys(): #Accede a la llave
    print(termino)

for valor in diccionario.values(): #Accede a los valores asociadcos
    print(valor)

#comprobar existencia de algun elemento
print("IDE" in diccionario)

#Para agregar un elemento
diccionario["PK"]="Primary Key"
print(diccionario)

#Para eliminar un elemento
diccionario.pop("DBMS")
print(diccionario)

#Para limpiar el diccionario
diccionario.clear()
print(diccionario)

#Para eliminar el diccionario
del diccionario