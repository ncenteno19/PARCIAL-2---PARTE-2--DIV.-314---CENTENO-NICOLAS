import json
import os


def leer_json(nombre_archivo:str) -> any | None:

    """
    Lee un archivo JSON y devuelve su contenido.
    Abre el archivo y deserializa su contenido a una estructura de datos.
    Args:
    nombre_archivo (str): Nombre o ruta del archivo JSON.
    Returns:
    any | None: Datos leídos del archivo o None si ocurre un error.
    """
    if type(nombre_archivo) == str and os.path.exists(nombre_archivo):
        
        with open(nombre_archivo,"r") as archivo:
            retorno = json.load(archivo)
        del archivo
    else:
        retorno = None
    
    return retorno

def guardar_json(nombre_archivo:str,objeto_guardar:any) -> bool:
    
    """
    Guarda un objeto en un archivo JSON.
    Serializa el objeto recibido y lo escribe en el archivo indicado.
    Args:
    nombre_archivo (str): Nombre o ruta del archivo JSON.
    objeto_guardar (any): Datos a guardar.
    Returns:
    bool: True si se guardó correctamente, False en caso contrario.
    """

    if type(nombre_archivo) == str:
        with open(nombre_archivo,"w") as archivo:
            json.dump(objeto_guardar,archivo,indent=4)
        del archivo

        retorno = True
    else:
        retorno = False

    return retorno
