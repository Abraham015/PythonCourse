#Dada la siguiente tupla
#Crear una lista que solo incluya llos numeros menores a 5
tupla=(13,1,8,3,2,5,8)
num=[]
for t in tupla:
    if t<5:
        num.append(t)

print(num)