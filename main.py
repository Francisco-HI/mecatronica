"""
Nombre: main.py
objetivo: Ventana principal del programa
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
raiz.title("PRINCIPAL")
desplegable(raiz)


#-------------------my code----------------------------------
 #----------------Botones y vampos---------------------------


miFrame=Frame(raiz, height=600, width=800, padx=40, pady=15)
miFrame.config( bg = '#FCF5E2')
miFrame.pack()


labelClave=Label(miFrame, text="Quienes somos:", font=("Helvetica", 16))
labelClave.grid(row=0, column=0, padx=10, pady=10)
labelClave.config( bg = '#FCF5E2')

bienvenido='La comunidad del Instituto Tecnológico de Colima les da la más cordial bienvenida a este sitio Web, donde podrás encontrar información que te puede ser de gran utilidad.  \
            \nNuestro plantel, como integrante del Tecnológico Nacional de México, ha avanzado con paso firme hacia su objetivo de consolidarse como una institución educativa de educación superior que busca brindar a la sociedad mexicana una educación humanista de excelencia, aplicando el “Modelo educativo para el siglo XXI: Formación y desarrollo de competencias profesionales”. \
            \nEl accionar de esta casa de estudios sigue centrado en quienes son nuestra razón de ser: la juventud estudiosa. La sociedad nos encomienda la formación profesional y pertinente de sus jóvenes, y hacia ello enfocamos nuestra labor docente y administrativa, para continuar prevaleciendo como una institución pública de educación superior con valores, conocimientos, compromiso y actitudes de servicio. \
            \nContribuimos así al logro de los objetivos marcados en el Programa Sectorial de Educación, de acuerdo con los lineamientos estipulados por nuestro órgano rector, el Tecnológico Nacional de México.'

texto=Text(miFrame, width=50, height=15, padx=10, pady=10, font=("Helvetica", 16))
texto.grid(row=1, column=0)
texto.insert(INSERT, bienvenido)

scrollvert=Scrollbar(miFrame, command=texto.yview,)
scrollvert.grid(row=1, column=1, sticky="nsew")
texto.config(yscrollcommand=scrollvert.set)





#Mostramos ventana
raiz.mainloop()
