import platform
import os
import time

def clear():
    sistema = platform.system()
    if str(sistema)=="Windows":
        os.system("cls")
    else:
        os.system("clear")

def cargarArchivo():
    print()

def infoGramatica():
    print()

def generarAutomata():
    print()

def reporteRecorrido():
    print()

def reporteTabla():
    print()

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

pantallaPrincipal()