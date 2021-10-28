from Token import Token
from Error import Error
from Expresiones import *
from Instrucciones import *

class AnalizadorSintactico:
    
    def __init__(self):
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0
        self.listaDatos=[]
        self.listaTemp=[]


 ################ registro ##########################################################################   
    def val_reg(self):
        if self.listaTokens[self.i].tipo=='llavec': 
            self.i+=1
        elif self.listaTokens[self.i].tipo=='entero':  ## de aca es donde se toman los datos
            lexema=int(self.listaTokens[self.i].lexema)
            self.listaTemp.append(lexema)
            self.i+=1
        elif self.listaTokens[self.i].tipo=='decimal':  ## de aca es donde se toman los datos
            lexema=self.listaTokens[self.i].lexema
            self.listaTemp.append(lexema)
            self.i+=1
        elif self.listaTokens[self.i].tipo=='cadena':  ## de aca es donde se toman los datos
            lexema=self.listaTokens[self.i].lexema
            self.listaTemp.append(lexema)
            self.i+=1
        else:
            pass


    def lista_val_reg2(self):
        if self.listaTokens[self.i].tipo=='llavec': 
            self.listaDatos.append(self.listaTemp)
            self.listaTemp=[]
        elif self.listaTokens[self.i].tipo=='coma': 
            self.i+=1
            self.val_reg()
            self.lista_val_reg2()

    def lista_val_reg(self):
        self.val_reg()
        self.lista_val_reg2()

    def registro(self):
        if self.listaTokens[self.i].tipo=='llavea': 
            self.i+=1
            self.lista_val_reg()
            if self.listaTokens[self.i].tipo=='llavec':
                self.i+=1 

    def lista_registros2(self):
        if self.listaTokens[self.i].tipo=='corchetec': 
            pass
        else:
            self.registro()
            self.lista_registros2()


    def lista_registros(self):
        self.registro()
        self.lista_registros2()


    def ins_registros(self):
        if self.listaTokens[self.i].tipo=='registros': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='igual': 
                self.i+=1
                if self.listaTokens[self.i].tipo=='corchetea': 
                    self.i+=1
                    self.lista_registros()
                    if self.listaTokens[self.i].tipo=='corchetec': 
                        self.i+=1
                        

################claves##########################################################################
    def val_clave(self):
        if self.listaTokens[self.i].tipo=='llavec': 
            self.i+=1
        elif self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            lexema=str(self.listaTokens[self.i].lexema)
            lexema=lexema.replace('"','')
            self.listaTemp.append(lexema)
            self.i+=1
        else:
            pass

    def claves(self):
        if self.listaTokens[self.i].tipo=='coma': 
            self.i+=1
        else:
            self.val_clave()
    
    def lista_claves2(self):
        if self.listaTokens[self.i].tipo=='corchetec': 
            pass
        else:
            self.claves()
            self.lista_claves2()
        
    
    def lista_claves(self):
        self.claves()
        self.lista_claves2()

    def ins_claves(self):
        if self.listaTokens[self.i].tipo=='claves': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='igual': 
                self.i+=1
                if self.listaTokens[self.i].tipo=='corchetea': 
                    self.i+=1
                    self.lista_claves()
                    if self.listaTokens[self.i].tipo=='corchetec':  ##aca se deja de leer los datos de valor
                        self.listaDatos.append(self.listaTemp)
                        self.listaTemp=[]
                        ##print(self.listaDatos)
                        self.i+=1

