import os
from graphviz import Digraph

def generarReporteAP(gramatica):
    
    g = Digraph('G', filename='AP.gv')
    g.attr(rankdir='LR')
    g.attr('node',shape='none', label="")
    g.node('inicio')
    g.attr('node',shape='circle', fixedsize='true', width='0.7', label='i')
    g.attr('node', style='filled', fillcolor='#535c689f')
    g.node('i')
    g.attr('node',shape='circle', fixedsize='true', width='0.7', label='p')
    g.node('p')

    g.attr('node', style='filled', fillcolor='#535c689f')
    g.attr('node', shape='doublecircle', fixedsize='true', width='0.7', label='f')
    g.node('f')
    g.attr('node', shape='circle', fixedsize='true', width='1.2', style='filled', fillcolor='#535c689f', label='q')

    transicionPQ="λ,λ;"+str(gramatica.NTI)
    #print(transicionPQ)
    transicionQNT=""
    for i in gramatica.P:
        for j in i.expresiones:
            transicionQNT+="λ,"+str(i.NoT)+";"+str(j.replace(" ",""))+"\n"
            
    transicionQT=""
    terminales=gramatica.T.split(",")
    for i in terminales:
        transicionQT+=str(i)+","+str(i)+";λ\n"

    g.edge('inicio','i')
    g.edge('i','p', label='λ,λ;#')
    g.edge('p','q', label='λ,λ;'+str(gramatica.NTI))
    g.edge('q','q', label=transicionQNT)
    g.edge('q','f', label='λ,#;λ')
    g.edge('q','q', label=transicionQT, headport='s')
    # print(g.source)
    path=os.getcwd()+"/Reportes/img/AP_"+str(gramatica.nombre)
    g.render(path, view=False, format="png")
    generarhtml(gramatica.nombre, gramatica.T, gramatica.NT)

def generarhtml(nombre, terminales, noTerminales):
    txt='''
    <!DOCTYPE html>
    <html lang="es">
    <title>Automata de Pila</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap"
        rel="stylesheet">
    <style>
        .w3-lobster {
            font-family: "Lobster", Sans-serif;
        }

        .Asap-Condensed {
            font-family: 'Asap Condensed', sans-serif;
        }

        .Courgette {
            font-family: 'Courgette', cursive;
        }

        .Rokkitt {
            font-family: 'Rokkitt', serif;
            font-weight: 800;
        }
    </style>

    <body>
        <div class="w3-display-container" style="height: 700px;" >
            <div class="w3-display-middle" style="width: 1300px;">
                <div class="w3-card-4 w3-margin-bottom">
                    <header class="w3-container w3-black  w3-round-small">
                        <p class="w3-lobster w3-center" style="font-size: 30px;">AP_'''+str(nombre)+'''</p>
                    </header>
                    <div class="w3-container w3-middle Asap-Condensed">
                        <table class="w3-table w3-margin-top">
                            <tr>
                                <td style="width:40%; vertical-align: middle;" class="Courgette"><p style="font-size: 18px;"><b>Terminales</b> = { '''+str(terminales)+''' } <br> <b>Alfabeto de pila</b> = { '''+str(terminales)+str(",")+str(noTerminales)+''',# } <br> <b>Estados</b> = { i, p, q, f } <br> <b>Estado inicial</b> = { i } <br> <b>Estado de aceptación</b> = { f }</p></td>
                                <td style="width:60%;" class="w3-center w3-Asap-Condensed "><img src="'''+str(os.getcwd())+str("/Reportes/img/AP_")+str(nombre)+'''.png" alt="Imagen automáta"></td>
                            </tr>
                        </table>
                    </div>
                    <footer class="w3-container w3-black  w3-round-small">
                        <br>
                    </footer>
                </div>
            </div>
            <br>
        </div>
    </body>

    </html>
     '''
    path=os.getcwd()+"/Reportes/AP_"+str(nombre)+".html"
    arhcivo=open(path,'w', encoding='utf8')
    arhcivo.write(txt)
    arhcivo.close()
    os.startfile(path)


# generarReporteAP()