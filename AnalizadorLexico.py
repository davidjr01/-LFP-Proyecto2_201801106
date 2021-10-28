from Token import Token
from Error import Error
import re
from tkinter import messagebox


class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analizar(self, codigo_fuente):
        self.listaTokens = []
        self.listaErrores = []

        # Atributos
        linea = 1
        columna = 1
        buffer = ''
        centinela = '$'
        estado = 0
        codigo_fuente += centinela

        # automata
        i = 0
        while i < len(codigo_fuente):
            c = codigo_fuente[i]

            if estado == 0:
                if c == '=':
                    buffer += c
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'igual', linea, columna))
                    buffer = ''
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llavea', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llavec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corchetea', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corchetec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '(':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'para', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'parc', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '"':
                    buffer += c
                    columna += 1
                    estado = 1  # ENTRA AL ESTADO 1, ESTADO DE CADENA
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2  # ENTRA AL ESTADO 2, ESTADO DE DIGITOS
                elif re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3  # ENTRA AL ESTADO 3, ESTADO DE PALABRAS RESERVADAS
                elif c == '#':
                    buffer += c
                    columna += 1
                    estado = 4  # ENTRA AL ESTADO 4, ESTADO DE COMENTARIO DE UNA LINEA
                elif c == "'":
                    buffer += c
                    columna += 1
                    estado = 5  # ENTRA AL ESTADO 5, ESTADO DE COMENTARIO MULTILINEA
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == '\t':
                    columna += 1
                elif c == ' ':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela:
                    self.listaTokens.append(Token('$', 'EOF', linea, columna))

                    messagebox.showinfo(message='El archivo fue analizado correctamete.')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error(buffer + ' no es reconocido.', 'Lexico', linea, columna))
                    buffer = ''
                    columna += 1

            elif estado == 1:  # ESTADO DE CADENA
                if c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1

            elif estado == 2:  # ESTADO DE DIGITOS
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                elif c == '.':
                    buffer += c
                    columna += 1
                    estado = 6  # ENTRA AL ESTADO 2, ESTADO DE DECIMALES
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0

            elif estado == 3:  # ESTADO DE PALABRAS RESERVADAS
                if re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'Claves':
                        self.listaTokens.append(Token(buffer, 'claves', linea, columna))
                    elif buffer == 'Registros':
                        self.listaTokens.append(Token(buffer, 'registros', linea, columna))
                    elif buffer == 'imprimir':
                        self.listaTokens.append(Token(buffer, 'imprimir', linea, columna))
                    elif buffer == 'imprimirln':
                        self.listaTokens.append(Token(buffer, 'imprimirln', linea, columna))
                    elif buffer == 'conteo':
                        self.listaTokens.append(Token(buffer, 'conteo', linea, columna))
                    elif buffer == 'promedio':
                        self.listaTokens.append(Token(buffer, 'promedio', linea, columna))
                    elif buffer == 'contarsi':
                        self.listaTokens.append(Token(buffer, 'contarsi', linea, columna))
                    elif buffer == 'datos':
                        self.listaTokens.append(Token(buffer, 'datos', linea, columna))
                    elif buffer == 'sumar':
                        self.listaTokens.append(Token(buffer, 'sumar', linea, columna))
                    elif buffer == 'max':
                        self.listaTokens.append(Token(buffer, 'max', linea, columna))
                    elif buffer == 'min':
                        self.listaTokens.append(Token(buffer, 'min', linea, columna))
                    elif buffer == 'exportarReporte':
                        self.listaTokens.append(Token(buffer, 'exportarReporte', linea, columna))
                    else:
                        self.listaErrores.append(Error(buffer + ' no es reconocido.', 'Lexico', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0

            elif estado == 4:  # ESTADO DE COMENTARIO DE UNA LINEA
                if c == '\n':
                    self.listaTokens.append(Token(buffer, 'comentario de una linea', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
                else:
                    buffer += c
                    columna += 1

            elif estado == 5:  # ESTADO DE COMENTARIO MULTILINEA
                if c == "'":
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'comentario multilinea', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
               
            elif estado == 6:  # ESTADO DE DECIMALES
                if re.search('\d', c):
                    buffer += c
                else:
                    self.listaTokens.append(Token(buffer, 'decimal', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            i += 1
        return self.listaTokens

    def imprimirToken(self):
        archivo = open('tokens.txt', 'w')
        for p in self.listaTokens:
            lineaa=str(p.linea )+ ""
            columnaa=str(p.columna)+""
            print("Lexema: " + p.lexema+"    Tipo:  "  + p.tipo+"   Linea  " + lineaa+"   Columna:   " + columnaa+"\n" )
        

