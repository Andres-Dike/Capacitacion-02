from domain.Task import Task
from repository.TaskRepository import TaskRepository
#esta clase cumple con spr, ya que tiene una sola responsabilidad, que es manejar la creación de tareas,
class CreateTask:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def agregar_tarea(self, nombre):
        if not nombre.strip():
            return "La tarea no puede estar vacía"
        nombre = nombre.strip().lower()
        tarea = Task(nombre)
        self.repository.agregar_tarea(tarea)
        return tarea
    
        # Esta función marca la tarea como completada
   
