class TransicionNT:
    def __init__(self, desapila, apila):
        self.desapila=desapila
        self.apila=apila

    def __str__(self):
        txt=str(self.desapila)+" "+str(self.apila)
        return txt