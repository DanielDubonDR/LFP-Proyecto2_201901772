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
        for i in self.transionesNTerminales:
            print(i)

    def verificar(self):
        if self.verificarAlfabeto(self.cadena[0]):
            self.historial.append(historial(0,"",self.cadena[0],"(i,λ,λ;p,#)"))
            self.pila.append("#")
            self.historial.append(historial(1,self.verPila(),self.cadena[0],"(p,λ,λ;q,"+str(self.gramatica.NTI)+")"))
            self.pila.append(self.gramatica.NTI)
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

    def desapilar(self):
        try:
            return self.pila.pop()
        except IndexError:
            return "vacio"
    
    def es_vacia(self):
        return self.pila == []
    
    def verificarAlfabeto(self, letra):
        alfabeto=self.gramatica.T
        if letra in alfabeto:
            return True
        else:
            return False