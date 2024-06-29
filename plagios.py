
import manejo_archivos 

def pedir_directorio():
    """Solicita al usuario que ingrese un directorio o le da la posibilidad de salir del programa"""
    while True:
            directorio=input("-Ingrese el directorio a escanear (o ingrese '*' para salir): ")
            directorio=directorio.strip()
            if directorio == "*":
                return None,False
            elif not manejo_archivos.validar_existencia_directorio(directorio):
                print(f"  -- El directorio ingresado NO existe --\n")
                continue
            return directorio,True

def pedir_n():
    """Solicita al usuario el tamaño de 'n' para los n-gramas."""
    while True:
            n=input("-Ingrese el tamaño para procesar los n-gramas: ")
            if not validar_numero(n):
                print(f"  -- Solo se permite procesar n-gramas de 2 a 9 --\n")
                continue
            return int(n)

def validar_numero(numero):
    """Valida que el numero sea un digito y este en el rango pedido"""
    return numero.isdigit() and 2 <= int(numero) < 10 and len(numero) ==1

def mostrar_resultados_sospechosos(diccionario):
    """Muestra por pantalla los resultados con coincidencias mayores a 15%"""
    print(f"\nSe encontraron {len(diccionario)} coincidencias con un porcentaje mayor a 15%: ")
    indice=1
    for clave,valor in diccionario.items():
        archivo1 , archivo2 = clave
        print(f"{indice}. Entre: {archivo1} y {archivo2} | Porcentaje: {valor}% ")
        indice+=1
    print()

def preguntar_nombre_reporte():
    """Solicita al usuario el nombre del archivo CSV"""
    while True:
            nombre_archivo=input(f"-Ingrese el nombre del archivo para guardar el reporte: ")
            nombre_archivo = nombre_archivo.strip()
            caracteres_no_permitidos = "<>/\\|[]*}{"
            contiene_caracter_no_permitido= False
            for caracter in nombre_archivo:
                if caracter in caracteres_no_permitidos:
                    contiene_caracter_no_permitido = True
                    break
            if not nombre_archivo.endswith(".csv") or len(nombre_archivo)== 4 or contiene_caracter_no_permitido == True:
                print(f"  -- El archivo debe ser de formato 'csv' y debe tener un nombre valido --\n")
                continue
            return nombre_archivo

def main():
    while True:
        directorio , permanecer_en_programa = pedir_directorio()
        if not permanecer_en_programa:
            break
        n= pedir_n()
        dicc_15_simil, dicc_1_simil=manejo_archivos.diccionarios_con_concidencias(directorio,n)

        mostrar_resultados_sospechosos(dicc_15_simil)

        nombre_archivo_csv = preguntar_nombre_reporte()
        manejo_archivos.crear_csv(nombre_archivo_csv,dicc_1_simil) 

    print("Saliendo del programa..")
    return 

main()
