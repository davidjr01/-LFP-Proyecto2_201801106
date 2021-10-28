class ExpresionIdentificador() :
    def __init__(self, id) :
        self.id = id
    def getValor(self, entorno):
        return entorno.get(self.id)


class ExpresionLiteral() :
    def __init__(self, tipo, valor) :
        self.tipo = tipo
        self.valor = valor

    def getValor(self, entorno):
        return self.valor