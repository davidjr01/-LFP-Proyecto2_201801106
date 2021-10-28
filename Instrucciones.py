from Expresiones import *


class IntruccionImprimirln() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print()
        print(valor)

class IntruccionImprimir() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print(valor,end="")

class IntruccionInstruccion() :
    def __init__(self, instruccion) :
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

class IntruccionListaInstrucciones2() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

class IntruccionListaInstrucciones() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

class IntruccionInicio() :
    def __init__(self,lista) :
        self.lista = lista

    def ejecutar(self, entorno):
        self.lista.ejecutar(entorno)