class GRM:
    def __init__(self, nombre, NT, T, NTI, P):
        self.nombre=nombre
        self.NT=NT
        self.T=T
        self.NTI=NTI
        self.P=P

    def __str__(self):
        string="- Nombre de la gramática tipo 2: "+str(self.nombre)+"\n- No Terminales: = { "+str(self.NT)+" }\n- Terminales = { "+str(self.T)+" }\n- No Terminal Inicial = "+str(self.NTI)+"\n- Producciones: \n"
        return string
    
class exp:
    def __init__(self, NoT, expresiones):
        self.NoT=NoT
        self.expresiones=expresiones

    def __str__(self):
        string="    "+str(self.NoT)+str(" -> ")
        for i in range(len(self.expresiones)):
            if i!= len(self.expresiones)-1:
                string+=str(self.expresiones[i])+"\n       | "
            else:
                string+=str(self.expresiones[i])
        return string