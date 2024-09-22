import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_events = ttk.Frame(self.root)
        self.frame_events.pack(padx=10, pady=10)

        self.treeview = ttk.Treeview(self.frame_events, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.pack()

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(padx=10, pady=10)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones de acción
        self.boton_agregar = ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(pady=5)

        self.boton_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.boton_salir.pack(pady=5)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        self.treeview.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        seleccionado = self.treeview.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?")
        if confirmacion:
            for item in seleccionado:
                self.treeview.delete(item)

    def limpiar_campos(self):
        # Reiniciar el DateEntry a la fecha actual
        self.date_entry.set_date(datetime.now())
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()