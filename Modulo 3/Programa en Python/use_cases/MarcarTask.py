from domain.Task import Task
from repository.TaskRepository import TaskRepository
class MarcarTask:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def marcar_completada(self, nombre):
        return self.repository.marcar_completada(nombre)