################## immpirmir ####################################################################
    def val_imp(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            lexema=str(self.listaTokens[self.i].lexema)
            lexema=lexema.replace('"','')
            expresion=ExpresionLiteral("cadena",lexema)
            self.i+=1
            return expresion
           
    def ins_imprimir(self):
        if self.listaTokens[self.i].tipo=='imprimir': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_imp()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionImprimir(expresion)

                    
################## immpirmirln ####################################################################
    def val_impln(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            lexema=self.listaTokens[self.i].lexema
            lexema=lexema.replace('"','')
            expresion=ExpresionLiteral("cadena",lexema)
            self.i+=1
            return expresion
    
    def ins_imprimirln(self):
        if self.listaTokens[self.i].tipo=='imprimirln': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_impln()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionImprimirln(expresion)

################## conteo ####################################################################
    def val_conteo(self):
        valor=len(self.listaDatos)-1
        expresion=ExpresionLiteral("cadena",valor)
        return expresion

    def ins_conteo(self):
        if self.listaTokens[self.i].tipo=='conteo': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_conteo()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionConteo(expresion)



################## promedio ####################################################################
    def val_promedio(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            campo=str(self.listaTokens[self.i].lexema)
            campo=campo.replace('"','')
            itempo=-1
            index=0
            for i in self.listaDatos[0]:
                itempo=itempo+1
                if campo==i:
                    index=itempo
                    break   
            promedio=0.0
            tope=0
            for i in self.listaDatos:
                tope=tope+1
                if tope>1:
                    promedio=promedio+float(i[index])
            
            promedio2=promedio/(len(self.listaDatos)-1)


            expresion=ExpresionLiteral("cadena",promedio2)
            self.i+=1
            return expresion
                
            
    def ins_promedio(self):
        if self.listaTokens[self.i].tipo=='promedio': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_promedio()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionPromedio(expresion)

################################## datos() #####################################################

    def val_datos(self):
        expresion=ExpresionLiteral("cadena",self.listaDatos)
        return expresion

    def ins_datos(self):
        if self.listaTokens[self.i].tipo=='datos': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_datos()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionDatos(expresion)

##############################sumar()############################################################

    def val_sumar(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            campo=str(self.listaTokens[self.i].lexema)
            campo=campo.replace('"','')
            itempo=-1
            index=0
            for i in self.listaDatos[0]:
                itempo=itempo+1
                if campo==i:
                    index=itempo
                    break   
            promedio=0.0
            tope=0
            for i in self.listaDatos:
                tope=tope+1
                if tope>1:
                    promedio=promedio+float(i[index])
            
            expresion=ExpresionLiteral("cadena",promedio)
            self.i+=1
            return expresion
                
            
    def ins_sumar(self):
        if self.listaTokens[self.i].tipo=='sumar': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_sumar()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionSumar(expresion)

######################################### Max ()######################################################

    def val_max(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            campo=str(self.listaTokens[self.i].lexema)
            campo=campo.replace('"','')
            itempo=-1
            index=0
            ldatos=[]
            for i in self.listaDatos[0]:
                itempo=itempo+1
                if campo==i:
                    index=itempo
                    break   
            promedio=0.0
            tope=0
            for i in self.listaDatos:
                tope=tope+1
                if tope>1:
                    ldatos.append(float(i[index]))
            
            expresion=ExpresionLiteral("cadena",ldatos)
            self.i+=1
            return expresion
                
            
    def ins_max(self):
        if self.listaTokens[self.i].tipo=='max': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_max()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionMax(expresion)

################################ Min() ##########################################################
    def val_min(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            campo=str(self.listaTokens[self.i].lexema)
            campo=campo.replace('"','')
            itempo=-1
            index=0
            ldatos=[]
            for i in self.listaDatos[0]:
                itempo=itempo+1
                if campo==i:
                    index=itempo
                    break   
            promedio=0.0
            tope=0
            for i in self.listaDatos:
                tope=tope+1
                if tope>1:
                    ldatos.append(float(i[index]))
            
            expresion=ExpresionLiteral("cadena",ldatos)
            self.i+=1
            return expresion
                
            
    def ins_min(self):
        if self.listaTokens[self.i].tipo=='min': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                expresion=self.val_min()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                        return IntruccionMin(expresion)
#################################################################################################
    def instrucciones(self):  ##############aca se modifica para instrucciones clase
        if self.listaTokens[self.i].tipo=='registros': 
            self.ins_registros()
        if self.listaTokens[self.i].tipo=='claves': 
            self.ins_claves()

        if self.listaTokens[self.i].tipo=='imprimir': 
            ins=self.ins_imprimir()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='imprimirln': 
            ins=self.ins_imprimirln()
            return IntruccionInstruccion(ins)

        if self.listaTokens[self.i].tipo=='conteo':   
            ins=self.ins_conteo()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='promedio': 
            ins=self.ins_promedio()
            return IntruccionInstruccion(ins)

        if self.listaTokens[self.i].tipo=='contarsi': 
            ins=self.ins_contarsi()
            return IntruccionInstruccion(ins)

        if self.listaTokens[self.i].tipo=='datos': 
            ins=self.ins_datos()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='sumar': 
            ins=self.ins_sumar()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='max': 
            ins=self.ins_max()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='min': 
            ins=self.ins_min()
            return IntruccionInstruccion(ins)
        
        if self.listaTokens[self.i].tipo=='exportarReporte': 
            ins=self.ins_exportarReporte()
            return IntruccionInstruccion(ins)



    def lista_instrucciones2(self): ##de aca deriban todas las intrucciones
        
        if self.listaTokens[self.i].tipo=='EOF':
            print("analisis sintactico exitoso")
            return None
        elif self.listaTokens[self.i].tipo=='registros' or self.listaTokens[self.i].tipo=='claves' or  self.listaTokens[self.i].tipo=='imprimir' or self.listaTokens[self.i].tipo=='imprimirln' or self.listaTokens[self.i].tipo=='conteo' or self.listaTokens[self.i].tipo=='promedio'or self.listaTokens[self.i].tipo=='contarsi' or self.listaTokens[self.i].tipo=='datos' or self.listaTokens[self.i].tipo=='sumar' or self.listaTokens[self.i].tipo=='max' or self.listaTokens[self.i].tipo=='min' or self.listaTokens[self.i].tipo=='exportarReporte':    
            ins=self.instrucciones()
            lista=self.lista_instrucciones2()
            return IntruccionListaInstrucciones2(ins,lista)

        else:
            linea=self.listaTokens[self.i].linea
            columna=self.listaTokens[self.i].columna
            self.listaErrores.append(Error('error sintactico','sintactico',linea,columna))

    def lista_instrucciones(self): ##de aca deriban todas las intrucciones
        
        if self.listaTokens[self.i].tipo=='registros' or self.listaTokens[self.i].tipo=='claves' or  self.listaTokens[self.i].tipo=='imprimir' or self.listaTokens[self.i].tipo=='imprimirln' or self.listaTokens[self.i].tipo=='conteo' or self.listaTokens[self.i].tipo=='promedio'or self.listaTokens[self.i].tipo=='contarsi' or self.listaTokens[self.i].tipo=='datos' or self.listaTokens[self.i].tipo=='sumar' or self.listaTokens[self.i].tipo=='max' or self.listaTokens[self.i].tipo=='min' or self.listaTokens[self.i].tipo=='exportarReporte':    
            ins=self.instrucciones()
            lista=self.lista_instrucciones2()
            return IntruccionListaInstrucciones(ins,lista)
            
        else:
            linea=self.listaTokens[self.i].linea
            columna=self.listaTokens[self.i].columna
            self.listaErrores.append(Error('error sintactico','sintactico',linea,columna))

        

    def inicio(self):
        lista=self.lista_instrucciones()
        return IntruccionInicio(lista)
        

    def analizar(self,listaTokens):
        
        self.i=0
        self.listaTokens=listaTokens
        arbolIns=self.inicio()
        arbolIns.ejecutar({})
      
        