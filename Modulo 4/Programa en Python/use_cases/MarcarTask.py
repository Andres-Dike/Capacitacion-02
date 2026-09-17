from domain.Task import Task
from repository.TaskRepository import TaskRepository
class MarcarTask:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def marcar_completada(self, nombre):
        if not nombre.strip():
            return "La tarea no puede estar vacía"
        if not self.existe_tarea(nombre):
            return "La tarea no existe"
  
    
    def existe_tarea(self, nombre):
     for tarea in self.repository.listar_tareas():
         if tarea.nombre == nombre:
            return True

     return False 