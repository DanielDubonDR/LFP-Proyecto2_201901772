class historial:
    def __init__(self, iteracion, pila, entrada, transicion):
        self.iteracion=iteracion
        self.pila=pila
        self.entrada=entrada
        self.transicion=transicion
    
    def __str__(self):
        txt=str(self.iteracion)+" "+str(self.pila)+" "+str(self.entrada)+" "+str(self.transicion)
        return txt