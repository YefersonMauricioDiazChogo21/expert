import modulos.matricula as m
import modulos.puebas as p
import modulos.registroCamper as rc
import modulos.reportes as r
import modulos.gestionTrabajo as g
import modulos.validaciones as v

camper={
    "1005539417": {
        "nombre": "Yeferson Mauricio",
        "apellidos": "Diaz Chogo",
        "direccion": "cll148#22-05",
        "acudiente": "N/A",
        "telefonos": [
            {
                "celular": "3143807720"
            }
        ],
        "estado": "inscrito",
        "sub-estado": "",
        "pruebas": {
            "iniciales": {
                "practica": "59",
                "teorica": "59"
            }
        },
        "ruta": "",
        "trainer": "",
        "fecha": {
            "inicio": "",
            "final": ""
        },
        "area": ""
    },
    "1098406115": {
        "nombre": "Adriana Daniela",
        "apellidos": "Sanabria Llorente",
        "direccion": "vereda las granjas, finca agualuna",
        "acudiente": "N/A",
        "telefonos": [
            {
                "celular": "3245538952"
            }
        ],
        "estado": "aprobado",
        "sub-estado": "",
        "pruebas": {
            "iniciales": {
                "practica": "55",
                "teorica": "79"
            }
        },
        "ruta": "",
        "trainer": "",
        "fecha": {
            "inicio": "02/03/2024",
            "final": ""
        },
        "area": ""
    }
}
trainers={ 
        "1": {
            "name": "Miguel",
            "horarios": {
                "6am": "NodeJs",
                "10am": "",
                "2pm": "",
                "6pm": ""
            },
            "rutas": [
                "NodeJs"
            ]
        },
        "2": {
            "name": "Johlver",
            "horarios": {
                "6am": "",
                "10am": "",
                "2pm": "",
                "6pm": ""
            },
            "rutas": []
        },
        "3": {
            "name": "Juan",
            "horarios": {
                "6am": "",
                "10am": "",
                "2pm": "",
                "6pm": ""
            },
            "rutas": []
        },
        "4": {
            "name": "Pedro",
            "horarios": {
                "6am": "",
                "10am": "",
                "2pm": "",
                "6pm": ""
            },
            "rutas": []
        }
        }
rutas={
        "231": {
            "nombre": "NodeJs",
            "asignado": {
                "fundamentos": [
                    "introduccion a la algoritmia",
                    "PseInt",
                    "Python"
                ],
                "web": [
                    "HTML",
                    "CSS",
                    "Bootstrap"
                ]
            },
            "elegido": {
                "formal": "nodejs",
                "SGDB": {
                    "principal": "",
                    "secundaria": ""
                },
                "backend": ""
            },
            "cupo": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,31,32,33]
        },
        "232": {
            "nombre": "Java",
            "asignado": {
                "fundamentos": [
                    "introduccion a la algoritmia",
                    "PseInt",
                    "Python"
                ],
                "web": [
                    "HTML",
                    "CSS",
                    "Bootstrap"
                ]
            },
            "elegido": {
                "formal": "java",
                "SGDB": {
                    "principal": "",
                    "secundaria": ""
                },
                "backend": ""
            },
            "cupo": []
        },
        "233": {
            "nombre": "NetCore",
            "asignado": {
                "fundamentos": [
                    "introduccion a la algoritmia",
                    "PseInt",
                    "Python"
                ],
                "web": [
                    "HTML",
                    "CSS",
                    "Bootstrap"
                ]
            },
            "elegido": {
                "formal": "netcore",
                "SGDB": {
                    "principal": "",
                    "secundaria": ""
                },
                "backend": ""
            },
            "cupo": []
        }
        }
areas={
        "sputnik": {
            "6am": {
                "trainer": "",
                "ruta": ""
            },
            "10am": {
                "trainer": "",
                "ruta": ""
            },
            "2pm": {
                "trainer": "",
                "ruta": ""
            },
            "6pm": {
                "trainer": "",
                "ruta": ""
            }
        },
        "apolo": {
            "6am": {
                "trainer": "",
                "ruta": ""
            },
            "10am": {
                "trainer": "",
                "ruta": ""
            },
            "2pm": {
                "trainer": "",
                "ruta": ""
            },
            "6pm": {
                "trainer": "",
                "ruta": ""
            }
        },
        "artemis": {
            "6am": {
                "trainer": "",
                "ruta": ""
            },
            "10am": {
                "trainer": "",
                "ruta": ""
            },
            "2pm": {
                "trainer": "",
                "ruta": ""
            },
            "6pm": {
                "trainer": "",
                "ruta": ""
            }
        }}
saludo = [['|      Bienvenidos al sistema de gestión de campers      |']]

menuPrincipal = """
        Elige la opción de nuestro menú que desees

        1. Registro de campers
        2. Gestión de trabajo
        3. Registro de pruebas
        4. Gestor de matrículas
        5. Campers en riesgo
        6. Reportes
        7. Salir
"""

bandera2 = True
while bandera2:
     v.os.system('clear')
     print(r.tabulate(saludo,tablefmt='heavy_grid'))
     print(menuPrincipal)
     opc= v.valiInt()
     if opc == 1:
          rc.registroCamper(camper)
     elif opc == 2:
          g.gestionTrabajo(trainers,rutas,areas)
     elif opc == 3:
          p.registroPruebas(trainers,rutas,areas,camper)
     elif opc == 4:
          m.gestionMatricula()
     elif opc == 5:
          r.camperRiesgo()
     elif opc == 6:
          r.reportes(camper,trainers,rutas)
     elif opc==7:
          bandera2=False
     elif opc > 7:
          print('Adios')
          print("Respuesta invalida")
