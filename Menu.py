from Funciones import *
from Inputs import *
from Prints import *

def mostrar_menu()-> None:

    opcion = -1
    
    carga_manual = False
    hay_alumnos = False   

    while opcion != 6:
        limpiar_consola()
        print("═════════ UTN FRA - Egresados Tec. Univ. en Programación ═════════")
        print("1. Cargar Alumnos")
        print("2. Mostrar Egresados por plan")
        print("3. Mostrar egresados anteriores al año 2000")
        print("4. Buscar alumno por nombre o apellido (avanzado)")
        print("5. Salón de la fama")
        print("6. Salir")
        print("══════════════════════════════════════════════════════════════════")

        opcion = ingresar_numero("Ingrese una opción: ")

        if (opcion > 1 and opcion < 6) and hay_alumnos == False:
            print("⚠️  Los datos no fueron cargados")
            esperar_enter()

        else:    
            match opcion:
                case 1:
                    limpiar_consola()
                    lista_alumnos = []
                    carga_manual = sub_menu_carga(lista_alumnos)

                    if lista_alumnos != None:
                        hay_alumnos = True

                case 2:
                    limpiar_consola()
                    mostrar_alumnos_nota_menor_a(matriz_notas,7)
                    esperar_enter()
                case 3:
                    limpiar_consola()
                    mostrar_alumnos_nota_menor_a(matriz_notas,4)
                    esperar_enter()
                case 4:
                    limpiar_consola()
                    mostrar_porcentaje(matriz_notas)
                    esperar_enter()  
                case 5:
                    limpiar_consola()
                    mostrar_mejor_trimestre(matriz_notas)
                    esperar_enter()

                case 6:
                    if carga_manual == True:
                        guardar_csv_matriz(nombre_archivo_csv(),matriz_notas)
                    print("Hasta luego!! ✌️")
                case _:
                    print("❌  Opción Inválida. Vuelva a intentarlo")
                    esperar_enter()


def sub_menu_carga(lista_alumnos: list)-> bool:
    
    carga_manual = False
    opcion = -1
  
    while opcion != 3:
        limpiar_consola()
        print("📝  *** CARGA DE DATOS*** 📝")
        print("1. Carga desde Archivo JSON")
        print("2. Carga manual")
        print("3. Volver al Menú Principal")
        print("════════════════════════════════")

        opcion = ingresar_numero("Ingrese una opción: ", "❌ Error. Los datos ingresados no son válidos.")

        match opcion:
                   
                case 1:
                    limpiar_consola()
                    print("📂  *** CARGA DESDE ARCHIVO JSON*** 📂")
                    cargar_json("alumnos.json",lista_alumnos)
                    mostrar_lista_diccionarios(lista_alumnos)
                
                    carga_manual = False
                    esperar_enter()

                case 2:
                    limpiar_consola()
                    print("📝  *** CARGA MANUSL*** 📝")
                    cargar_alumno(lista_alumnos)
                    mostrar_lista_diccionarios(lista_alumnos)
                    carga_manual = True
                    esperar_enter()

                case 3:
                    limpiar_consola()

                case _:
                    print("❌  Opción Inválida. Vuelva a intentarlo")
                    esperar_enter()
    
    return carga_manual

    