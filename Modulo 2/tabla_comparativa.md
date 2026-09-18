| Aspecto | Módulo 1 — ToDo.py (ANTES) | Módulo 2 — Task/Main/TaskService (DESPUÉS) |
| --- | --- | --- |
| Arquitectura | Una sola clase monolítica | Separación en 3 capas (entidad, servicio, UI) |
| Nº de clases | 1 (ToDo) | 3 (Task, TaskService, Main) |
| Representación de la tarea | Diccionario (`{"nombre":..., "completada":...}`) | Clase Task (objeto) |
| Responsabilidad única (SRP) | No — la clase hace todo | Sí — cada clase tiene su rol |
| Abierto/Cerrado (OCP) | No — hay que modificar la clase para todo | Parcial — añadir función aún modifica TaskService |
| Separación lógica / interfaz | No — todo mezclado, print al final del archivo | Sí — Main maneja la UI, TaskService la lógica |
| Interfaz de usuario | Ninguna (llamadas hardcodeadas con print) | Menú interactivo por consola (input) |
| Almacenamiento | Lista en memoria dentro de la clase | Lista en memoria en TaskService |
| Normalización de nombres | No (guarda el nombre tal cual) | Sí (`strip().lower()`) |
| Validación de entrada | Solo valida nombre vacío | Valida nombre vacío |
| Reutilización / escalabilidad | Baja | Media |