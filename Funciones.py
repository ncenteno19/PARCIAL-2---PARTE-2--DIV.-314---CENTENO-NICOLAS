import subprocess
import datetime as dt
import random

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

        #b)Guardar cada diccionario de la lista
        for i in range(len(lista_json)):
            lista_alumnos.append(lista_json[i])
       
    else:
        retorno = False

    return retorno

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
                









def leer_csv_notas_matriz(nombre_archivo:str, matriz_notas: list) -> list:

    """
    Lee un archivo CSV y construye una matriz de notas.

    Abre el archivo indicado, omite la primera línea (cabecera) y
    luego procesa cada línea mediante algoritmia, separando los valores
    por comas sin utilizar funciones propias de strings. Finalmente,
    convierte los valores a enteros y los almacena en una matriz.

    Args:
        nombre_archivo (str): Nombre o ruta del archivo CSV a leer.
        matriz_notas (list): Matriz donde se cargarán las notas

    Returns:
        list: Matriz de enteros donde cada fila representa un alumno
              y cada columna corresponde a una nota trimestral.
    """


    if (
        type(nombre_archivo) == str and 
        os.path.exists(nombre_archivo) and 
        type(matriz_notas) == list
    ):
        #a)Apertura
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            archivo.readline()#Falsa lectura

            for linea in archivo:
                linea = reemplazar_caracteres(linea,"\n","")
                fila_notas = separar_cadena(linea)
                normalizar_notas(fila_notas)
                matriz_notas.append(fila_notas)

        #c)cierre
        del archivo
    
    return matriz_notas        

def separar_cadena(cadena:str,separador:str = ",") -> list:

    """
    Separa una cadena en una lista de valores utilizando un separador.

    Recorre la cadena carácter por carácter y construye manualmente
    una lista de subcadenas cada vez que encuentra el separador,
    sin utilizar métodos de strings como split().

    Args:
        cadena (str): Cadena a separar.
        separador (str): Carácter que actúa como separador (por defecto ',').

    Returns:
        list: Lista de cadenas separadas.
    """

    lista_separada = []
    cadena_nueva = ""
    if type(cadena) == str and (type(separador) == str and len(separador) == 1):
        for i in range(len(cadena)):
            if cadena[i] == separador:
                lista_separada.append(cadena_nueva)
                cadena_nueva = ""
            else:
                cadena_nueva += cadena[i]
        lista_separada.append(cadena_nueva)
    
    return lista_separada

def calcular_porcentaje(cantidad_parcial: int, total: int, 
                        mensaje_error: str = "❌ División por 0") -> float:
    """
    Calcula porcentaje del valor parcial en referencia con el valor total indicado.

    Args:
        votos (int): Cantidad parcial a saber e porcentaje.
        total (int): Valor Total.
        mensaje_error (str): Mensaje a mostrar si el total es cero.

    Returns:
        float: Porcentaje calculado o None si no es posible realizar la división.
    """
    if total == 0:
        print(mensaje_error)
    else:
        return cantidad_parcial / total * 100
    
def calcular_promedio(total: int, cantidad_elementos: int,
                      mensaje_error: str = "❌ División por 0") -> float:
    
    """
    Calcula el promedio a partir de un total y una cantidad de elementos.

    Verifica que la cantidad sea distinta de cero para evitar errores
    de división. En caso contrario, muestra un mensaje de error.

    Args:
        total (int): Suma total de los valores.
        cantidad (int): Cantidad de elementos utilizados para el cálculo.
        mensaje_error (str): Mensaje a mostrar si la cantidad es cero.

    Returns:
        float: Promedio calculado o None si no es posible realizar la operación.
    """

    if cantidad_elementos == 0:
        print(mensaje_error)
    else:
        return  total/ cantidad_elementos

def guardar_csv_matriz(nombre_archivo: str, matriz: list, 
                       cabecera: str = "1° Trimestre,2° Trimestre,3° Trimestre") -> bool:

    
    """
    Guarda una matriz de notas en un archivo CSV.

    Crea o sobrescribe un archivo con el nombre indicado, escribe una
    cabecera y luego guarda cada fila de la matriz como una línea en
    formato CSV, separando los valores por comas.

    Args:
        nombre_archivo (str): Nombre o ruta del archivo CSV a crear.
        matriz (list): Matriz donde cada fila representa las notas de un alumno.
        cabecera (str): Línea inicial del archivo que describe las columnas.

    Returns:
        bool: True si la operación se realizó correctamente, False en caso contrario.
    """


    if type(nombre_archivo) == str and type(cabecera) == str and type(matriz) == list:
        retorno = True
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:

            archivo.write(cabecera + "\n")

            for fil in range(len(matriz)):
                linea = unir_cadena(matriz[fil])
                if fil == len(matriz) - 1:
                    archivo.write(linea)
                else:
                    archivo.write(linea + "\n")

        del archivo
    else:
        retorno = False

    return retorno

def unir_cadena(lista:list, separador:str = ",") -> str:
    """
    Une los elementos de una lista en una cadena separada por un carácter.

    Recorre la lista y construye manualmente una cadena donde los valores
    están separados por el carácter indicado, sin utilizar métodos de string.

    Args:
        lista (list): Lista de valores a unir.
        separador (str): Carácter separador (por defecto ',')

    Returns:
        str: Cadena formada por los elementos de la lista separados por el separador.
    """

    cadena_nueva = ""
    
    for i in range(len(lista)):
        if i == len(lista) - 1:
            cadena_nueva += f"{lista[i]}"
        else:
            cadena_nueva += f"{lista[i]}{separador}"
        
    return cadena_nueva

def nombre_archivo_csv()-> str:
    """
    Genera un nombre de archivo CSV con la fecha actual.

    Obtiene la fecha del sistema, la formatea en formato día-mes-año
    y la utiliza para construir el nombre del archivo.

    Returns:
        str: Nombre del archivo en formato 'dd-mm-aaaa.csv'.
    """

    fecha_actual = dt.date.today()
    fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
    nombre_archivo = fecha_formateada + ".csv"

    return nombre_archivo