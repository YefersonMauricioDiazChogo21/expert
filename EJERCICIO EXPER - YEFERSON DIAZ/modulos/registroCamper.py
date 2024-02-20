import os
from tabulate import tabulate
import modulos.validaciones as v

def registroCamper(camper):
    bandera = True

    while bandera:
        v.os.system('clear')
        titulo=[["|          REGISTRO CAMPERS          |"]]
        print(tabulate(titulo,tablefmt='heavy_grid'))
        menu="""
        1. Registrar camper
        2. Listar campers
        3. salir al menu principal
        """
        print(menu)
        selec = v.valiInt()
        if selec == 1:

            documento = input("Numero de Documento del camper:\n")
            camper[documento]={"nombre" :str(input("Nombres:\n").upper()),
                            "apellidos" : str(input("Apellidos:\n").upper()),
                            "direccion" : str(input("Ditreccion de residencia:\n")),
                            "acudiente": str(input("Nmbre del acudiente:\n")),
                            "telefonos": [],
                            "estado": "inscrito",
                            "sub-estado":"",
                            "pruebas":{"iniciales":{"practica":"","teorica":""}},
                            "trainer":"",
                            "ruta":"",
                            "fecha": {"inicio": "",
                                      "final": ""},
                            "area":""
                            }
            bandera2=True
            while bandera2:
                telefonos={}
                selec2=0
                menu2="""
                    Ingrese el tipo de contacto:

                    1. telefono fijo
                    2. telefono celular
               
                """
                print(menu2)
                selec2=v.valiInt()
                print("Ingrese el numero:\n")
                tel = v.valiInt()
                if selec2 ==1:
                    telefonos["fijo"] = tel
                else:
                    telefonos["celular"] = tel
                
                bandera2 = bool(input("Desea agregar otro numnero mde telefono? ENTER(no) Otra tecla(si)"))
                
            
        elif selec==2:
            for i in camper:
                print(camper[i]["nombre"],camper[i]["apellidos"])
            stop=input('Presione una tecla para continuar')
        elif selec ==3:
            bandera = False
        else:
            print("Opcion invalida")
            bandera = True    