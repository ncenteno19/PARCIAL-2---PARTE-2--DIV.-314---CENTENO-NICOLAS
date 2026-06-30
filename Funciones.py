import subprocess
import datetime as dt
import random
import os

from Archivos import *
from Inputs import *

def limpiar_consola():
    """
    Función que limpia consola vista en clase
    """
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def esperar_enter() -> None:
    """
    Función para esperar un Enter para continuar vista en clase
    """
    print("")
    input("Ingresá ENTER para Volver al Menú...")

def cargar_json(nombre_archivo:str,lista_alumnos:list) -> bool:

    """
    Carga una lista de alumnos desde un archivo JSON.
    Lee el archivo JSON y agrega cada diccionario a la lista recibida.
    Args:
    nombre_archivo (str): Nombre o ruta del archivo JSON.
    lista_alumnos (list): Lista donde se cargarán los alumnos.
    Returns:
    bool: True si la carga fue correcta, False en caso contrario.
    """

    if type(nombre_archivo) == str and type(lista_alumnos) == list:
        retorno = True
        
        lista_json = leer_json(nombre_archivo)

        if validar_json(lista_json):

            for i in range(len(lista_json)):
                lista_alumnos.append(lista_json[i])
        else:
            print("❌ Error en los datos del archivo")
            retorno = False
       
    else:
        retorno = False

    return retorno


def validar_json(lista_json: list) -> bool:

    """
    Valida que la estructura de los datos cargados desde un archivo JSON sea correcta.
    Verifica que el contenido no sea None, que sea una lista y que contenga elementos.
    Luego recorre cada elemento asegurando que sea un diccionario y que tenga
    las claves esperadas con los tipos de datos correctos.

    Args:
    lista_json (list): Datos obtenidos desde el archivo JSON.

    Returns:
    bool: True si la estructura y los datos son válidos, False en caso contrario.
    """

    if (
        lista_json != None and
        type(lista_json) == list and 
        len(lista_json) > 0 
        ):
        
        for i in range (len(lista_json)):

            if type(lista_json[i]) != dict:              
                return False

            if not (
                type(lista_json[i].get("legajo")) == int and
                type(lista_json[i].get("nombre")) == str and
                type(lista_json[i].get("apellido")) == str and
                type(lista_json[i].get("egreso")) == int and
                type(lista_json[i].get("plan")) == int and
                type(lista_json[i].get("nota_promedio")) == float 
            ):
                return False
            
        return True
    
    else:
        return False
    


def formatear_clave(clave:str) -> str:
    """
    Formatea una clave para su visualización.
    Reemplaza guiones bajos por espacios y convierte el texto a formato título.
    Args:
    clave (str): Clave a formatear.
    Returns:
    str: Clave formateada.
    """

    clave = reemplazar_caracteres(clave,"_"," ")
    clave = convertir_titulo(clave)

    return clave

def reemplazar_caracteres(cadena_original:str,caracter_viejo:str,caracter_nuevo:str) -> str:
    
    """
    Reemplaza o elimina un carácter en una cadena.

    Recorre la cadena carácter por carácter y reemplaza todas las
    ocurrencias de un carácter por otro. Permite también eliminar
    caracteres si el carácter nuevo es una cadena vacía.

    Args:
        cadena_original (str): Cadena a procesar.
        caracter_viejo (str): Carácter a reemplazar (debe ser de longitud 1).
        caracter_nuevo (str): Carácter de reemplazo o cadena vacía para eliminar.

    Returns:
        str: Nueva cadena con los caracteres reemplazados.
    """

    cadena_nueva = ""
    
    if (
            type(cadena_original) != str
            or type(caracter_viejo) != str
            or type(caracter_nuevo) != str
            or len(caracter_viejo) != 1
            or len(caracter_nuevo) > 1
        ):
            print("❌ Error en los parámetros")
            return cadena_nueva
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == caracter_viejo:
            cadena_nueva += caracter_nuevo
        else:
            cadena_nueva += cadena_original[i]
            
    return cadena_nueva

def convertir_titulo(cadena_original:str) -> str:
    """
    Convierte una cadena a formato título.

    Convierte toda la cadena a minúsculas y luego transforma
    en mayúscula la primera letra de cada palabra.

    Args:
    cadena_original (str): Cadena a transformar.

    Returns:
    str: Cadena en formato título.

    """
    cadena_original = convertir_minuscula(cadena_original)
    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter = cadena_original[i]
        if i == 0 or cadena_original[i-1] == " ":
            caracter = convertir_mayuscula(caracter)
        cadena_copia += caracter

    return cadena_copia

