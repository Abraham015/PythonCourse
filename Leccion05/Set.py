#Un set no permite elementos duplicados
#Para definir un set se hace lo siguiente
planetas={"Marte", "Jupiter", "Venus"}
print(planetas)

#Para conocer el largo de los elementos
print(len(planetas))

#Para verificar si un elemento esta presente
print("Marte" in planetas)

#Para agregar más elementos
planetas.add("Tierra")
print(planetas)

#No soporta elementos duplicados

#Para eliminar un elemento
planetas.remove("Tierra")
print(planetas)

#Se puede utilizar la palabra discard, pero no marca error
#Si no se encuentra en el set
planetas.discard("Jupiter")
print(planetas)

#Para limpiar el set se usa
planetas.clear()
print(planetas)

#Si queremos eliminar el set
del planetas