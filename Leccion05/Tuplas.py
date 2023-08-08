#En una tupla no se pueden agregar ni eliminar elementos
#Para definir una tupla es
frutas=("Naranja", "Platano", "Guayaba")
print(frutas)

#Para saber el tamaño
print(len(frutas))

#Para acceder a un elemento
print(frutas[0])
#Navegacion inervsa
print(frutas[-1])

#Para acceder un rango 
print(frutas[:1])

for t in frutas:
    print(t, end=" ")

#Para cambiar los valores de una tupla
#frutas[0] = "Pera"
frutaLista=list(frutas) #Convierte la tupla a lista
frutaLista[0]="Pera"
frutas=tuple(frutaLista)
print("\n", frutas)