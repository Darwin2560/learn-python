import tkinter as tk
from tkinter import ttk

from models.pelicula import create_table, delete_table, Movie, guardar, get_movies, update, delete


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro', command=create_table)
    menu_inicio.add_command(label='Eliminar Registro', command=delete_table)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_movie = None
        self.config(width=480, height=320)
        self.campos_peliculas()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    def campos_peliculas(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Género: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Entry de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        self.boton_agregar = tk.Button(self, text='Agregar', command=self.habilitar_campos)
        self.boton_agregar.config(width=20, font=('Arial', 12, 'bold'), bg='blue', fg='white', cursor='hand2', activebackground='#5dade2', activeforeground='white')
        self.boton_agregar.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_pelicula)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), bg='green', fg='white', cursor='hand2', activebackground='#27ae60', activeforeground='white')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), bg='red', fg='white', cursor='hand2', activebackground='#e74c3c', activeforeground='white')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_movie = None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_pelicula(self):
        self.movie = Movie(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()
        )
        if self.id_movie == None:
            guardar(self.movie)
        else:
            update(self.movie, self.id_movie)
        self.tabla_peliculas()
        self.deshabilitar_campos()
        self.id_movie = None

    def tabla_peliculas(self):
        # Llenar la tabla con los datos de la base de datos
        self.movies = get_movies()
        self.movies.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        # scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scrollbar.grid(row=4, column=4, sticky='nse')
        self.tabla.config(yscrollcommand=self.scrollbar.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACIÓN')
        self.tabla.heading('#3', text='GÉNERO')

        for movie in self.movies:
            self.tabla.insert('', 0, text=movie[0], 
                            values=(movie[1], movie[2], movie[3]))
        
        # Botones de la tabla
        self.boton_editar = tk.Button(self, text='Editar', command = self.editar_pelicula)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), bg='yellow', fg='black', cursor='hand2', activebackground='#ffeb3b', activeforeground='black')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text='Eliminar', command = self.eliminar_pelicula)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), bg='red', fg='white', cursor='hand2', activebackground='#ef5350', activeforeground='white')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_pelicula(self):
        try:
            self.id_movie = self.tabla.item(self.tabla.selection())['text']
            self.name_movie = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duration_movie = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.gender_movie = self.tabla.item(
                self.tabla.selection())['values'][2]

            self.habilitar_campos()
            self.entry_nombre.insert(0, self.name_movie)
            self.entry_duracion.insert(0, self.duration_movie)
            self.entry_genero.insert(0, self.gender_movie)
        except:
            titulo = 'Actualización de Película'
            mensaje = 'Debe seleccionar una película para editar.'
            tk.messagebox.showwarning(titulo, mensaje)

    def eliminar_pelicula(self):
        try:
            self.id_movie = self.tabla.item(self.tabla.selection())['text']
            titulo = 'Eliminar Película'
            mensaje = '¿Está seguro de eliminar la película?'
            if tk.messagebox.askyesno(titulo, mensaje):
                delete(self.id_movie)
            self.tabla_peliculas()
            self.id_movie = None
        except:
            titulo = 'Eliminar Película'
            mensaje = 'Debe seleccionar una película para eliminar.'
            tk.messagebox.showwarning(titulo, mensaje)