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




ventana=Tk()


def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def cargar2():
    global imagenes
    direccion=askopenfilename()
    codigo=leerArchivo(direccion)
    scanner = AnalizadorLexico()
    listaTokens=scanner.analizar(codigo)
    parser = AnalizadorSintactico()
    parser.analizar(listaTokens)
    

cargar2()