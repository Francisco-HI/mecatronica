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
from menusuperior import desplegable
from modificar import modificando
from Buscar import buscando
from borrar import borrando
 

raiz=Tk()
raiz.title("MODIFICAR BUSCAR Y ELIMINAR")
desplegable(raiz)

def AgregarFrm():
    messagebox.showinfo(message="Registro guardado", title="Atencion")

#-------------------my code----------------------------------
 #----------------Botones y vampos---------------------------


miFrame=Frame(raiz, height=600, width=800, padx=40, pady=15)       ##Se crea una nueva ventana dentro de la ventana principal raiz
miFrame.config( bg = '#FCF5E2')
miFrame.pack()                                                       ##En esta ventan tendremos todos los widgets

miClave=StringVar()
miNombre=StringVar()
miSueldo=StringVar()

miClave2=StringVar()
miNombre2=StringVar()
miSueldo2=StringVar()

#############//////////Campos de los datos actuales
labelsms=Label(miFrame, text="Actual")
labelsms.grid(row=0, column=1, padx=10, pady=10)
labelsms.config( bg = '#FCF5E2')

labelClave=Label(miFrame, text="Clave:")
labelClave.grid(row=1, column=0, sticky="e", padx=10, pady=10)
labelClave.config( bg = '#FCF5E2')
cuadroClave=Entry(miFrame, textvariable=miClave)
cuadroClave.grid(row=1, column=1, padx=10, pady=10)
cuadroClave.config(state="readonly")

labelNombre=Label(miFrame, text="Nombre:")
labelNombre.grid(row=2, column=0, sticky="e", padx=10, pady=10)
labelNombre.config( bg = '#FCF5E2')
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=2, column=1, padx=10, pady=10)
cuadroNombre.config(state="readonly")

labelSueldo=Label(miFrame, text="Sueldo:")
labelSueldo.grid(row=3, column=0, sticky="e", padx=10, pady=10)
labelSueldo.config( bg = '#FCF5E2')
cuadroSueldo=Entry(miFrame, textvariable=miSueldo)
cuadroSueldo.grid(row=3, column=1, padx=10, pady=10)
cuadroSueldo.config(state="readonly")


######################Campos de los nuevos datos######################
labelsms2=Label(miFrame, text="Nueva")
labelsms2.grid(row=0, column=3, padx=10, pady=10)
labelsms2.config( bg = '#FCF5E2')

labelClave2=Label(miFrame, text="Clave:")
labelClave2.grid(row=1, column=2, sticky="e", padx=10, pady=10)
labelClave2.config( bg = '#FCF5E2')
cuadroClave2=Entry(miFrame, textvariable=miClave2)
cuadroClave2.grid(row=1, column=3, padx=10, pady=10)
cuadroClave2.config(state="readonly")


labelNombre2=Label(miFrame, text="Nombre:")
labelNombre2.grid(row=2, column=2, sticky="e", padx=10, pady=10)
labelNombre2.config( bg = '#FCF5E2')
cuadroNombre2=Entry(miFrame, textvariable=miNombre2)
cuadroNombre2.grid(row=2, column=3, padx=10, pady=10)
cuadroNombre2.config(state="readonly")


labelSueldo2=Label(miFrame, text="Sueldo:")
labelSueldo2.grid(row=3, column=2, sticky="e", padx=10, pady=10)
labelSueldo2.config( bg = '#FCF5E2')
cuadroSueldo2=Entry(miFrame, textvariable=miSueldo2)
cuadroSueldo2.grid(row=3, column=3, padx=10, pady=10)
cuadroSueldo2.config(state="readonly")

#########################Activar o desactivar los botones y los cuadros de texto#################

def btbuscar():
    regreso=buscando(miClave.get()[:4])      #Asignar una variable para poder regresar los valores
    miClave.set(regreso.cla)
    miNombre.set(regreso.nom)
    miSueldo.set(regreso.suel)
    miClave2.set("")
    miNombre2.set("")
    miSueldo2.set("")


