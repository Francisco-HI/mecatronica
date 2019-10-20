"""
Nombre: insertar.py
Objetivo: insertar datos en la tabla empleados
Autor: Jose Francisco Garcia Fuentes
Fecha: 03/10/2019
"""
from tkinter import messagebox

class inserto():
    #Constructor: instancia la clase para construir objetos
    def __init__(self, clave, nombre, sueldo):
        self.cla = clave
        self.nom = nombre
        self.suel = sueldo

        # Importamos la libreria mysql
        import pymysql

        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos crud
        db = pymysql.connect("localhost","root","","trabajadores")
        ##################################################

        # prepare a cursor object using cursor() method
        cursor = db.cursor()


        # cadena sql de insercion
        sqlcad = "INSERT INTO empleados(clave, nombre, sueldo) VALUES (" + str(self.cla) + ",'" + self.nom + "'," + str(self.suel) + ");"

        # ejecuta el SQL query usando el metodo execute().
        cursor.execute(sqlcad)

        # Commit your changes in the database  (Es para confirmar los cambios)
        db.commit()

        # procesa una unica linea usando el metodo fetchone().

        # desconecta del servidor
        db.close()

        messagebox.showinfo(message="Registro guardado", title="Atencion")
