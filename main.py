from tkinter import Tk
from tkinter.filedialog import askopenfilename
import platform
import os
import time
from  LeerArchivo import extraerGramaticas
from Funciones.GraficarAP import generarReporteAP
from Funciones.ValidarCadena import validar
Tk().withdraw()

#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
ruta=""
gramaticas=None
AP=[]

def clear():
    sistema = platform.system()
    if str(sistema)=="Windows":
        os.system("cls")
    else:
        os.system("clear")

def cargarArchivo():
    clear()
    global ruta
    print("\n------------------------------------ CARGAR ARCHIVO ------------------------------------\n")
    try:
        ruta = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.glc*"), ("all files", "*.*")))
        if ruta=="":
            print(" > ERROR: No se seleccionó ningún archivo")
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
        else:
            print(" > Archivo cargado")
            global gramaticas
            gramaticas=extraerGramaticas(ruta)
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
    except:
        print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def infoGramatica():
    if ruta!="":
        z=len(gramaticas)+1
        opcion=0
        while opcion!=z:
            clear()
            cont=0
            String=""
            print("\n---------------------------------- SELECCIONAR GRAMÁTICA ---------------------------------")
            for i in gramaticas:
                cont+=1
                String+=str("\n ")+str(cont)+str(". ")+str(i.nombre)
            print(String)
            print(" "+str(cont+1)+". Regresar\n")
            try:
                opcion=int(input("- Ingrese una opción:\n  > "))
                if opcion>z or opcion<1:
                    print("\n > Opción inválida...")
                    input(" - PRESIONE ENTER PARA CONTINUAR...")
                else:
                    if opcion!=z:
                        clear()
                        print("\n------------------------------- INFORMACIÓN DE LA GRAMÁTICA ------------------------------\n")
                        print(gramaticas[opcion-1])
                        for j in gramaticas[opcion-1].P:
                            print(j)
                        input("\n - PRESIONE ENTER PARA CONTINUAR...")
            except:
                print("\n > Opción inválida...")
                input(" - PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado o procesado ningún archivo ")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")


def generarAutomata():
    if ruta!="":
        z=len(gramaticas)+1
        opcion=0
        while opcion!=z:
            clear()
            cont=0
            String=""
            print("\n---------------------------------- SELECCIONAR GRAMÁTICA ---------------------------------")
            for i in gramaticas:
                cont+=1
                String+=str("\n ")+str(cont)+str(". ")+str(i.nombre)
            print(String)
            print(" "+str(cont+1)+". Regresar\n")
            try:
                opcion=int(input("- Ingrese una opción:\n  > "))
                if opcion>z or opcion<1:
                    print("\n > Opción inválida...")
                    input(" - PRESIONE ENTER PARA CONTINUAR...")
                else:
                    if opcion!=z:
                        clear()
                        print("\n--------------------------------- GENERAR AUTOMÁTA DE PILA -------------------------------\n")
                        generarReporteAP(gramaticas[opcion-1]) 
                        AP.append(gramaticas[opcion-1].nombre)
                        print("  > Automáta de pila generado")
                        input("\n - PRESIONE ENTER PARA CONTINUAR...")
            except:
                print("\n > Opción inválida...")
                input(" - PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado o procesado ningún archivo ")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def reporteRecorrido():
    print()

def obtenerG(opcion):
    for i in gramaticas:
        if i.nombre == AP[opcion]:
            return i

def reporteTabla():
    if ruta!="":
        if len(AP)!=0:
            z=len(AP)+1
            opcion=0
            while opcion!=z:
                clear()
                cont=0
                String=""
                print("\n------------------------------ SELECCIONAR AUTOMÁTA DE PILA ------------------------------")
                for i in AP:
                    cont+=1
                    String+=str("\n ")+str(cont)+str(". AP_")+str(i)
                print(String)
                print(" "+str(cont+1)+". Regresar\n")
                try:
                    opcion=int(input("- Ingrese una opción:\n  > "))
                    if opcion>z or opcion<1:
                        print("\n > Opción inválida...")
                        input(" - PRESIONE ENTER PARA CONTINUAR...")
                    else:
                        if opcion!=z:
                            clear()
                            print("\n------------------------------------- VERIFICAR CADENA -----------------------------------\n")
                            cadena=str(input("  Ingrese la cadena a validar:\n    > "))
                            verificar=validar(obtenerG(opcion-1), cadena)
                            print("\n  > Reporte generado")
                            input("\n - PRESIONE ENTER PARA CONTINUAR...")
                except:
                    print("\n > Opción inválida...")
                    input(" - PRESIONE ENTER PARA CONTINUAR...")
        else:
            clear()
            print("\n------------------------------ SELECCIONAR AUTOMÁTA DE PILA ------------------------------")
            print("\n  > ERROR: No se ha generado ningún automáta de pila ")
            input("  - PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado o procesado ningún archivo ")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def salir():
    print("  > Saliendo...\n")

def pantallaPrincipal():
    for i in range(5,0,-1):
        clear()
        print("   _____________________________________________________________________________ ")
        print("  |                                                                             |")
        print("  |                PROCESADOR Y GENERADOR DE AUTÓMATAS DE PILA                  |")
        print("  |                                                                             |")
        print("  |   - Curso: Lenguajes Formales y de Programación       ~ Sección: B+         |")
        print("  |   - Nombre: Daniel Reginaldo Dubón Rodríguez          ~ Carné: 201901772    |")
        print("  |   - Carrera: Ingeniería en Ciencias y Sistemas                              |")
        print("  |_____________________________________________________________________________|")
        print("\n   > Espere por favor: "+str(i))
        time.sleep(1)

    for i in range(2,0,-1):
        clear()
        print("   _____________________________________________________________________________ ")
        print("  |                                                                             |")
        print("  |                                                                             |")
        print("  |                                BIENVENIDO                                   |")
        print("  |                                                                             |")
        print("  |_____________________________________________________________________________|")
        time.sleep(1)
    
    clear()
    menu()

def menu():
    opcion=0
    while opcion!=6:
        clear()
        print("\n------------------------------------ MENÚ PRINCIPAL ------------------------------------\n")
        print("   1. Cargar archivo")
        print("   2. Mostrar información general de la gramática")
        print("   3. Generar autómata de pila equivalente")
        print("   4. Reporte de recorrido")
        print("   5. Reporte en tabla")
        print("   6. Salir\n")
        opcion=int(input("- Ingrese una opción:\n  > "))
        switch={1:cargarArchivo, 2:infoGramatica, 3:generarAutomata, 4:reporteRecorrido, 5:reporteTabla, 6:salir}
        func=switch.get(opcion,"Opción inválida")
        try:
            func()
        except:
            print("\n > Opción inválida...")
            input(" - PRESIONE ENTER PARA CONTINUAR...")

menu()