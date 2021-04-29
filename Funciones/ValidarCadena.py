from Clases.Historial import historial
from Clases.Transiciones import TransicionNT

class validar:
    def __init__(self, gramatica, cadena):
        self.pila=[]
        self.gramatica=gramatica
        self.historial=[]
        self.transionesNTerminales=[]
        self.cadena=cadena
        self.generarTransiciones()
        self.verificar()
    
    def generarTransiciones(self):
        for i in self.gramatica.P:
            for j in i.expresiones:
                self.transionesNTerminales.append(TransicionNT(i.NoT,j))
        '''
        for i in self.transionesNTerminales:
            print(i)
        '''

    def verificar(self):
        print(self.cadena)
        print(self.cadena[0])
        if self.verificarAlfabeto(self.cadena[0]):
            self.historial.append(historial(0,"",self.cadena[0],"(i,λ,λ;p,#)"))
            self.pila.append("#")
            self.historial.append(historial(1,self.verPila(),self.cadena[0],"(p,λ,λ;q,"+str(self.gramatica.NTI)+")"))
            self.pila.append(self.gramatica.NTI)
            longitud=len(self.cadena)
            posicion=0
            while posicion<longitud:
                top=self.obtenerTop()
                if self.determinarTipo(self.obtenerTop())=="T":
                    if self.obtenerTop()==self.cadena[posicion]:
                        self.desapilar()
                        posicion+=1
                    else:
                        print("1 Cadena invalida")
                        posicion+=1
                elif self.determinarTipo(self.obtenerTop())=="NT":
                    if self.determinarProducciones(self.obtenerTop()) == 1:
                        self.apilar(self.obtenerExpresion(self.obtenerTop()))
                        print(self.obtenerTop())
                    
# empezar a trabajar acaaaa



            for i in self.historial:
                print(i)
        else:
            print("No se encuentra en el alfabeto")
    
    def verPila(self):
        reversa=self.pila.copy()
        reversa.reverse()
        txt=""
        for i in reversa:
            txt+=str(i)
        return txt

    def apilar(self, produccion):
        aux=produccion.split(" ")
        aux.reverse()
        for i in aux:
            self.pila.append(i)

    def desapilar(self):
        try:
            return self.pila.pop()
        except IndexError:
            return "vacio"
    
    def obtenerTop(self):
        try:
            return self.pila[len(self.pila)-1]
        except IndexError:
            return "vacio"
    
    def es_vacia(self):
        return self.pila == []
    
    def determinarTipo(self, evaluar):
        if evaluar in self.gramatica.T:
            return "T"
        elif evaluar in self.gramatica.NT:
            return "NT"
    
    def verificarAlfabeto(self, letra):
        alfabeto=self.gramatica.T
        if letra in alfabeto:
            return True
        else:
            return False
    
    def determinarProducciones(self, NT):
        cont=0
        for i in self.gramatica.P:
            if i.NoT == NT:
                cont+=1
        return cont
    
    def obtenerExpresion(self, NT):
        for i in self.gramatica.P:
            if i.NoT == NT:
                return i.expresiones