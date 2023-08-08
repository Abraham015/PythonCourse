nombres=["Juan", "Karla", "Ricardo","María"] #Así es como definimos las listas
#Imprimir la lista de nombres
print(nombres)
#Para acceder a los elementos de manera individual se hace como
print(nombres[0])
#Podemos acceder a los elementos de la lista de manera inversa
print(nombres[-1])
#Para acceder a un rango, se puede colocar como 0:2 o :2
print(nombres[:2])
print(nombres[1:])

#Para iterar una lista se hace de la siguiente manera
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")

#Para saber el largo de la lista es
print(len(nombres))

#Para anexar un nuevo elemento se utilizará append
nombres.append("Lorenzo")
print(nombres)
#Para insertar un elemento en un índice
nombres.insert(1, "Octavio")
print(nombres)

#Para quitar un elemento de la lista
nombres.remove("Octavio")
print(nombres)

#Para remnover el ultimo elemento
nombres.pop()
print(nombres)

#Para eliminar un indice
del nombres[0]
print(nombres)

#Para limpiar la lista
nombres.clear()
print(nombres)

#Para eliminar la lista por completo
del nombres
#print(nombres)