def btcambiar():  
    modificando(miClave.get()[:4], miClave2.get()[:4], miNombre2.get()[:50], miSueldo2.get()[:11])  #Mandar a ejecutar el archivo modificar
    miClave.set(miClave2.get())
    miNombre.set("")
    miSueldo.set("")
    miClave2.set("")
    miNombre2.set("")
    miSueldo2.set("")


def bteliminar():  
    borrando(miClave.get()[:4])      #Ejecutar la clase borrar para eliminar el registro
    miClave.set("")
    miNombre.set("")
    miSueldo.set("")
    miClave2.set("")
    miNombre2.set("")
    miSueldo2.set("")

##-----------------Opciones q ejecuta el radio button cuando las selecciono
def botonRadio(): 
    opc=opcion.get()
    if  opc==1:      
        cuadroClave.config(state=NORMAL)
        cuadroNombre.config(state="readonly")
        cuadroSueldo.config(state="readonly")
        cuadroClave2.config(state="readonly")
        cuadroNombre2.config(state="readonly")
        cuadroSueldo2.config(state="readonly")
        botonbuscar.config(state=NORMAL, bg = "#B4EAF1")
        botoncambiar.config(state=DISABLED, bg = '#E0DFE3')
        botoneliminar.config(state=DISABLED, bg = '#E0DFE3')
        
    elif opc==2:
        cuadroClave.config(state=NORMAL)
        cuadroNombre.config(state=DISABLED)
        cuadroSueldo.config(state=DISABLED)
        cuadroClave2.config(state=NORMAL)
        cuadroNombre2.config(state=NORMAL)
        cuadroSueldo2.config(state=NORMAL)
        botonbuscar.config(state=DISABLED, bg = '#E0DFE3')
        botoncambiar.config(state=NORMAL, bg = "#B4EAF1")
        botoneliminar.config(state=DISABLED, bg = '#E0DFE3')
    elif opc==3: 
        cuadroClave.config(state=NORMAL)
        cuadroNombre.config(state="readonly")
        cuadroSueldo.config(state="readonly")
        cuadroClave2.config(state="readonly")
        cuadroNombre2.config(state="readonly")
        cuadroSueldo2.config(state="readonly")
        botonbuscar.config(state=DISABLED, bg = '#E0DFE3')
        botoncambiar.config(state=DISABLED, bg = '#E0DFE3')
        botoneliminar.config(state=NORMAL, bg = "#B4EAF1")





#######################Botones-------------------------
botonbuscar=Button(miFrame, text="Buscar", command=btbuscar)
botonbuscar.grid(row = 4, column = 2)
botonbuscar.config(state=DISABLED, bg = '#E0DFE3')

botoncambiar=Button(miFrame, text="Cambiar", command=btcambiar)
botoncambiar.grid(row =5, column = 2)
botoncambiar.config(state=DISABLED, bg = '#E0DFE3')

botoneliminar=Button(miFrame, text="Eliminar", command=bteliminar)
botoneliminar.grid(row = 6, column = 2)
botoneliminar.config(state=DISABLED, bg = '#E0DFE3')

######################Crear radiobutton----------------------
opcion=IntVar()
rdBBusc=Radiobutton(miFrame, text="Buscar",  variable=opcion, value=1, command=botonRadio)        
rdBBusc.grid(row = 4, column = 1)
rdBBusc.config( bg = '#FCF5E2')

rdBModif=Radiobutton(miFrame, text="Modificar", variable=opcion, value=2, command=botonRadio)
rdBModif.grid(row = 5, column = 1)
rdBModif.config( bg = '#FCF5E2')

rdBElimi=Radiobutton(miFrame, text="Eliminar", variable=opcion, value=3, command=botonRadio)
rdBElimi.grid(row = 6, column = 1)
rdBElimi.config( bg = '#FCF5E2')

#Mostramos ventana
raiz.mainloop()
