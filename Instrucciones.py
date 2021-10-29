from Expresiones import *
from graphviz import Graph

documento=""
ad=""
sumarr=""
maxx=""
minn=""
lval=[]
ltodo=[]

    
class InstruccionEpsilon():
    def __init__(self) :
        pass
    def ejecutar(self,entorno):
        pass
    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"Epsilon")
        return idnodo


class IntruccionMin() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento
        global minn
        valor = self.expresion.getValor(entorno)

        listaa=[]
        cont=0
        for i in valor:
            cont=cont+1
            if cont==len(valor):
                minn=i
            else:
                listaa.append(i)

        for n in range(len(listaa)-1,0,-1):
            for i in range(n):
                if listaa[i]>listaa[i+1]:
                    temp = listaa[i]
                    listaa[i] = listaa[i+1]
                    listaa[i+1] = temp

        
        print()
        print(listaa[0])
        documento=documento+"\n"
        documento=documento+ str(listaa[0]) +"\n"

    def getNodos(self):
        global dot
        global minn
        idnodo=str(inc())
        dot.node(idnodo,"INS_MIN")

        idimprimir=str(inc())
        dot.node(idimprimir,"min")

        idpara=str(inc())
        dot.node(idpara,"(")
        
        idex=str(inc())
        dot.node(idex,"expresion")

        idl=str(inc())
        dot.node(idl,"literal")


        idmax=str(inc())
        dot.node(idmax,minn)

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idex)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        dot.edge(idex,idl)
        dot.edge(idl,idmax)
        return idnodo
        

class IntruccionMax() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento
        global maxx
        valor = self.expresion.getValor(entorno)
        listaa=[]
        cont=0
        for i in valor:
            cont=cont+1
            if cont==len(valor):
                maxx=i
            else:
                listaa.append(i)


        for n in range(len(listaa)-1,0,-1):
            for i in range(n):
                if listaa[i]>listaa[i+1]:
                    temp = listaa[i]
                    listaa[i] = listaa[i+1]
                    listaa[i+1] = temp

        print()
        pos=len(listaa)-1
        print(listaa[pos])

        documento=documento +"\n"
        documento=documento+ str(listaa[pos]) +"\n"
        

    def getNodos(self):
        global dot
        global maxx
        idnodo=str(inc())
        dot.node(idnodo,"INS_MAX")

        idimprimir=str(inc())
        dot.node(idimprimir,"max")

        idpara=str(inc())
        dot.node(idpara,"(")
        
        idex=str(inc())
        dot.node(idex,"expresion")

        idl=str(inc())
        dot.node(idl,"literal")


        idmax=str(inc())
        dot.node(idmax,maxx)

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idex)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        dot.edge(idex,idl)
        dot.edge(idl,idmax)
        return idnodo

class IntruccionSumar() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global sumarr
        valor = self.expresion.getValor(entorno)
        print()
        v=str(valor)
        vl=v.split(",")
        print(vl[1])
        global documento
        documento=documento +"\n"
        documento=documento+ str(vl[1]) +"\n"
        sumarr=vl[0]
    
    def getNodos(self):
        global ad
        global dot
        global sumarr
        idnodo=str(inc())
        dot.node(idnodo,"INS_SUMA")

        idimprimir=str(inc())
        dot.node(idimprimir,"sumar")

        idpara=str(inc())
        dot.node(idpara,"(")
        
        idex=str(inc())
        dot.node(idex,"expresion")

        idl=str(inc())
        dot.node(idl,"literal")


        idsu=str(inc())
        dot.node(idsu,sumarr)

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idex)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        dot.edge(idex,idl)
        dot.edge(idl,idsu)
        return idnodo


class IntruccionDatos() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento
        valor = self.expresion.getValor(entorno)
        print()
        documento=documento +"\n"
        datos=""
        tamaño=len(valor[0])
        for i in valor:
            for j in range(tamaño):
                datos+=str(i[j])+ "\t"
            print(datos)
            documento=documento+ str(datos) +"\n"
            datos=""
    
    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INS_DATOS")

        iddatos=str(inc())
        dot.node(iddatos,"datos")

        idpara=str(inc())
        dot.node(idpara,"(")

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,iddatos)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        return idnodo
        

class IntruccionPromedio() :
    def __init__(self, expresion) :
        self.expresion = expresion
        

    def ejecutar(self, entorno):
        global ad
        global documento
        valor = self.expresion.getValor(entorno)
        print()
        v=str(valor)
        listaV=v.split(",")
        print(listaV[1])
        promedioa=listaV[0]
        documento=documento +"\n"
        documento=documento+ str(listaV[1]) +"\n"
        ad=str(listaV[0])
        
        
    
    def getNodos(self):
        global ad
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INS_PROMEDIO")

        idimprimir=str(inc())
        dot.node(idimprimir,"promedio")

        idpara=str(inc())
        dot.node(idpara,"(")
        
        idex=str(inc())
        dot.node(idex,"expresion")

        idl=str(inc())
        dot.node(idl,"literal")


        idpro=str(inc())
        dot.node(idpro,ad)

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idex)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        dot.edge(idex,idl)
        dot.edge(idl,idpro)
        return idnodo

