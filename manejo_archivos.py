
import os ,csv, procesamiento_n_gramas  

def validar_existencia_directorio(directorio):
    """Verifica que el directorio existe y que pueda acceder a este"""
    try:
        os.listdir(directorio)
        return True
    except (FileNotFoundError,NotADirectoryError):
        return False

def crear_diccionarios(directorio,n):
    """Crea un diccionario que como clave tiene el nombre del archivo y como valor un diccionario con los 'n' gramas de cada archivo"""
    archivos = os.listdir(directorio)
    diccionarios={}

    for archivo in archivos:
        if archivo.endswith(".txt"):
            ruta = os.path.join(directorio, archivo)
            diccionario_archivo = diccionarios_n_gramas(ruta, n)
            if diccionario_archivo != {}:
                diccionarios[archivo] = diccionario_archivo 

    return diccionarios

def diccionarios_n_gramas(ruta, n):
    """Genera un diccionario de 'n' gramas limpiando signos de puntuación"""
    lista_archivo = []
    caracteres_no_admitidos = ".,-!_><\\/"
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip().lower()
            lista_linea = []
            for caracter in linea:
                if caracter not in caracteres_no_admitidos:
                    lista_linea.append(caracter)
            lista_linea = "".join(lista_linea)
            palabras = lista_linea.split()
            lista_archivo += palabras

    diccionario = procesamiento_n_gramas.n_gramas(lista_archivo, n)
    return diccionario

def comparar_diccionarios(dics):
    """Compara diccionarios de n-gramas y calcula la similitud entre ellos"""
    d15_similitud={}
    d1_similitud={}
    claves = list(dics.keys())
    cantidad_diccionarios = len(claves)
    for i in range(cantidad_diccionarios-1): 
        clave_i = claves [i]
        diccionario_i= dics[clave_i]
        for j in range(i+1,cantidad_diccionarios):
            clave_j = claves [j]
            diccionario_j= dics[clave_j]

            porcentaje=procesamiento_n_gramas.porcentaje_coincidencias(diccionario_i,diccionario_j)

            if porcentaje >= 1:
               d1_similitud[(clave_i,clave_j)]=porcentaje
            if porcentaje >= 15:
                d15_similitud[(clave_i,clave_j)]=porcentaje

    return d15_similitud,d1_similitud

def diccionarios_con_concidencias(directorio,n):
    """Se encarga de generar una lista de diccionarios con n-gramas y compara que tan similares son"""
    diccionario= crear_diccionarios(directorio,n)
    dic15 , dic1 = comparar_diccionarios(diccionario)
    return dic15 , dic1 

def crear_csv(nombre_ruta,diccionario):
    with open(nombre_ruta,"w") as archivo_nuevo:
        w=csv.writer(archivo_nuevo,delimiter=",")

        encabezado=["nombre_archivo1","nombre_archivo2","similaridad"]
        w.writerow(encabezado)

        for clave,valor in diccionario.items():
            archivo1,archivo2 = clave
            lista=[archivo1,archivo2,f"{valor}%"]
            w.writerow(lista)
