class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre        # atributo público
        self.__edad = edad          # atributo privado

    def hacer_sonido(self):
        pass  # Este método será sobrescrito en las clases derivadas

    def __str__(self):
        return f"{self.nombre} ({self.__class__.__name__}): Edad {self.__edad}"
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza  # atributo público

    def hacer_sonido(self):
        return "Guau!"

    def __str__(self):
        return f"{super().__str__()}, Raza: {self.raza}"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color  # atributo público

    def hacer_sonido(self):
        return "Miau!"

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}"


class Ave(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie  # atributo público

    def hacer_sonido(self):
        return "Pío pío!"

    def __str__(self):
        return f"{super().__str__()}, Especie: {self.especie}"

def main():
    perro = Perro("Firulais", 5, "Labrador")
    gato = Gato("Pelusa", 3, "Blanco y negro")
    ave = Ave("Piolín", 1, "Canario")

    print(perro.hacer_sonido())  # Output: Guau!
    print(gato.hacer_sonido())   # Output: Miau!
    print(ave.hacer_sonido())    # Output: Pío pío!

    # Mostramos la información detallada de los animales
    print(perro)
    print(gato)
    print(ave)

if __name__ == "__main__":
    main()