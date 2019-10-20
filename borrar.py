"""
Nombre: borrar.py
Objetivo: borrar datos en la tabla empleadod
Autor: Jose Francisco Garcia Fuentes
Fecha: 20/10/2019
"""
from tkinter import messagebox

class borrando():
    #Constructor: instancia la clase para construir objetos
    def __init__(self, clave1):
        self.cla1 = clave1

        # Importamos la libreria mysql
        import pymysql

        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos crud
        db = pymysql.connect("localhost","root","","trabajadores")
        ##################################################

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # cadena sql de insercion
        sqlcad = "DELETE FROM empleados WHERE `clave`=" + str(self.cla1)  

        # ejecuta el SQL query usando el metodo execute().
        cursor.execute(sqlcad)

        # Commit your changes in the database
        db.commit()

        # procesa una unica linea usando el metodo fetchone().

        print ("Operación realizada...")

        # desconecta del servidor
        db.close()

        messagebox.showinfo(message="Registro ELIMINADO!", title="Atencion")