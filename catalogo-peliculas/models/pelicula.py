from tkinter import messagebox

from .connection_db import ConnectionDB


def create_table():
    connect = ConnectionDB()
    sql = """
    CREATE TABLE movies (
        id_movie INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        duration VARCHAR(10),
        gender VARCHAR(100)
    )
    """
    try:
        print(sql)  # Imprime la consulta para depuración
        connect.cursor.execute(sql)
        connect.closeDB()
        titulo = "Crear Registro"
        mensaje = "La tabla de películas ha sido creada correctamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "Error al crear la tabla de películas"
        messagebox.showwarning(titulo, mensaje)


def delete_table():
    connect = ConnectionDB()
    try:
        sql = "DROP TABLE movies"
        connect.cursor.execute(sql)
        connect.closeDB()
        titulo = "Eliminar Registro"
        mensaje = "La tabla de películas ha sido eliminada correctamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar Registro"
        mensaje = "Error al eliminar la tabla de películas"
        messagebox.showwarning(titulo, mensaje)


class Movie:
    def __init__(self, name, duration, gender):
        self.id_movie = None
        self.name = name
        self.duration = duration
        self.gender = gender

    def __str__(self):
        return f"Pelicula[{self.name}, {self.duration}, {self.gender}]"


def guardar(movie):
    try:
        connection = ConnectionDB()
        sql = """
            INSERT INTO movies (name, duration, gender)
            VALUES (?,?,?)
        """
        values = (movie.name, movie.duration, movie.gender)
        connection.cursor.execute(sql, values)
        connection.closeDB()
    except:
        titulo = "Guardar Película"
        mensaje = "Error al guardar la película"
        messagebox.showerror(titulo, mensaje)


def get_movies():
    connection = ConnectionDB()
    sql = "SELECT * FROM movies"
    try:
        connection.cursor.execute(sql)
        movies = connection.cursor.fetchall()
        connection.closeDB()
    except:
        titulo = "Obtener Películas"
        mensaje = "Error al obtener las películas"
        messagebox.showerror(titulo, mensaje)
    return movies


def update(movies, id_movie):
    connection = ConnectionDB()
    sql = f"""
        UPDATE movies
        SET name='{movies.name}', duration='{movies.duration}', gender='{movies.gender}'
        WHERE id_movie={id_movie}
    """

    try:
        connection.cursor.execute(sql)
        connection.closeDB()
    except:
        titulo = "Actualizar Película"
        mensaje = "Error al actualizar la película"
        messagebox.showerror(titulo, mensaje)


def delete(id_movie):
    connection = ConnectionDB()
    sql = f"DELETE FROM movies WHERE id_movie={id_movie}"

    try:
        connection.cursor.execute(sql)
        connection.closeDB()
    except:
        titulo = "Eliminar Película"
        mensaje = "Error al eliminar la película"
        messagebox.showerror(titulo, mensaje)
