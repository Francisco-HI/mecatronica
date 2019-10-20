"""
Esta parte sera para agregar el menu superior a todas las ventanas,
Así que si se agrega una nueva opcion desplegable aquí, se agregara
a todas las ventanas con esta clase
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os



class desplegable():
    #Constructor: instancia la clase para construir objetos
    def __init__(self, raiz):
        
        self.raizz = raiz


        def AgregarFrm():
            raiz.destroy()
            direccion = r'"' + str(os.path.dirname(os.path.abspath(__file__))) + '"\VTNagregar.py '       #optener la direccion donde se esta ejecutando el script actual
            os.system('python '+ str(direccion))
            
            #os.system('python '+ r'"C:\Users\FRANCISCO\Google Drive\7mo semestre\programacion\unidad 3\Programas\dashboard\calculadoraTkinter.py"')
            #raiz.destroy()

        def ModificarFrm():
            raiz.destroy()
            direccion = r'"' + str(os.path.dirname(os.path.abspath(__file__))) + '"\VTNmodificar.py '       #optener la direccion donde se esta ejecutando el script actual
            os.system('python '+ str(direccion))
        
        def Somos():
            raiz.destroy()
            direccion = r'"' + str(os.path.dirname(os.path.abspath(__file__))) + '"\main.py '       #optener la direccion donde se esta ejecutando el script actual
            os.system('python '+ str(direccion))

        def Credits():
            raiz.destroy()
            direccion = r'"' + str(os.path.dirname(os.path.abspath(__file__))) + '"\creditos.py '       #optener la direccion donde se esta ejecutando el script actual
            os.system('python '+ str(direccion))
                
            

       

        menubar= Menu(raiz)

        #Construir opciones de raiz
        menutrab=Menu(menubar, tearoff=0)
        menutrab.add_command(label="Agregar",command=AgregarFrm)
        menutrab.add_command(label="Buscar, Cambiar y Eliminar",command=ModificarFrm)
        menubar.add_cascade(label="Trabajadores",menu=menutrab)

        #Dibujar el menu para los reportes
        menurep=Menu(menubar,tearoff=0)
        #menurep.add_command(label="Pantalla",command="mensaje")
        menurep.add_command(label="PDF",command="mensaje")
        menubar.add_cascade(label="Reportes",menu=menurep)

        #dibujar el menu para salir de la app
        menusalir=Menu(menubar,tearoff=0)
        menusalir.add_command(label="Creditor",command=Credits)
        menusalir.add_command(label="Salir",command=quit)
        menusalir.add_command(label="Quienes somos?",command=Somos)
        menubar.add_cascade(label="Quienes somos?",menu=menusalir)

        # Display the menu
        raiz.config(menu=menubar)

    


 
