class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Usamos una tupla para autor y título como se especifica
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, categoria={self.categoria}, isbn={self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, id_usuario={self.id_usuario}, libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros con ISBN como clave
        self.usuarios = set()  # Conjunto para manejar IDs de usuarios únicos

    def añadir_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca por su ISBN."""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.id_usuario in {u.id_usuario for u in self.usuarios}:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        """Elimina un usuario de la biblioteca."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado de la biblioteca.")
        else:
            print(f"El usuario con ID {id_usuario} no se encuentra en la biblioteca.")

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro a un usuario."""
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro in usuario.libros_prestados:
                print(f"El usuario con ID {id_usuario} ya tiene prestado el libro {libro}.")
            else:
                usuario.libros_prestados.append(libro)
                print(f"Libro {libro} prestado al usuario {usuario}.")
        else:
            if not libro:
                print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")
            if not usuario:
                print(f"El usuario con ID {id_usuario} no está registrado en la biblioteca.")

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro prestado por un usuario."""
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro {libro} devuelto por el usuario {usuario}.")
            else:
                print(f"El usuario con ID {id_usuario} no tiene prestado el libro {libro}.")
        else:
            if not libro:
                print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")
            if not usuario:
                print(f"El usuario con ID {id_usuario} no está registrado en la biblioteca.")

    def buscar_libros(self, **kwargs):
        """Busca libros en la biblioteca por título, autor o categoría."""
        resultado = []
        for libro in self.libros.values():
            if all(getattr(libro, k) == v for k, v in kwargs.items()):
                resultado.append(libro)
        return resultado

    def listar_libros_prestados(self, id_usuario):
        """Lista todos los libros actualmente prestados a un usuario."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            print(f"Libros prestados al usuario {usuario.nombre}: {usuario.libros_prestados}")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado en la biblioteca.")


# Ejemplo de uso

# Crear una biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", ("George Orwell",), "Ficción", "9780451524935")
libro2 = Libro("Cien años de soledad", ("Gabriel García Márquez",), "Realismo mágico", "9780060883287")

# Crear usuarios
usuario1 = Usuario("Ana Pérez", "123")
usuario2 = Usuario("Juan Gómez", "456")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Prestar libros
biblioteca.prestar_libro("9780451524935", "123")

# Listar libros prestados
biblioteca.listar_libros_prestados("123")

# Buscar libros por título
print(biblioteca.buscar_libros(titulo="1984"))

# Devolver libros
biblioteca.devolver_libro("9780451524935", "123")

# Listar libros prestados después de la devolución
biblioteca.listar_libros_prestados("123")
