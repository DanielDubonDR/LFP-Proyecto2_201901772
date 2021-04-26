from graphviz import Digraph

g = Digraph('G', filename='AP.gv')
g.attr(rankdir='LR')
g.attr('node',shape='circle', fixedsize='true', width='0.5')
g.node('i')
g.node('p')
texto="Terminales = { a,b,z }\lAlfabeto de pila = { a,b,z,S,A,C,# }\lEstados = { i,p,q,f } \lEstado inicial = {i} \lEstado de aceptacion = { f }\l"
# g.attr('node',shape='plaintext', fontsize='15',  label=texto, width='3')
# g.node('txt')
g.attr('node',shape='none', label="")
g.node('inicio')
g.attr('node', shape='doublecircle', fixedsize='true', width='0.5', label='f')
g.node('f')
# g.attr('node', shape='plaintext',  label='Nombre: AP_Grm1\n ', width='3', fontsize='20')
# g.node('title')
g.attr('node', shape='circle', fixedsize='true', width='1', style='filled', fillcolor='#00ff005f', label='q')

g.edge('inicio','i')
g.edge('i','p', label='λ,λ,#')
g.edge('p','q', label='λ,λ,S')
g.edge('q','q', label='λ,S,A \nλ,A,aAa \nλ,A,B \nλ,B,bBb \nλ,B,C \nλ,C,zC \nλ,C,z')
g.edge('q','f', label='λ,#,λ')
g.edge('q','q', label='a,a,λ \nb,b,λ \nz,z,λ', headport='s')
print(g.source)
g.render('D://test-output/round-table.gv', view=True, format="png")




'''
digraph G {
    rankdir=LR

    node [shape=circle,fixedsize=true,width=0.5];  i; p;
    node[shape=plaintext, fontsize=15,  label="Terminales = { a,b,z }\lAlfabeto de pila = { a,b,z,S,A,C,# }\lEstados = { i,p,q,f } \lEstado inicial = {i} \lEstado de aceptacion = { f }\l", width=3 ]; texto;
    node[shape=none, label=""]; inicio;
    node [shape=doublecircle,fixedsize=true,width=0.5, label="f"]; f;
    node[shape=plaintext,  label="Nombre: AP_Grm1\n ", width=3, fontsize=20]; title;
    node [shape=circle,fixedsize=true,width=1, style=filled, fillcolor="#00ff005f", label="q"];  q;
    
    inicio->i;
    edge[label = "λ,λ,#"];
    i -> p
    edge[label = "λ,λ,S"];
    p -> q
    edge[label = "E\nF"];
    q -> q
    edge[label = "λ,#,λ"];
    q -> f
    edge[label = "G\nH" headport="s"];
    q -> q
    
}
'''