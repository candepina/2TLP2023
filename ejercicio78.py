padres = []
hijos = []

for i in range(3):
    pa = input("Ingrese nombre del padre: ")
    ma = input("Ingrese nombre de la madre: ")
    padres.append([pa, ma])

for i in range(3):
    cant = int(input("Ingrese cantidad de hijos para la familia " + str(i + 1) + ": "))
    hijos_familia = []
    for j in range(cant):
        nom = input("Ingrese el nombre del hijo: ")
        hijos_familia.append(nom)
    hijos.append(hijos_familia)

print("Listado de padres, madres e hijos:")

for i in range(3):
    print("Familia " + str(i + 1) + ":")
    print("Padre: " + padres[i][0])
    print("Madre: " + padres[i][1])
    print("Hijos:")
    for hijo in hijos[i]:
        print(hijo)

print("Listado de padres y cantidad de hijos que tienen:")

for i in range(3):
    print("Padre: " + padres[i][0])
    print("Cantidad de hijos: " + str(len(hijos[i])))
