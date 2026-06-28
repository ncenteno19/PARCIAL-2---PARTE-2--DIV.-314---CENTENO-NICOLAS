from Funciones import *


def mostrar_diccionario(diccionario:dict) -> None:
    """
    Muestra en pantalla las claves y valores de un diccionario.
    Args:
    diccionario (dict): Diccionario a mostrar.
    Returns:
    None
    """

    
    for clave in diccionario:
        print(f"{formatear_clave(clave)} : {diccionario[clave]}")
    print("────────────────────────────────")

def mostrar_lista_diccionarios(lista_diccionarios:list) -> None:
    """
    Muestra en pantalla las claves y valores de un diccionario.
    Args:
    diccionario (dict): Diccionario a mostrar.
    Returns:
    None
    """
    print("────────────────────────────────")
    for i in range(len(lista_diccionarios)):
        mostrar_diccionario(lista_diccionarios[i])
        
def mostrar_egresados_por_plan(lista_alumnos: list, mensaje: str = "Ingrese el Plan a buscar: ",
                               mensaje_error: str = "❌ No se encontraron alumnos") -> None:
    
    """
    Muestra los alumnos egresados de un plan específico.
    Solicita al usuario el plan de estudios y recorre la lista de alumnos,
    mostrando aquellos que coinciden con el plan ingresado. Si no se
    encuentran resultados, informa al usuario.

    Args:
    lista_alumnos (list): Lista de diccionarios con los datos de los alumnos.
    mensaje (str): Texto para solicitar el ingreso del plan.
    mensaje_error (str): Mensaje a mostrar si no se encuentran alumnos.

    Returns:
    None
    """

    print("***  EGRESADOS POR PLAN ***\n")

    print("────────────────────────────────")
    
    plan = validar_plan(mensaje)
    print("")

    hay_alumno = False

    for i in range (len(lista_alumnos)):
        if lista_alumnos[i]["plan"] == plan:
            hay_alumno = True
            mostrar_diccionario(lista_alumnos[i])
    
    if hay_alumno == False:
        print(mensaje_error)

def mostrar_egresos_menor_2000(lista_alumnos: list,
                               mensaje_error: str = "❌ No se encontraron alumnos") -> None:
    
    """
    Muestra los alumnos egresados antes del año 2000.
    Recorre la lista de alumnos y muestra aquellos cuyo año de egreso
    sea menor a 2000. Además, calcula y muestra el promedio general
    de las notas de los alumnos encontrados. Si no hay resultados,
    informa al usuario.

    Args:
    lista_alumnos (list): Lista de diccionarios con los datos de los alumnos.
    mensaje_error (str): Mensaje a mostrar si no se encuentran alumnos.

    Returns:
    None
    """

    print("***  EGRESADOS ANTERIORES AL 2000 ***\n")
    print("────────────────────────────────")
    print("")

    hay_alumno = False
    suma_promedio = 0
    contador = 0

    for i in range (len(lista_alumnos)):
        if lista_alumnos[i]["egreso"] < 2000:
            hay_alumno = True
            suma_promedio += lista_alumnos[i]["nota_promedio"]
            contador += 1
            mostrar_diccionario(lista_alumnos[i])
    
    if hay_alumno == False:
        print(mensaje_error)
    else:
        print(f"El promedio de las notas es: {calcular_promedio(suma_promedio,contador):.2f}")

def buscar_alumno_avanzado(lista_alumnos: list,
                               mensaje_error: str = "❌ No se encontraron alumnos") -> None:
    
    """
    Busca alumnos por nombre o apellido de forma parcial.
    Solicita una cadena de al menos 3 caracteres y compara con los nombres
    y apellidos de los alumnos, permitiendo coincidencias parciales desde
    el inicio. Muestra todos los resultados encontrados y la cantidad.

    Args:
    lista_alumnos (list): Lista de diccionarios con los datos de los alumnos.
    mensaje_error (str): Mensaje a mostrar si no se encuentran coincidencias.

    Returns:
    None
    """

    print("***  BUSCAR ALUMNO (AVANZADO) ***\n")
    print("─────────────────────────────────────────")

    a_buscar = convertir_titulo(ingresar_nombre("Ingrese el nombre o apellido a buscar: "))

    print("─────────────────────────────────────────")

    hay_alumno = False
    contador_alumno = 0

    for i in range (len(lista_alumnos)):
        contador_nombre = 0
        contador_apellido = 0
        
        nombre = lista_alumnos[i]["nombre"]
        apellido = lista_alumnos[i]["apellido"]

        if len(a_buscar) <= len(nombre):

            for j in range (len(a_buscar)):
                if nombre[j] == a_buscar[j]:
                    contador_nombre += 1

        if len(a_buscar) <= len(apellido):

            for k in range (len(a_buscar)):
                if apellido[k] == a_buscar[k]:
                    contador_apellido += 1 
        
        if (
            contador_nombre == len(a_buscar) or 
            contador_apellido == len(a_buscar)
            ):
           hay_alumno = True
           contador_alumno += 1
           mostrar_diccionario(lista_alumnos[i])


    if hay_alumno == False:
        print(mensaje_error)
    else:
        print(f"Se encontraron {contador_alumno} alumnos")
   
def mostrar_alumnos_por_promedio(lista_alumnos: list, nota: float = 9, 
                            mensaje_error: str = "❌ No se encontraron alumnos") -> None:

    """
    Muestra los alumnos con nota promedio mayor o igual a un valor dado.
    Ordena la lista de alumnos de mayor a menor según la nota promedio
    y muestra aquellos que cumplen con el mínimo indicado. Si no se
    encuentran resultados, informa al usuario.

    Args:
    lista_alumnos (list): Lista de diccionarios con los alumnos.
    nota (float): Nota mínima para mostrar alumnos (por defecto 9).
    mensaje_error (str): Mensaje a mostrar si no hay resultados.

    Returns:
    None
    """

    print("***  SALÓN DE LA FAMA ***\n")
    print("─────────────────────────────────────────")

    ordenar_alumno_clave(lista_alumnos, "nota_promedio")

    hay_alumno = False

    for i in range(len(lista_alumnos)):
        if lista_alumnos[i].get("nota_promedio") >= nota:
            hay_alumno = True
            mostrar_diccionario(lista_alumnos[i])

    if hay_alumno == False:
        print(mensaje_error)

















