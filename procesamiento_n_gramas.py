
def n_gramas(lista_texto,n):
    """Devuelve un diccionario con los 'n' gramas del texto"""
    n_gramas_dic={}
    cant_palabras = len(lista_texto)
    for i in range(cant_palabras-n+1):
        if cant_palabras - i >= n:
            lista=[]
            for j in range(i,i+n):
                lista.append(lista_texto[j])

            tupla=tuple(lista)
            if tupla not in n_gramas_dic:
                n_gramas_dic[tupla]=1
            else:
                n_gramas_dic[tupla]+=1
        else:
            break
    return n_gramas_dic

def total_apariciones(diccionario):
    """Calcula el total de apariciones de n-gramas en un diccionario"""
    return sum(diccionario.values())

def porcentaje_coincidencias(diccionario1,diccionario2):
    """Devuelve el porcentaje de similaridad entre las claves de dos diccionarios"""
    try:
        suma_interseccion=0
        for tupla in diccionario1:
            if tupla in diccionario2:
                    cant1= diccionario1.get(tupla)
                    cant2= diccionario2.get(tupla)
                    suma_interseccion+= (cant1+cant2)

        porcentaje_similaridad= suma_interseccion / (total_apariciones(diccionario1) + total_apariciones(diccionario2))
        return round(porcentaje_similaridad*100,2)
    except ZeroDivisionError:
        return 0
