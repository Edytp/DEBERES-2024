import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Aplicación de Gestión de Datos")
        self.root.geometry("400x300")

        # Etiquetas
        self.etiqueta_entrada = tk.Label(root, text="Ingrese información:")
        self.etiqueta_entrada.pack(pady=10)

        # Campo de texto
        self.campo_texto = tk.Entry(root, width=40)
        self.campo_texto.pack(pady=5)

        # Botón "Agregar"
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack(pady=5)

        # Lista para mostrar los datos
        self.lista_datos = tk.Listbox(root, width=50, height=10)
        self.lista_datos.pack(pady=10)

        # Configuración para almacenar datos
        self.datos = []

    def agregar_dato(self):
        """Añade la información del campo de texto a la lista."""
        dato = self.campo_texto.get()
        if dato:
            self.datos.append(dato)
            self.lista_datos.insert(tk.END, dato)
            self.campo_texto.delete(0, tk.END)  # Limpiar campo de texto después de agregar
        else:
            tk.messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

    def limpiar_datos(self):
        """Limpia la lista y el campo de texto."""
        self.lista_datos.delete(0, tk.END)
        self.campo_texto.delete(0, tk.END)
        self.datos.clear()

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
