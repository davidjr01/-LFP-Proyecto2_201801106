from re import T
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from tkinter import *
from tkinter import ttk
from typing import Counter, final
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import scrolledtext
from Instrucciones import *




ventana=Tk()


def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido
def cargar_archivo():
    direccion=askopenfilename()
    codigo=leerArchivo(direccion)
    return codigo

def cargar2():
    direccion=askopenfilename()
    codigo=leerArchivo(direccion)
    scanner = AnalizadorLexico()
    listaTokens=scanner.analizar(codigo)
    #scanner.imprimirToken()
    parser = AnalizadorSintactico()
    parser.analizar(listaTokens)
    


#cargar2()


def salir():
    ventana.destroy()

def btCargar():
    codigo=cargar_archivo()
    txt.insert(INSERT,codigo)

def btAnalizar():
    listaTokens=[]
    txt2.delete("1.0", tk.END)
    codigo2=txt.get("1.0",tk.END) ##para obtener texto de un textarea
    scanner = AnalizadorLexico()
    listaTokens=scanner.analizar(codigo2)
    #scanner.imprimirToken()
    parser = AnalizadorSintactico()
    parser.analizar(listaTokens)
    asdf=Debugg()
    txt2.insert(INSERT,asdf.Documento())
    txt2.configure(state='disabled')
   


anchoventana=int(1070)
largoventana=int(750)
x_ventana =(int( ventana.winfo_screenwidth()/2))-(int(anchoventana/2))
y_ventana = int((ventana.winfo_screenheight() -100 )/2)-(int(largoventana/2))
posicion = str(anchoventana) + "x" + str(largoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("INICIO")
ventana.resizable(False,False)


#FRAMES ---------------
mframe=Frame(ventana,width=350 ,height=60)
mframe.config(bg="#ABB2B9")
mframe.place(x=700,y=15)

linea=Frame(ventana,width=1030 ,height=5)
linea.config(bg="black")
linea.place(x=20,y=80)


mframe2=Frame(ventana,width=505 ,height=640)
mframe2.config(bg="red")
mframe2.place(x=20,y=90)

mframe3=Frame(ventana,width=505 ,height=640)
mframe3.config(bg="white")
mframe3.place(x=545,y=90)

#text area --------------------------------------
txt=scrolledtext.ScrolledText(mframe2,width=60 ,height=40)
txt.grid(column=0,row=0)

txt2=scrolledtext.ScrolledText(mframe3,width=60 ,height=40)
txt2.grid(column=0,row=0)

#BOTONES  ---------------

boton1=Button(mframe,text="CARGAR",command=btCargar)
boton1.place(x=10,y=10,width=60,height=30)

boton2=Button(mframe,text="ANALIZAR",command=btAnalizar)
boton2.place(x=80,y=10,width=65,height=30)

boton2=Button(mframe,text="REPORTES")
boton2.place(x=155,y=10,width=65,height=30)

boton2=Button(mframe,text="SALIR",command=salir)
boton2.place(x=240,y=10,width=65,height=30)





ventana.mainloop()