class IntruccionConteo() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento
        valor = self.expresion.getValor(entorno)
        print(valor)
        documento=documento +"\n"
        documento=documento+ str(valor) +"\n"
    
    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INS_CONTEO")

        idimprimir=str(inc())
        dot.node(idimprimir,"conteo")

        idpara=str(inc())
        dot.node(idpara,"(")

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        return idnodo

class IntruccionImprimirln() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento
        valor = self.expresion.getValor(entorno)
        print()
        print(valor)
        documento=documento +"\n"
        documento=documento+ str(valor) +"\n"

    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INS_IMPRIMIRLN")

        idimprimir=str(inc())
        dot.node(idimprimir,"imprimirln")

        idpara=str(inc())
        dot.node(idpara,"(")

        hijo=self.expresion.getNodos()

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        return idnodo

class IntruccionRegistro() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global ltodo
        valor = self.expresion.getValor(entorno)
        ltodo=valor
    
    def getNodos(self):
        global dot
        global ltodo
        listareg=[]
        c1=0
        for i in ltodo:
            c1=c1+1
            if c1==1:
                pass   
            else:
                listareg.append(i)

        idnodo=str(inc())
        dot.node(idnodo,"INS_REGISTRO")

        idregistros=str(inc())
        dot.node(idregistros,"Registros")

        idigual=str(inc())
        dot.node(idigual,"=")

        idillavea=str(inc())
        dot.node(idillavea,"[")

        idlistaregistro=str(inc())
        dot.node(idlistaregistro,"lista_Registros")


        idillavec=str(inc())
        dot.node(idillavec,"]")

        dot.edge(idnodo,idregistros)
        dot.edge(idnodo,idigual)
        dot.edge(idnodo,idillavea)
        dot.edge(idnodo,idlistaregistro)
        dot.edge(idnodo,idillavec)

        for i in listareg:
            x=str(inc())
            dot.node(x,"{")
            dot.edge(idlistaregistro,x)

            v=str(inc())
            dot.node(v,"Lista_ValoresRegistro")
            dot.edge(idlistaregistro,v)
            conteo=0
            for j in i:
                conteo=conteo+1
                if conteo==len(i):
                    aa=str(inc())
                    dot.node(aa,str(j))
                    dot.edge(v,aa)
                else:
                    aa=str(inc())
                    dot.node(aa,str(j))
                    dot.edge(v,aa)

                    aaa=str(inc())
                    dot.node(aaa,",")
                    dot.edge(v,aaa)




            x2=str(inc())
            dot.node(x2,"}")
            dot.edge(idlistaregistro,x2)
           



       

        return idnodo

class IntruccionValores() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global lval
        valor = self.expresion.getValor(entorno)
        lval=valor
 
    
    def getNodos(self):
        global dot
        global lval
        idnodo=str(inc())
        dot.node(idnodo,"INS_CLAVE")

        idiclaves=str(inc())
        dot.node(idiclaves,"Claves")

        idigual=str(inc())
        dot.node(idigual,"=")

        idillavea=str(inc())
        dot.node(idillavea,"[")

        idlista=str(inc())
        dot.node(idlista,"lista_Claves")


        idillavec=str(inc())
        dot.node(idillavec,"]")

        dot.edge(idnodo,idiclaves)
        dot.edge(idnodo,idigual)
        dot.edge(idnodo,idillavea)
        dot.edge(idnodo,idlista)
        dot.edge(idnodo,idillavec)
        c=0
        for i in lval:
            c+=1
            x=str(inc())
            dot.node(x,i)
            if c==(len(lval)):
                dot.edge(idlista,x)
            else:
                x2=str(inc())
                dot.node(x2,",")
                dot.edge(idlista,x)
                dot.edge(idlista,x2)

        return idnodo


class IntruccionImprimir() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global documento 
        valor = self.expresion.getValor(entorno)
        print(valor,end="")
        documento=documento+ str(valor) 
    
    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INS_IMPRIMIR")

        idimprimir=str(inc())
        dot.node(idimprimir,"imprimir")

        idpara=str(inc())
        dot.node(idpara,"(")

        hijo=self.expresion.getNodos()

        idparc=str(inc())
        dot.node(idparc,")")

        idpcoma=str(inc())
        dot.node(idpcoma,";")

        dot.edge(idnodo,idimprimir)
        dot.edge(idnodo,idpara)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idparc)
        dot.edge(idnodo,idpcoma)
        return idnodo




class IntruccionInstruccion() :
    def __init__(self, instruccion) :
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)
    
    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"INSTRUCCION")
        hijo=self.instruccion.getNodos()
        dot.edge(idnodo,hijo)
        return idnodo

class IntruccionListaInstrucciones2() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"LISTAINSTRUCCIONES")
        if self.instruccion:
            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)
            if self.lista:
                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        
        
        return idnodo

class IntruccionListaInstrucciones() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(inc())
        dot.node(idnodo,"LISTAINSTRUCCIONES")
        if self.instruccion:
            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)
            if self.lista:
                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class IntruccionInicio() :
    def __init__(self,lista) :
        self.lista = lista

    def ejecutar(self, entorno):
        self.lista.ejecutar(entorno)
    
    def getNodos(self):
        global dot 
        idnodo=str(inc())
        dot.node(idnodo,"INICIO")
        hijo=self.lista.getNodos()
        dot.edge(idnodo,hijo)
        dot.view()
        return idnodo



class Debugg() :

    def Documento(self):
        global documento
        documento2=documento
        documento=""
        return documento2