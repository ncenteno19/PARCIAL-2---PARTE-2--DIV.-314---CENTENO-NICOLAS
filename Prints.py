from Funciones import *

def mostrar_matriz(matriz:list) -> None: 
    """
    Muestra en pantalla una matriz.

    Recorre la matriz utilizando dos bucles y muestra
    cada elemento en formato tabular

    Args:
        matriz (list): Matriz a mostrar.

    Returns:
        None
    """

    for fil in range(len(matriz)):
        for col in range(len(matriz[0])):
            print(matriz[fil][col],end=" ")
        print("")

def mostrar_alumnos_nota_menor_a(matriz_notas: list, nota:int,
                                 mensaje_error: str = "❌ No se encontraron alumnos") -> None:
    
    """
    Muestra los alumnos que poseen al menos una nota menor al valor indicado.

    Recorre la matriz de notas y detecta, por cada alumno, si tiene
    alguna nota inferior al umbral especificado. En caso afirmativo,
    muestra el trimestre y la nota correspondiente.

    Args:
        matriz_notas (list): Matriz donde cada fila representa un alumno
                             y cada columna una nota trimestral.
        nota (int): Valor umbral para comparar las notas.
        mensaje_error (str): Mensaje a mostrar si no se encuentran resultados.

    Returns:
        None
    """

    print(f"***  ALUMNOS CON NOTA MENOR A {nota}  ***\n")

    contador = 0
    if type(matriz_notas) == list and type(nota) == int and len(matriz_notas[0]) > 0:
        for fil in range(len(matriz_notas)):
            vector_notas = []
            vector_trimestre = []
            for col in range(len(matriz_notas[0])):
                if matriz_notas [fil][col] < nota:
                    vector_notas.append(matriz_notas [fil][col])
                    vector_trimestre.append(col+1)
                    
            
            notas_encontradas = len(vector_notas)

            if notas_encontradas > 0:
                contador += 1

            if notas_encontradas == 1:
                print(f"El alumno {fil+1} tuvo una nota menor a {nota}")
                print(f"Trimestre {vector_trimestre[0]}: Nota: {vector_notas[0]}")
                print("────────────────────────────────")


            elif notas_encontradas > 1:
                print(f"El alumno {fil+1} tuvo {notas_encontradas} notas menores a {nota}")
                for i in range (len(vector_trimestre)):
                    print(f"Trimestre {vector_trimestre[i]}: Nota: {vector_notas[i]}")
                print("────────────────────────────────")

        if contador == 0:
            print(mensaje_error)


    else:
        print("❌ Error en los datos enviados")

def mostrar_porcentaje(matriz_notas: list) -> None:

    """
    Calcula y muestra el porcentaje de alumnos y notas aprobadas y desaprobadas.

    Recorre la matriz de notas, calcula el promedio de cada alumno para
    determinar si aprobó o desaprobó el año, y contabiliza tanto la cantidad
    de alumnos como de notas aprobadas y desaprobadas. Finalmente, muestra
    los porcentajes correspondientes.

    Args:
        matriz_notas (list): Matriz donde cada fila representa un alumno
                             y cada columna una nota trimestral.

    Returns:
        None
    """

    print("***  PORCENTAJE DE APROBADOS Y DESAPROBADOS  ***\n")

    notas_aprobadas = 0
    notas_desaprobadas = 0
    alumnos_aprobados = 0
    alumnos_desaprobados = 0

    filas = len(matriz_notas)
    columnas = len(matriz_notas[0]) 
    
    if type(matriz_notas) == list and filas > 0 and columnas > 0:
        for fil in range(filas):
            suma_notas = 0
            for col in range(columnas):
                suma_notas += matriz_notas[fil][col] 
                if matriz_notas [fil][col] > 6:
                    notas_aprobadas += 1
                else:
                    notas_desaprobadas += 1

            promedio = calcular_promedio(suma_notas,columnas)

            print("──────────────────────────────────────────────")
            if promedio >= 7: 
                print(f"El alumno {fil+1} APROBÓ el año. Promedio {promedio:.2f}")
                alumnos_aprobados += 1
            else:
                print(f"El alumno {fil+1} DESAPROBÓ el año. Promedio {promedio:.2f}")
                alumnos_desaprobados += 1

        print("══════════════════════════════════════════════")
        print(f"Porcentaje alumnos APROBADAS: {calcular_porcentaje(alumnos_aprobados, filas):.2f} %")
        print(f"Porcentaje alumnos DESAPROBADOS: {calcular_porcentaje(alumnos_desaprobados, filas):.2f} %")
        print("══════════════════════════════════════════════")
        total_notas = filas * columnas
        print(f"Porcentaje notas APROBADAS: {calcular_porcentaje(notas_aprobadas, total_notas):.2f} %")             
        print(f"Porcentaje notas DESAPROBADAS: {calcular_porcentaje(notas_desaprobadas, total_notas):.2f} %")   
        print("══════════════════════════════════════════════")

    else:
        print("❌ Error en los datos enviados")

def mostrar_mejor_trimestre(matriz_notas: list) -> None:
    
    """
    Determina y muestra el/los trimestre(s) con mejor rendimiento.

    Calcula la suma de notas por cada trimestre y, como todos los trimestres
    poseen la misma cantidad de alumnos, utiliza dicha suma para identificar
    el trimestre con mayor promedio. En caso de empate, muestra todos los
    trimestres correspondientes.

    Args:
        matriz_notas (list): Matriz donde cada fila representa un alumno
                             y cada columna una nota trimestral.

    Returns:
        None
    """

    print(f"***  TRIMESTRE/S CON MEJOR PROMEDIO  ***\n")
    print("───────────────────────────────────────")
    
    suma_1 = 0
    suma_2 = 0
    suma_3 = 0
    
    if type(matriz_notas) == list and len(matriz_notas) and len(matriz_notas[0]) > 0:
        
        for fil in range(len(matriz_notas)):
            suma_1 += matriz_notas[fil][0]
            suma_2 += matriz_notas[fil][1]
            suma_3 += matriz_notas[fil][2]

        vector_sumas = [suma_1, suma_2, suma_3]

        aux_suma = suma_1
        for i in range (1,len(vector_sumas)):
            if aux_suma < vector_sumas[i]:
                aux_suma = vector_sumas[i]
    
        for j in range(len(vector_sumas)):
            if aux_suma == vector_sumas[j]:
                print(f"{j+1}° Trimestre")
                print(f"Promedio: {calcular_promedio(vector_sumas[j], len(matriz_notas)):.2f}")
                print("═══════════════════════════════════════")
            
    else:
        print("❌ Error en los datos enviados")




