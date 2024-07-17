class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')  # Abre el archivo en modo escritura al crear la instancia
        print(f"Archivo '{self.filename}' abierto.")

    def write(self, text):
        self.file.write(text)

    def __del__(self):
        if hasattr(self, 'file') and self.file:
            self.file.close()  # Cierra el archivo al destruir la instancia
            print(f"Archivo '{self.filename}' cerrado.")
        else:
            print("No se pudo cerrar el archivo porque no estaba abierto.")