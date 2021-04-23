from Clases.Gramatica import GRM, exp

def extraerGramaticas(ruta):
    archivo=open(ruta,'r', encoding='utf8')
    contenido=archivo.read()
    archivo.close()
    grupos=contenido.split("*")
    grupos.pop()
    for grupo in grupos:
        agregar=None
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
            for xd in listaProducciones:
                print(xd)
            print()
            

extraerGramaticas("Archivos_Prueba/entrada.glc")