import sqlite3


class ConnectionDB:
    def __init__(self):
        self.connection = sqlite3.connect('src/database/peliculas.db')
        self.cursor = self.connection.cursor()

    def closeDB(self):
        self.connection.close()
