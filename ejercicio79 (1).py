empleados = []
faltas = []

for k in range(3):
    empleado = input("Ingrese nombre del empleado: ")
    empleados.append(empleado)
    falta = int(input("Ingrese la cantidad de faltas por empleado: "))
    faltas_empleado = []

    for x in range(falta):
        dia = int(input("Ingrese el día de falta: "))
        faltas_empleado.append(dia)

    faltas.append(faltas_empleado)

print("Nombres de empleados y los días que faltaron:")
for y in range(3):
    empleado = empleados[y]
    dias = faltas[y]
    print(empleado, "faltó los días:", ', '.join(map(str, dias))

print("Empleados con más de 10 días faltados:")
for i in range(3):
    empleado = empleados[i]
    dias = faltas[i]
    if len(dias) > 10:
        print(f"{empleado} faltó más de 10 días")

print("Empleados con menos de 3 días faltados:")
for i in range(3):
    empleado = empleados[i]
    dias = faltas[i]
    if len(dias) < 3:
        print(f"{empleado} faltó menos de 3 días")
