from graphviz import Digraph

def generarReporteAP(gramatica):
    '''
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

    g.edge('inicio','i')
    g.edge('i','p', label='λ,λ,#')
    g.edge('p','q', label='λ,λ,S')
    g.edge('q','q', label='λ,S,A \nλ,A,aAa \nλ,A,B \nλ,B,bBb \nλ,B,C \nλ,C,zC \nλ,C,z')
    g.edge('q','f', label='λ,#,λ')
    g.edge('q','q', label='a,a,λ \nb,b,λ \nz,z,λ', headport='s')
    print(g.source)
    g.render('D://test-output/round-table.gv', view=True, format="png")
    '''
    transicionPQ="λ,λ,"+str(gramatica.NTI)
    print(transicionPQ)
    transicionQNT=""
    for i in gramatica.P:
        for j in i.expresiones:
            transicionQNT+="λ,"+str(i.NoT)+","+str(j.replace(" ",""))+"\n"
            
    transicionQT=""
    terminales=gramatica.T.split(",")
    for i in terminales:
        transicionQT+=str(i)+","+str(i)+",λ\n"
    # print(transicionQN)
    print(transicionQT)



# generarReporteAP()