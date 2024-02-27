print("Hello world")
print("UEA")
print('BIENVENIDOS')
nombre = input("APELLIDO Y NOMBRE:")
matriz = [
    [5, 2, 6],
    [3, 1, 4],
    [7, 8, 9]
]

valor_buscado = int(input('Valor a buscar:'))
fila_encontrada = -1
columna_enontrada = -1

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_enontrada = columna
            break
    if fila_encontrada != -1:
        break

if fila_encontrada != -1:
    print(f'Se encontró {valor_buscado} en la fila {fila_encontrada} y la Columna {columna_enontrada}')
else:
    print(f'{valor_buscado} no se encontro en la matriz')
