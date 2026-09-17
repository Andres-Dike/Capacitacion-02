from domain.Task import Task
from repository.TaskRepository import TaskRepository
class ListTask: 
       def __init__(self, repository: TaskRepository):
           self.repository = repository
       def listar_tareas(self):
           return self.repository.listar_tareas()