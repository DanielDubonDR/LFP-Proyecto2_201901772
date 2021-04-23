class GRM:
    def __init__(self, nombre, NT, T, NTI, P):
        self.nombre=nombre
        self.NT=NT
        self.T=T
        self.NTI=NTI
        self.P=P

    def __str__(self):
        string="Nombre: "+str(self.nombre)+"\nNo Terminales: "+str(self.NT)+"\nTerminales: "+str(self.T)+"\nNo Terminal Inicial: "+str(self.NTI)+"\nProducciones: "+str(self.P)
        return string
    
class exp:
    def __init__(self, NoT, expresiones):
        self.NoT=NoT
        self.expresiones=expresiones

    def __str__(self):
        string=str(self.NoT)+str(" ")+str(self.expresiones)
        return string