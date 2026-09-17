from fastapi import FastAPI
from use_cases.CreateTask import CreateTask
from repository.TaskRepository import TaskRepository

app = FastAPI()

repository = TaskRepository()
create_task = CreateTask(repository)

@app.get("/tareas")
def registrar_tarea(nombre: str):

    tarea = create_task.agregar_tarea(nombre)

    if tarea is None:
        return {
            "mensaje": "El nombre de la tarea no puede estar vacío"
        }

    return {
        "mensaje": "Tarea registrada correctamente",
        "tarea": {
            "nombre": tarea.nombre,
            "completada": tarea.completada
        }
    }