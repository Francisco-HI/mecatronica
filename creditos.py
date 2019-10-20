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
raiz.title("CREDITOS")

desplegable(raiz)



#-------------------my code----------------------------------
 #----------------Botones y vampos---------------------------


miFrame=Frame(raiz, height=600, width=800, padx=40, pady=15)
miFrame.config( bg = '#FCF5E2')
miFrame.pack()


labelClave=Label(miFrame, text="Creditos:", font=("Helvetica", 16))
labelClave.grid(row=0, column=0, padx=10, pady=10)
labelClave.config( bg = '#FCF5E2')


bienvenido='Elaboró: José Francisco García Fuentes  \
            \nAsesor: Jesús Alberto Verduzco Ramírez '

texto=Text(miFrame, width=35, height=5, padx=5, pady=10, font=("Helvetica", 16))
texto.grid(row=1, column=0)
texto.insert(INSERT, bienvenido)

scrollvert=Scrollbar(miFrame, command=texto.yview,)
scrollvert.grid(row=1, column=1, sticky="nsew")
texto.config(yscrollcommand=scrollvert.set)





#Mostramos ventana
raiz.mainloop()
