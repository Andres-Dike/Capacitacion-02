from domain.Task import Task
from repository.TaskRepository import TaskRepository
class ListTask: 
       def __init__(self, repository: TaskRepository):
           self.repository = repository
       def listar_tareas(self):
         if not self.lista_esta_vacia():
               
            return self.repository.listar_tareas()

       def lista_esta_vacia(self):
            
            return len(self.repository.listar_tareas()) == 0
               