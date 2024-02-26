print("BIENVENIDO A LA UEA")
print("ESCUELA DE TECNOLOGIAS DE LA INFORMACIÓN")
nombre = input ("APELLIDO Y NOMBRE:")
print("Funcion buscar")
matriz = [
    [12,13,14],
    [5,6,8],
    [10, 11,1]
]
no_fila = 0

busqueda = int(input('Valor a buscar:'))

for fila in matriz:
    no_columna = 0
    for columna in fila:
        if (columna == busqueda):
            print(f'No. {busqueda}, su posicion es:[{no_fila}] [{no_columna}] ')

        no_columna += 1
    no_fila += 1