def convertir_mayuscula(cadena_original:str) -> str:
    
    """
    Convierte los caracteres minúsculos de una cadena a mayúscula
    utilizando códigos ASCII.

    Args:
    cadena_original (str): Cadena a convertir.

    Returns:
    str: Cadena con letras en mayúscula.
    """

    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter = cadena_original[i]
        caracter_ascii = ord(caracter)
        if caracter_ascii >= 97 and caracter_ascii <= 122:
            caracter_ascii -= 32
            caracter = chr(caracter_ascii)
        
        cadena_copia += caracter

    return cadena_copia

def convertir_minuscula(cadena_original:str) -> str:

    """
    Convierte los caracteres mayúsculos de una cadena a minúscula
    utilizando códigos ASCII.

    Args:
    cadena_original (str): Cadena a convertir.

    Returns:
    str: Cadena con letras en minúscula.
    """

    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter = cadena_original[i]
        caracter_ascii = ord(caracter)
        if caracter_ascii >= 65 and caracter_ascii <= 90:
            caracter_ascii += 32
            caracter = chr(caracter_ascii)
        
        cadena_copia += caracter

    return cadena_copia

def cargar_alumno(lista_alumnos: list) -> bool:
    if type(lista_alumnos) == list:
        retorno = True
        alumno = {}

        alumno["legajo"] = ingresar_legajo(lista_alumnos)
        alumno["nombre"] = convertir_titulo(ingresar_nombre("Nombre: "))
        alumno["apellido"] = convertir_titulo(ingresar_nombre("Apellido: "))
        alumno["egreso"] = validar_numero("Año de Egreso: ", 1991, 2026)
        alumno["plan"] = validar_plan()
        alumno["nota_promedio"] = float(validar_numero("Promedio: ", 6, 10))

        if confirmar_carga_alumno():
            lista_alumnos.append(alumno)
         
    else:
        retorno = False

    return retorno

def ingresar_legajo (lista_alumnos: list) -> int:
    
    """
    Genera un legajo único de 6 cifras para un alumno.

    Si la lista de alumnos está vacía, genera directamente un legajo.
    En caso contrario, crea un número aleatorio y verifica que no exista
    en la lista, repitiendo el proceso hasta encontrar uno único.

    Args:
        lista_alumnos (list): Lista de diccionarios con los alumnos cargados.

    Returns:
        int: Legajo único de 6 cifras.
    """
    
    if len(lista_alumnos) > 0:
        while True:
            legajo = random.randint(100000, 999999)
            repetido = False

            for i in range (len(lista_alumnos)):
                if lista_alumnos[i]["legajo"] == legajo:
                    repetido = True
                    break
            
            if repetido == False:
                return legajo
    else:
         legajo = random.randint(100000, 999999)
         return legajo
                
def calcular_promedio(suma_total: int | float, cantidad_elementos: int,
                      mensaje_error: str = "❌ División por 0") -> float:
    
    """
    Calcula el promedio a partir de una suma total y una cantidad de elementos.

    Verifica que la cantidad sea distinta de cero para evitar errores
    de división. En caso contrario, muestra un mensaje de error.

    Args:
        suma_total (int | float): Suma total de los valores.
        cantidad (int): Cantidad de elementos utilizados para el cálculo.
        mensaje_error (str): Mensaje a mostrar si la cantidad es cero.

    Returns:
        float: Promedio calculado o None si no es posible realizar la operación.
    """

    if cantidad_elementos == 0:
        print(mensaje_error)
    else:
        return  suma_total/ cantidad_elementos

def intercambiar_valores(vector:list,izq:int,der:int) -> None:

    """
    Intercambia dos elementos de una lista.
    Realiza el intercambio de posiciones entre dos elementos
    especificados por sus índices.

    Args:
    vector (list): Lista donde se realizará el intercambio.
    izq (int): Índice del primer elemento.
    der (int): Índice del segundo elemento.

    Returns:
    None
    """
    aux_izq = vector[izq]
    vector[izq] = vector[der]
    vector[der] = aux_izq

def ordenar_alumno_clave(lista_alumnos:list, clave:str ,criterio: bool = True) -> bool:

    """
    Ordena una lista de alumnos según una clave.
    Aplica un algoritmo de ordenamiento comparando el valor de una
    clave en cada diccionario. Permite ordenar de forma ascendente
    o descendente según el criterio.

    Args:
    lista_alumnos (list): Lista de diccionarios de alumnos.
    clave (str): Clave por la cual ordenar.
    criterio (bool): False para ascendente, True para descendente.

    Returns:
    bool: True si se ordenó correctamente, False en caso contrario.
    """

    if type(lista_alumnos) == list and type(clave) == str:
        retorno = True
        for izq in range(len(lista_alumnos) - 1):
            for der in range((izq + 1),len(lista_alumnos)):
                if (
                    criterio == False and (lista_alumnos[izq].get(clave) > lista_alumnos[der].get(clave)) or 
                    criterio == True and (lista_alumnos[izq].get(clave) < lista_alumnos[der].get(clave))
                ):
                    intercambiar_valores(lista_alumnos,izq,der)
    else:
        retorno = False

    return retorno




    









