def creciente(archivo):
    """
    Hace lo que dice el ejercicio
    """
    linea = archivo.readline()
    anterior = len(linea)
    while linea != '':
        nuevalinea = archivo.readline()
        if len(nuevalinea) != 0:
            res = anterior < len(nuevalinea)
            if res is True:
                anterior = len(nuevalinea)
                continue
        return res
    return True

with open('archivo.txt') as f:
    print(creciente(f))
