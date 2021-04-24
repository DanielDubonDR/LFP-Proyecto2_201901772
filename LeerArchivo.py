from Clases.Gramatica import GRM, exp
from Funciones.RGNAdmitidas import reporte

def extraerGramaticas(ruta):
    archivo=open(ruta,'r', encoding='utf8')
    contenido=archivo.read()
    archivo.close()
    grupos=contenido.split("*")
    grupos.pop()
    gramaticas=[]
    gramaticasRegulares=[]
    for grupo in grupos:
        agregar=False
        lineas=grupo.lstrip().rstrip().split("\n")
        nombre=str(lineas[0])
        inf=lineas[1].split(";")
        NT=inf[0]
        T=inf[1]
        TI=inf[2]

        listaProducciones=[]

        for i in range(2,len(lineas)):
            produccion=lineas[i].split("->")
            Expresiones=produccion[1].lstrip().rstrip()
            if len(Expresiones.split()) > 2:
                agregar=True

        if agregar:
            for i in range(2,len(lineas)):
                listaAux=[]
                produccion=lineas[i].split("->")
                NoT=produccion[0]
                Expresiones=produccion[1].lstrip().rstrip()
                listaAux.append(Expresiones)
                if len(listaProducciones)==0:
                    listaProducciones.append(exp(NoT,listaAux))
                else:
                    encontrado=False
                    pos=None
                    for buscar in listaProducciones:
                        if buscar.NoT == NoT:
                            encontrado=True
                            pos=listaProducciones.index(buscar)
                            #print(pos)
                            break

                    if encontrado:
                        listaProducciones[pos].expresiones.append(Expresiones)
                    else:
                        listaProducciones.append(exp(NoT,listaAux))
            gramaticas.append(GRM(nombre,NT,T,TI,listaProducciones))
        
            '''
            for x in gramaticas:
                print(x)
                for xx in x.P:
                    print(xx)
                print()
            '''
        else:
            regular2=False
            regular1=False
            for i in range(2,len(lineas)):
                produccion=lineas[i].split("->")
                Expresiones=produccion[1].lstrip().rstrip()
                analizarExpresion=Expresiones.split()
                if len(analizarExpresion)==2:
                    if verficarTerminal(T,analizarExpresion[0]) and verficarNTerminal(NT,analizarExpresion[1]):
                        regular2=False
                    elif verficarNTerminal(NT,analizarExpresion[0]) and verficarTerminal(T,analizarExpresion[1]):
                        regular2=False
                    else:
                        regular2=True
                        break
                elif len(analizarExpresion)==1:
                    if verficarTerminal(T,analizarExpresion[0]):
                        regular1=False
                    else:
                        regular2=True
                        break
            if regular2==False and regular1==False:
                for i in range(2,len(lineas)):
                    listaAux=[]
                    produccion=lineas[i].split("->")
                    NoT=produccion[0]
                    Expresiones=produccion[1].lstrip().rstrip()
                    listaAux.append(Expresiones)
                    if len(listaProducciones)==0:
                        listaProducciones.append(exp(NoT,listaAux))
                    else:
                        encontrado=False
                        pos=None
                        for buscar in listaProducciones:
                            if buscar.NoT == NoT:
                                encontrado=True
                                pos=listaProducciones.index(buscar)
                                #print(pos)
                                break

                        if encontrado:
                            listaProducciones[pos].expresiones.append(Expresiones)
                        else:
                            listaProducciones.append(exp(NoT,listaAux))
                gramaticasRegulares.append(GRM(nombre,NT,T,TI,listaProducciones))

            else:
                for i in range(2,len(lineas)):
                    listaAux=[]
                    produccion=lineas[i].split("->")
                    NoT=produccion[0]
                    Expresiones=produccion[1].lstrip().rstrip()
                    listaAux.append(Expresiones)
                    if len(listaProducciones)==0:
                        listaProducciones.append(exp(NoT,listaAux))
                    else:
                        encontrado=False
                        pos=None
                        for buscar in listaProducciones:
                            if buscar.NoT == NoT:
                                encontrado=True
                                pos=listaProducciones.index(buscar)
                                #print(pos)
                                break

                        if encontrado:
                            listaProducciones[pos].expresiones.append(Expresiones)
                        else:
                            listaProducciones.append(exp(NoT,listaAux))
                gramaticas.append(GRM(nombre,NT,T,TI,listaProducciones))
    '''
    for x in gramaticas:
        print(x)
        for xx in x.P:
            print(xx)
        print()
    '''
    # if len(gramaticasRegulares)!=0:
    #     reporte(gramaticasRegulares)

    return gramaticas
                
def verficarTerminal(lista, T):
    verificar=False
    for x in lista:
        if T==x:
            verificar=True
    return verificar

def verficarNTerminal(lista, NT):
    verificar=False
    for x in lista:
        if NT==x:
            verificar=True
    return verificar


# extraerGramaticas("Archivos_Prueba/entrada.glc")