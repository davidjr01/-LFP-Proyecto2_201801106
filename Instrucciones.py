from Expresiones import *


class IntruccionMin() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)

        for n in range(len(valor)-1,0,-1):
            for i in range(n):
                if valor[i]>valor[i+1]:
                    temp = valor[i]
                    valor[i] = valor[i+1]
                    valor[i+1] = temp

        print()
        print(valor[0])
        

class IntruccionMax() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)

        for n in range(len(valor)-1,0,-1):
            for i in range(n):
                if valor[i]>valor[i+1]:
                    temp = valor[i]
                    valor[i] = valor[i+1]
                    valor[i+1] = temp

        print()
        pos=len(valor)-1
        print(valor[pos])

class IntruccionSumar() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print()
        print(valor)


class IntruccionDatos() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print()
        datos=""
        tamaño=len(valor[0])
        for i in valor:
            for j in range(tamaño):
                datos+=str(i[j])+ "\t"
            print(datos)
            datos=""
        

class IntruccionPromedio() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print()
        print(valor)

class IntruccionConteo() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print(valor)

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