# -*- coding: utf-8 -*-
import sys
from TablaFrecuencia import TablaFrecuencia

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except Exception as e:
        print("Debes enviar como argumento el nombre de un archivo " \
            "txt que contenga el listado de valores a procesar.")
        raise

    try:
        with open(file_name, 'r') as f:
            lista = [int(i) for i in f.read().split()]
    except Exception as e:
        print("El archivo solo debe contener números.")
        raise

    tabla_frecuencia =  TablaFrecuencia(lista)
    tabla_frecuencia.calcular()
    print(tabla_frecuencia.absoluta)
    print(tabla_frecuencia.relativa)
