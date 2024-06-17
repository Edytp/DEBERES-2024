# Función para ingresar temperaturas diarias
def ingresar_temperaturas_diarias():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Iterar sobre los días de la semana y pedir al usuario que ingrese la temperatura
    for dia in dias_semana:
        temperatura = float(input(f"Ingrese la temperatura de {dia}: "))
        temperaturas.append(temperatura)

    return temperaturas


# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    if len(temperaturas) == 0:
        return 0.0  # Si no hay temperaturas ingresadas, el promedio es 0.0

    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


def main():
    print("Bienvenido al programa para calcular el promedio semanal de temperaturas.")

    # Ingresar temperaturas diarias
    temperaturas = ingresar_temperaturas_diarias()

    # Calcular promedio semanal
    promedio_semanal = calcular_promedio_semanal(temperaturas)

    # Mostrar resultado
    print(f"\nEl promedio semanal de temperaturas es: {promedio_semanal:.2f} grados Celsius.")


if __name__ == "__main__":
    main()