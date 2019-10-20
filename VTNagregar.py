"""
Nombre: dashboard.py
objetivo: Construye el menu principal de la aplicacion de base de datos
Autor: Jose Francisco Garcia Fuentes
Fecha: 10 de octubre de 2019
"""

#cramos clase
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#Enlazar otro archivo y extrar una clase
from insertar import inserto
from menusuperior import desplegable
import os


 

raiz=Tk()
raiz.title("AGREGAR")
desplegable(raiz)


#-------------------my code----------------------------------
 #----------------Botones y vampos---------------------------


miFrame=Frame(raiz, height=600, width=800, padx=40, pady=15)
miFrame.config( bg = '#FCF5E2')
miFrame.pack()

miClave=StringVar()
miNombre=StringVar()
miSueldo=StringVar()


labelClave=Label(miFrame, text="Clave:")
labelClave.grid(row=0, column=0, sticky="e", padx=10, pady=10)
labelClave.config( bg = '#FCF5E2')
cuadroClave=Entry(miFrame, textvariable=miClave)
cuadroClave.grid(row=0, column=1, padx=10, pady=10)

labelNombre=Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)
labelNombre.config( bg = '#FCF5E2')
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

labelSueldo=Label(miFrame, text="Sueldo:")
labelSueldo.grid(row=2, column=0, sticky="e", padx=10, pady=10)
labelSueldo.config( bg = '#FCF5E2')
cuadroSueldo=Entry(miFrame, textvariable=miSueldo)
cuadroSueldo.grid(row=2, column=1, padx=10, pady=10)


def btguardar():

    inserto(miClave.get()[:4], miNombre.get()[:50], miSueldo.get()[:11])
    miClave.set("")
    miNombre.set("")
    miSueldo.set("")
    


botonguardar=Button(miFrame, text="GUARDAR", command=btguardar)
botonguardar.grid(row=3, column=1)
botonguardar.config(bg = '#B4EAF1')


#Mostramos ventana
raiz.mainloop()
