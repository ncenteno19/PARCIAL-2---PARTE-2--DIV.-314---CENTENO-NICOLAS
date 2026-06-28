
def ingresar_numero(mensaje: str, 
                    mensaje_error: str = "❌ Error. Los datos ingresados no son válidos.") -> int | float:
    """
    Solicita al usuario un número y valida que sea un entero o flotante válido.

    Verifica que la cadena ingresada represente un número válido
    utilizando código ASCII. Luego convierte el valor a tipo int
    o float según corresponda.

    Args:
        mensaje (str): Texto para solicitar el ingreso.
        mensaje_error (str): Mensaje a mostrar si el dato es inválido.

    Returns:
        int | float: Número válido ingresado por el usuario.
    """

    numero = input(mensaje)

    while validar_cadena_numero(numero) == False:
        print(mensaje_error)
        numero = input(mensaje)

    contador_puntos = 0
    for i in range(len(numero)):
            caracter = numero[i]
            caracter_ascii = ord(caracter)
            
            if caracter_ascii == 46:
                contador_puntos += 1

    if contador_puntos == 1:
        numero = float(numero)
    else:
        numero = int(numero)

    return numero
   
def validar_cadena_numero(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número entero o flotante válido.
    Utilizando código ASCII

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        contador_puntos = 0

        for i in range(len(cadena)):
            caracter = cadena[i]
            caracter_ascii = ord(caracter)
            
            if caracter_ascii == 46:
                contador_puntos += 1
                if contador_puntos > 1:
                    retorno = False
                    break

            elif caracter_ascii > 57 or caracter_ascii < 48:
                retorno = False
                break
        
        if contador_puntos == len(cadena):
            retorno = False       

    else:
        retorno = False

    return retorno

def ingresar_nombre(mensaje: str, 
                    mensaje_error: str = "❌ Inválido. Debe tener al menos 3 caracteres y solo letras.")-> str:

    """
    Solicita y valida el ingreso de un nombre.
    Pide al usuario un nombre por teclado y valida que tenga al menos
    3 caracteres y que contenga solo letras. Una vez validado, lo
    convierte a formato título.
    
    Args:
    mensaje (str): Texto para solicitar el ingreso.
    mensaje_error (str): Mensaje a mostrar en caso de error.

    Returns:
    str: Nombre válido en formato título.
    """

    nombre = input(mensaje)
    
    while True:

        if len(nombre) < 3:
            print(mensaje_error)
        
        elif validar_cadena_string(nombre) == False:
            print(mensaje_error)
        
        else:
            
            return nombre
        
        nombre = input(mensaje)

def validar_cadena_string(cadena: str) -> bool:
    
    """
    Verifica que una cadena contenga solo letras.
    Recorre la cadena carácter por carácter y valida que todos
    los caracteres sean letras (mayúsculas o minúsculas) utilizando ASCII.

    Args:
    cadena (str): Cadena a validar.

    Returns:
    bool: True si la cadena contiene solo letras, False en caso contrario.
    """

    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            caracter = cadena[i]
            caracter_ascii = ord(caracter)
            if not (
                (caracter_ascii >= 65 and caracter_ascii <= 90)or
                (caracter_ascii >= 97 and caracter_ascii <= 122)
                ):
                retorno = False
                break
    else:
        retorno = False

    return retorno

def validar_numero(mensaje: str, num_min: int, num_max: int ) -> int | float:
    
    """
    Solicita un número y valida que se encuentre dentro de un rango.
    Pide un valor entero al usuario y verifica que esté entre los
    límites indicados. Si no cumple, solicita el ingreso nuevamente.

    Args:
    mensaje (str): Texto para solicitar el ingreso.
    num_min (int): Valor mínimo permitido.
    num_max (int): Valor máximo permitido.

    Returns:
    int: Número válido dentro del rango especificado.

    """

    while True: 
            numero = ingresar_numero(mensaje)
            
            if numero < num_min or numero > num_max:
                print(f"❌ Error. Debe ser entre {num_min} y {num_max}.")
            else:
                return numero 
    
def validar_plan(mensaje: str = "Plan: ", mensaje_error: str= "❌ Error. Debe ser 1991, 2003 o 2024.") -> int:
    
    """
    Solicita y valida el plan de estudios.
    Pide un número entero y verifica que sea uno de los valores
    permitidos (1991, 2003 o 2024). Si no cumple, solicita nuevamente.
    
    Args:
    mensaje (str): Texto para solicitar el ingreso.
    mensaje_error (str): Mensaje a mostrar en caso de error.

    Returns:
    int: Plan válido.
    """

    while True: 
            numero = ingresar_numero(mensaje)
            
            if not (
                numero == 1991 or
                numero == 2003 or
                numero == 2024
            ):
                print(mensaje_error)
            else:
                return numero 
    



