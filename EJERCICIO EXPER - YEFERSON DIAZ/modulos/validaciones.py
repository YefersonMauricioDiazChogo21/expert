import os

# stop=input('Presione una tecla para continuar')

def valiInt():
    try:
        opc = int(input("\t"))
        return opc
    except ValueError:
        print('Solo se aceptan numeros, ingrese nuevamente')
        return valiInt()