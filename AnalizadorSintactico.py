from Token import Token
from Error import Error

class AnalizadorSintactico:
    
    def __init__(self):
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0


 ################ registro ##########################################################################   
    def val_reg(self):
        if self.listaTokens[self.i].tipo=='llavec': 
            self.i+=1
        elif self.listaTokens[self.i].tipo=='entero':  ## de aca es donde se toman los datos
            
            self.i+=1
        elif self.listaTokens[self.i].tipo=='decimal':  ## de aca es donde se toman los datos
            
            self.i+=1
        elif self.listaTokens[self.i].tipo=='cadena':  ## de aca es donde se toman los datos
           
            self.i+=1
        else:
            pass


    def lista_val_reg2(self):
        if self.listaTokens[self.i].tipo=='llavec': 
            pass
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
                    if self.listaTokens[self.i].tipo=='corchetec': 
                        self.i+=1

################## immpirmir ####################################################################
    def val_imp(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            self.i+=1
           

    
    def ins_imprimir(self):
        if self.listaTokens[self.i].tipo=='imprimir': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                self.val_imp()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1
                    
################## immpirmirln ####################################################################
    def val_impln(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            self.i+=1
    
    def ins_imprimirln(self):
        if self.listaTokens[self.i].tipo=='imprimirln': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                self.val_impln()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1

################## conteo ####################################################################
    
    def ins_conteo(self):
        if self.listaTokens[self.i].tipo=='conteo': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1

################## promedio ####################################################################
    def val_promedio(self):
        if self.listaTokens[self.i].tipo=='cadena':  # de aca es donde se toman los datos
            self.i+=1

    def ins_promedio(self):
        if self.listaTokens[self.i].tipo=='promedio': 
            self.i+=1
            if self.listaTokens[self.i].tipo=='para': 
                self.i+=1
                self.val_promedio()
                if self.listaTokens[self.i].tipo=='parc': 
                    self.i+=1
                    if self.listaTokens[self.i].tipo=='puntocoma': 
                        self.i+=1

#################################################################################################
    def instrucciones(self): 
        if self.listaTokens[self.i].tipo=='registros': 
            self.ins_registros()
        if self.listaTokens[self.i].tipo=='claves': 
            self.ins_claves()

        if self.listaTokens[self.i].tipo=='imprimir': 
            self.ins_imprimir()
        
        if self.listaTokens[self.i].tipo=='imprimirln': 
            self.ins_imprimirln()
        
        if self.listaTokens[self.i].tipo=='conteo': 
            self.ins_conteo()
        
        if self.listaTokens[self.i].tipo=='promedio': 
            self.ins_promedio()


    def lista_instrucciones2(self): ##de aca deriban todas las intrucciones
        if self.listaTokens[self.i].tipo=='registros': 
            self.instrucciones()
            self.lista_instrucciones2()
        if self.listaTokens[self.i].tipo=='claves': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='imprimir': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='imprimirln': 
            self.instrucciones()
            self.lista_instrucciones2()
        
        if self.listaTokens[self.i].tipo=='conteo': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='promedio': 
            self.instrucciones()
            self.lista_instrucciones2()

        elif self.listaTokens[self.i].tipo=='EOF':
            print("analisis sintactico exitoso")

        else:
            linea=self.listaTokens[self.i].linea
            columna=self.listaTokens[self.i].columna
            self.listaErrores.append(Error('error sintactico','sintactico',linea,columna))

    def lista_instrucciones(self): 
        if self.listaTokens[self.i].tipo=='registros': 
            self.instrucciones()
            self.lista_instrucciones2()
        if self.listaTokens[self.i].tipo=='claves': 
            self.instrucciones()
            self.lista_instrucciones2()
        if self.listaTokens[self.i].tipo=='imprimir': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='imprimirln': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='conteo': 
            self.instrucciones()
            self.lista_instrucciones2()

        if self.listaTokens[self.i].tipo=='promedio': 
            self.instrucciones()
            self.lista_instrucciones2()
        else:
            linea=self.listaTokens[self.i].linea
            columna=self.listaTokens[self.i].columna
            self.listaErrores.append(Error('error sintactico','sintactico',linea,columna))

        

    def inicio(self):
        self.lista_instrucciones()
        pass




    def analizar(self,listaTokens):
        
        self.i=0
        self.listaTokens=listaTokens
        self.inicio()
      
        