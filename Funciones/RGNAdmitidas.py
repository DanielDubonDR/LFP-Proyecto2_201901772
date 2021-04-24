import os
txt=""
def reporte(lista):
    global txt
    txt='''
        <!DOCTYPE html>
        <html>
            <title>Menu</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap" rel="stylesheet">
            <style>
                .w3-lobster
                {
                    font-family: "Lobster", Sans-serif;
                }
                .w3-Asap-Condensed
                {
                    font-family: 'Asap Condensed', sans-serif;
                }
                .w3-Courgette
                {
                    font-family: 'Courgette', cursive;
                }
                .w3-Rokkitt
                {
                    font-family: 'Rokkitt', serif;
                    font-weight: 800;
                }
            </style>
            <body>
                <div class="w3-container w3-teal w3-center w3-margin-bottom">
                    <br>
                    <h1 class="w3-lobster" style="font-size: 60px;">Gramáticas Regulares</h1>
                    <h3 class="w3-Courgette" style="font-size: 20px;">Gramáticas no cargadas por no ser exclusivamente gramáticas libres de contexto</h3>
                    <br>
                </div>
    '''
    for i in lista:
        txt+='''
            <table class="w3-table w3-margin-top">
                    <tr>
                        <td style="width:25%;" class=" w3-Courgette"></td>
                        <td style="width:50%;" class=" w3-Courgette">
                            <div class="w3-container  w3-margin-bottom">
                                <div class="w3-card-4 w3-margin-bottom">
                                    <header class="w3-container w3-deep-purple  w3-round-small w3-center">
                                        <h1 class="w3-Rokkitt">'''+str(i.nombre)+'''</h1>
                                    </header>
                                    <div class="w3-container w3-middle Asap-Condensed">
                                        <p style="font-size: 18px;"><b>No Terminales</b> = { '''+str(i.NT)+''' } <br> <b>Terminales</b> = {'''+str(i.T)+''' } <br> <b>No Terminal Inicial</b> = '''+str(i.NTI)+''' <br> <b>Producciones:</b></p>
        '''
        for x in i.P:
            txt+="<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"+str(x.NoT)+str(" -> ")
            for j in range(len(x.expresiones)):
                if j!= len(x.expresiones)-1:
                    txt+=str(x.expresiones[j])+"<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|&nbsp"
                else:
                    txt+=str(x.expresiones[j])
        txt+='''
                                    </div>
                                    <footer class="w3-container w3-deep-purple w3-round-small"><br></footer>
                                </div>
                            <br>
                            </div>
                        </td>
                        <td style="width:25%;" class=" w3-Courgette"></td>
                    </tr>
                </table>
         '''

    txt+='''
        </body>
    </html>
    '''
    crearArchivo()

def crearArchivo():
    path=os.getcwd()+"/Reportes/GRMR.html"
    arhcivo=open(path,'w', encoding='utf8')
    arhcivo.write(txt)
    arhcivo.close()
    os.startfile(path)
