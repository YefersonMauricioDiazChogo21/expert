from tabulate import tabulate
import os

archivo = "usuario.json"
alerta= "Aun no esta codificado"

def camEnRuta(rutas,camper):
    for i in rutas: 
        print("id.",i,rutas[i]["nombre"])
    selec=str(input("Ingresa el id de ruta a la cual deseas listar"))
    print("CAMPERS")
    for i in camper:
        if camper[i]["ruta"]==selec:
            print("Id:",i,"-",camper[i]["nombre"])
    print("TRAINERS")
    for i in camper:
        if camper[i]["ruta"]==selec:
            print("Id:",i,"-",camper[i]["trainer"])

def resultadosMod(rutas):
    for i in rutas:
        print("Id:",i,"-",rutas[i]["nombre"])
        ruta=int(input("Elije el Id de la ruta"))
        bandera=True
        while bandera:
            print("Elija el modulo")
            opc=int(input("\t1. Fundamentos de programacion\n"
                        "\t2. Programacion Web\n"
                        "\t3. Programacion Formal\n"
                        "\t4. Base de datos\n"
                        "\t5. Backend\n"
                        "\t6. Salir\n"))
            if opc==1:
                bandera2=True
                while bandera2:
                    print("Elija el sub-modulo")
                    opc2=int(input("\t1. Introduccion a la programacion\n"
                                "\t2. PseInt\n"
                                "\t3. Python\n"
                                "\t4. Salir"))
    print(alerta)
def reportes(camper,trainers,rutas):
    global alerta
    bandera =True
    while bandera:
        print("MODULO DE REPORTES")
        opc = int(input("\t1. Campers inscritos\n"
                        "\t2. Campers aprobados\n"
                        "\t3. Trainers\n"
                        "\t4. Campers con bajo rendimiento\n"
                        "\t5. Campers y entrenador en ruta\n"
                        "\t6. Resultados de pruebas en cada modulo\n"
                        "\t7. Salir\n"))
        if opc ==1:
            for i in camper:
                if camper[i]["estado"]=="inscrito":
                    print(i, camper[i]["nombre"])
        elif opc==2:
            for i in camper:
                if camper[i]["estado"]=="aprobado":
                    print(i, camper[i]["nombre"])
        elif opc==3:
            for i in trainers:
                print(i, trainers[i]["name"])
        elif opc==4:
            pass
            #camperRiesgo()
        elif opc==5:
            camEnRuta(camper,rutas)
        elif opc==6:
            resultadosMod(rutas)
        elif opc==7:
            bandera =False
            os.system('clear')
        else:
            print("Opcion no valida")