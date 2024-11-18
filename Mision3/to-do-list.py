datos_estudiantes = {}


def agregar_tarea(usuario, tarea, fecha):
    if usuario not in datos_estudiantes:
        datos_estudiantes[usuario] = {"tareas": [], "recordatorios": []}
    datos_estudiantes[usuario]["tareas"].append({"tarea": tarea, "fecha_entrega": fecha})
    print(f"Tarea {tarea} con fecha de entrega {fecha} ha sido añadida correctamente para el usuario {usuario}.\n")


def ver_tareas(usuario):
    # Verificar si el usuario tiene tareas registradas
    if usuario in datos_estudiantes and datos_estudiantes[usuario]["tareas"]:
        print(f"\nTareas para {usuario}:")
        for idx, tarea in enumerate(datos_estudiantes[usuario]["tareas"], 1):
            print(f"{idx}. {tarea['tarea']} - Fecha de entrega: {tarea['fecha_entrega']}")
        print("\n")
    else:
        print(f"\n{usuario} no tiene tareas pendientes.\n")


def eliminar_tarea(usuario, numero_tarea):
    if usuario in datos_estudiantes and datos_estudiantes[usuario]["tareas"]:
        if 0 < numero_tarea <= len(datos_estudiantes[usuario]["tareas"]):
            tarea_eliminada = datos_estudiantes[usuario]["tareas"].pop(numero_tarea - 1)
            print(f"Tarea {tarea_eliminada['tarea']} eliminada para {usuario}.\n")
        else:
            print("Numero de tarea invalida")
    else:
        print(f"El usuario {usuario} no tiene tareas pendientes")


def iniciar_chatbot():
    while (True):
        print("**** Bienvenido a mi ChatBot ****")
        print("Opciones")
        print("1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Eliminar la tarea")
        print("4. Salir")
        op = int(input("Ingresa tu opción"))
        if (op == 1):
            usuario = input("Ingrese el nombre del usuario")
            tarea = input("Ingrese la tarea")
            fecha = input("Ingrese la fecha de la tarea en formato DD/MM/AAAA")
            agregar_tarea(usuario, tarea, fecha)
        elif (op == 2):
            usuario = input("Ingrese el nombre del usuario")
            ver_tareas(usuario)
        elif (op == 3):
            usuario = input("Ingrese el nombre del usuario")
            ver_tareas(usuario)
            numero_tarea = int(input("Ingrese el número de la tarea a eliminar"))
            eliminar_tarea(usuario, numero_tarea)
        elif (op == 4):
            print("Bye")
            break
        else:
            print("Opción Erroneas")


iniciar_chatbot()