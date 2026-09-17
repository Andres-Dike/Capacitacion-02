from fastapi import FastAPI
from use_cases.CreateTask import CreateTask
from use_cases.ListTask import ListTask
from use_cases.MarcarTask import MarcarTask
from repository.TaskRepository import TaskRepository

app = FastAPI()

repository = TaskRepository()
create_task = CreateTask(repository)
list_task = ListTask(repository)
marcar_task = MarcarTask(repository)

@app.post("/tareas")
def registrar_tarea(nombre: str):

    tarea = create_task.agregar_tarea(nombre)
    return {
        "mensaje": "Tarea registrada correctamente",
        "tarea": {
            "nombre": tarea.nombre,
            "completada": tarea.completada
        }
    }


@app.get("/tareas")
def listar_tareas():

    if list_task.lista_esta_vacia():
        return {
            "mensaje": "No hay tareas registradas"
        }

    tareas = list_task.listar_tareas()

    return {
        "tareas": [
            {
                "nombre": tarea.nombre,
                "completada": tarea.completada
            }
            for tarea in tareas
        ]
    }
@app.put("/tareas/completar")
def marcar_tarea_completada(nombre: str):
   resultado = marcar_task.marcar_completada(nombre)
   return {
        "mensaje": resultado
   }