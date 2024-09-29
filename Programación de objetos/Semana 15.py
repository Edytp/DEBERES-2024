import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada
        self.tarea_input = tk.Entry(root, width=40)
        self.tarea_input.pack(pady=10)
        self.tarea_input.bind('<Return>', self.agregar_tarea)

        # Botón para añadir tarea
        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        # Botón para marcar como completada
        self.boton_completada = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completada.pack(pady=5)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Listbox para mostrar tareas
        self.lista_tareas = Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10)

        # Scrollbar
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_tareas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista_tareas.yview)

    def agregar_tarea(self, event=None):
        tarea = self.tarea_input.get()
        if tarea:
            self.lista_tareas.insert(END, tarea)
            self.tarea_input.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def marcar_completada(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(seleccion)
            self.lista_tareas.delete(seleccion)
            self.lista_tareas.insert(END, f"✔ {tarea}")  # Añade un símbolo de completada
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(seleccion)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
