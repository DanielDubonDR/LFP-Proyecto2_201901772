import os
txt=""
def reporte(lista, cadena, acpetada):
    global txt
    txt='''
        <!DOCTYPE html>
        <html>
        <title>Reporte Tabla</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <style>
        .w3-lobster {
            font-family: "Lobster", serif;
        }
        </style>

        <body>
        <div class="w3-container w3-teal w3-center w3-margin-bottom">
            <br><br>
            <h1 class="w3-lobster w3-xxxlarge">Reporte en Tabla</h1>
            <br><br>
        </div>
        <div class="w3-container w3-lobster w3-center">
            <p class="w3-xxxlarge">Cadena: '''+str(cadena)+'''<p>
        </div>
        <div class="w3-container w3-center">
            <div class="w3-container w3-lobster">
            </div>
            <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
            <tr class="w3-black">
                <th style="width:15%;" class="w3-center" style="vertical-align: middle;">Iteración</th>
                <th style="width:35%;" class="w3-center">Pila <br> <i class="material-icons">arrow_back</i></th>
                <th style="width:15%;" class="w3-center" style="vertical-align: middle;">Entrada</th>
                <th style="width:35%;" class="w3-center" style="vertical-align: middle;">Transiciones</th>
            </tr>
    '''
    for i in lista:
        txt+='''
            <tr>
                <td class="w3-center"><b>'''+str(i.iteracion)+'''</b></td>
                <td style="text-align: right;">'''+str(i.pila)+'''</td>
                <td class="w3-center">'''+str(i.entrada)+'''</td>
                <td class="w3-center">'''+str(i.transicion)+'''</td>
            </tr>
        '''

    txt+='''
            </table>
        <div class="w3-container w3-lobster w3-center">
        <p class="w3-xxxlarge">'''+str(acpetada)+'''<p>
        </div>
    </div><br><br>
    
    </body>

    </html>
    '''
    crearArchivo()

def crearArchivo():
    path=os.getcwd()+"/Reportes/ReporteTabla.html"
    arhcivo=open(path,'w', encoding='utf8')
    arhcivo.write(txt)
    arhcivo.close()
    os.startfile(path)