from .models import Tarea, SubTarea


def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    subtareas = SubTarea.objects.filter(eliminada=False)
    return tareas, subtareas


def crear_nueva_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()


def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla():
    tareas, subtareas = recupera_tareas_y_sub_tareas()
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas.filter(tarea=tarea):
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
