
# Programa para convertir grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    """Función para convertir grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Ingreso de datos por el usuario
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de Celsius a Fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Mostrar resultado
print(f"{temperatura_celsius} grados Celsius son equivalentes a {temperatura_fahrenheit} grados Fahrenheit.")
