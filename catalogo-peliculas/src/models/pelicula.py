from tkinter import messagebox
from .connection_db import ConnectionDB

def create_table():
    connect = ConnectionDB()
    sql = '''
    CREATE TABLE IF NOT EXISTS movies (
        id_movie INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        duration VARCHAR(10),
        gender VARCHAR(100)
    )
    '''
    try:
        print(sql)  # Imprime la consulta para depuración
        connect.cursor.execute(sql)
        connect.connection.commit()  # Asegúrate de hacer commit después de ejecutar
        connect.closeDB()
        titulo = 'Crear Registro'
        mensaje = 'La tabla de películas ha sido creada correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'Error al crear la tabla de películas'
        messagebox.showwarning(titulo, mensaje)

def delete_table():
    connect = ConnectionDB()
    try:
        sql = 'DROP TABLE IF EXISTS movies'
        connect.cursor.execute(sql)
        connect.connection.commit()  # Asegúrate de hacer commit después de ejecutar
        connect.closeDB()
        titulo = 'Eliminar Registro'
        mensaje = 'La tabla de películas ha sido eliminada correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Eliminar Registro'
        mensaje = 'Error al eliminar la tabla de películas'
        messagebox.showwarning(titulo, mensaje)
