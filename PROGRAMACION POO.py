# Definición de la clase ClimaSemanal
class ClimaSemanal:
    def __init__(self):
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = []

    def ingresar_temperatura(self, dia):
        temperatura = float(input(f"Ingrese la temperatura de {dia}: "))
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0.0  # Si no hay temperaturas ingresadas, el promedio es 0.0

        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio


def main():
    print("Bienvenido al programa para calcular el promedio semanal de temperaturas.")

    # Crear objeto de la clase ClimaSemanal
    clima = ClimaSemanal()

    # Iterar sobre los días de la semana y pedir al usuario que ingrese la temperatura
    for dia in clima.dias_semana:
        clima.ingresar_temperatura(dia)

    # Calcular promedio semanal
    promedio_semanal = clima.calcular_promedio_semanal()

    # Mostrar resultado
    print(f"\nEl promedio semanal de temperaturas es: {promedio_semanal:.2f} grados Celsius.")


if __name__ == "__main__":
    main()