import os
import modulos.validaciones as v
from tabulate import tabulate


areas={}


def trainers(trainers):
    titulo=[["|        GESTION DE TRIANERS       |"]]
    print(tabulate(titulo,tablefmt='heavy_grid'))
    for i in trainers:
        print("ID:",i,"-",trainers[i]["name"])
    bandera=True
    while bandera:

        menu="""
        1. Agregar trainer
        2. Asignar rutas y horarios  al trainer
        3. Salir
        """
        print(menu)
        print('Elije una opcion de nuestro menu')
        opc = v.valiInt()
        if opc == 1:
            idTrainer= str(input("Ingrese el documento del trainer\n-"))
            trainers[idTrainer] ={"name":str(input("Nombre completo del trainer\n-")),
                                            "horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                                            "rutas":[]
        }
            
        elif opc==2:
            idTrainer2= str(input("Ingrese el documento del trainer\n-"))
            for idRuta in rutas:
                print("Id:",idRuta,"-",rutas[idRuta]["nombre"])
            ruta=str(input("ingrese el Id de la ruta Ruta\n"))
            rutasTrainer =rutas[ruta]["nombre"]
            trainers[idTrainer2]["rutas"].append(rutasTrainer)
            print(trainers[idTrainer2]["horarios"])
            print("\tIngrese el horario asignado a la ruta\n",
            "\t1. 6am\n"
            "\t2. 10am\n"
            "\t3. 2pm\n"
            "\t4. 6pm\n"
            "\t5. Salir")
            opc2=int(input())
            if opc2==1:
                trainers[idTrainer2]["horarios"]["6am"]=rutasTrainer
            elif opc2==2:
                trainers[idTrainer2]["horarios"]["10am"]=rutasTrainer
            elif opc2==3:
                trainers[idTrainer2]["horarios"]["2pm"]=rutasTrainer
            elif opc2==4:
                trainers[idTrainer2]["horarios"]["6pm"]=rutasTrainer
            elif opc2==5:
                bandera=False
            else:
                print("Opcion no valida")
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("OPcion no valida")
       
def rutas(rutas):
    bandera=True
    while bandera:
        print("Rutas de entreamiento")
        for ruta in rutas:
            print(rutas[ruta]["nombre"])
        opc=int(input("\t1. Editar ruta existente\n"
                        "\t2. Crear nueva ruta\n"
                        "\t3. salir\n"))
        if opc==1:
            for ruta in rutas:
                print(rutas[ruta]["nombre"])
            rutaExistente= input("Nombre de la ruta")
            rutas[rutaExistente]["elegido"]= {"formal":rutaExistente,
                                    "SGDB":{"principal":str(input("Base de datos primaria\n")),
                                        "secundaria":str(input("Base de datos secundaria\n"))},
                                    "backend":str(input("Ingrese el Backend\n"))}
        elif opc==2:
            rutaNueva= input("Nombre de la ruta")
            rutas[rutaNueva]= {"nombre":rutaNueva,
                                "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                                "web":["HTML","CSS","Bootstrap"]},
                                    "elegido":{"formal":rutaNueva,
                                                "SGDB":{"principal":str(input("Sistema de base de datos primaria o principal\n")),
                                                        "secundaria":str(input("Sistema de base de datos secundaria\n"))},
                                                "backend":str(input("Backend\n"))
                                                },
                                    "cupo":[]   
            }
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("Opcion invalida")
        
def areas(areas):
    bandera =True
    while bandera:
        print("\t1. Listar areas existentes\n"
            "\t2. Crear nueva area\n"
            "\t3. Salir"
        )
        opc = int(input("\t"))
        if opc == 1:
            for i in areas:
                print(i)
        elif opc==2:
            for i in areas:
                print(i)
            areaNueva= str(input("Nombre de la area\n"))
            areas[areaNueva]={"6am":{"trainer":"","ruta":""},
                    "10am":{"trainer":"","ruta":""},
                    "2pm":{"trainer":"","ruta":""},
                    "6pm":{"trainer":"","ruta":""}}
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("Opcion invalida")
        

def gestionTrabajo(trainers,rutas,areas):
    bandera=True
    while bandera:
        print("GESTION DE TRABAJO")
        opc = int(input("\t1. Trainers"
                    "\n\t2. Areas de entrenamiento"
                    "\n\t3. Rutas de entrenamiento"
                    "\n\t4. Salir\n-"
                    ))
        if opc == 1:
            print("TRAINERS")
            trainers(trainers)
        elif opc==2:
            print("AREAS")
            areas(areas)
        elif opc==3:
            print("RUTAS")
            rutas(rutas)
        elif opc==4:
            bandera =False
            os.system('clear')
        else:
            print("Opcion invalida")