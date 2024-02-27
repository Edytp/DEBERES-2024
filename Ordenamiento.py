print("Hello world")
print("UEA")
print('BIENVENIDOS')
nombre = input("APELLIDO Y NOMBRE:")

matriz = [
    [9, 2, 5],
    [4, 7, 1],
    [6, 3, 8]
]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def ordenar_fila(matriz, fila):
    if fila >= 0 and fila < len(matriz):
        bubble_sort(matriz[fila])
        return True
    else:
        return False


print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = int(input('Fila a ordenar:'))
if ordenar_fila(matriz, fila_a_ordenar):
    print("\nLa fila", fila_a_ordenar, "se ha ordenado correctamente.")
else:
    print("\nLa fila", fila_a_ordenar, "no se pudo ordenar porque está fuera de rango.")

print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)

