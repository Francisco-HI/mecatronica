"""
Nombre: buscar.py
Objetivo: Buscar datos datos en la tabla empleadod
Autor: Jose Francisco Garcia Fuentes
Fecha: 20/10/2019
"""
from tkinter import messagebox

class buscando():
    #Constructor: instancia la clase para construir objetos
    def __init__(self, clave1):
        self.cla1 = clave1
        self.cla = 0
        self.nom =""
        self.suel = 0

                
        # Importamos la libreria mysql
        import pymysql

        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos crud
        db = pymysql.connect("localhost","root","","trabajadores")
        ##################################################

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # cadena sql de insercion
        sqlcad = "SELECT * FROM `empleados` WHERE `clave`=" + str(self.cla1)  

        # ejecuta el SQL query usando el metodo execute().
        cursor.execute(sqlcad)

        # Commit your changes in the database
        db.commit()

        # Almacenar los registros de la variable resultado
        resultado = cursor.fetchall()

        #Imprimir la lista de registros recuperados
        for row in resultado:
            #now print fetched result
            #print(str(row[2]))
            self.cla=row[0]
            self.nom=row[1]
            self.suel=row[2]
            
        # procesa una unica linea usando el metodo fetchone().

        print ("Operación realizada...")

        # desconecta del servidor
        db.close()

