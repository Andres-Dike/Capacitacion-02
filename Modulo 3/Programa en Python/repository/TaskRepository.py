class TaskRepository:
    def __init__(self):
        self.tareas = []  # Lista para almacenar las tareas

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        return self.tareas

    def marcar_completada(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.completada = True
                return "Tarea marcada como completada"
        return "Tarea no encontrada"