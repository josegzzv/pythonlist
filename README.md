# Task Management with SQLite3

This is a task management program implemented in Python that uses an SQLite3 database to store and manage task lists. The program allows users to create task lists, add tasks to lists, complete tasks, delete tasks, and delete entire lists.

## Features

- **Create task lists**: Users can create multiple task lists, each with its own name.
- **Add tasks**: Users can add tasks to any existing task list.
- **Complete tasks**: Users can mark tasks as completed.
- **Delete tasks**: Users can delete specific tasks from a list.
- **Delete lists**: Users can delete entire lists, along with all associated tasks.
- **Persistent storage**: All lists and tasks are stored in an SQLite database (`tareas.db`), ensuring that data is preserved between sessions.

## Requirements

- Python 3.x
- SQLite3 library (included by default in Python)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. **Running the Program**:
    - Open a terminal and navigate to the directory where the `gestion_tareas_sqlite3.py` file is located.
    - Run the script with the following command:
      ```bash
      python gestion_tareas_sqlite3.py
      ```

2. **Interacting with the Menu**:
    - The program presents an interactive menu that allows you to choose different options:
      1. **Add a task list**: Create a new task list.
      2. **View a task list**: Display tasks from a specific list, with options to add, complete, or delete tasks.
      3. **Delete a task list**: Remove an entire list along with its associated tasks.
      4. **Exit**: Exit the program.

3. **Example Workflow**:
    - Select "1. Add a task list" to create a new list.
    - Select "2. View a task list" to view and manage tasks within the created list.
    - Add tasks, mark them as completed, or delete them as needed.
    - Select "3. Delete a task list" to remove a list when it is no longer needed.

## Database Structure

The program uses an SQLite database named `tareas.db`, which contains the following tables:

- **`listas`**: Stores task lists.
  - `id` (INTEGER, PRIMARY KEY): Unique identifier for the list.
  - `nombre` (TEXT): Name of the task list.

- **`tareas`**: Stores tasks associated with the lists.
  - `id` (INTEGER, PRIMARY KEY): Unique identifier for the task.
  - `lista_id` (INTEGER, FOREIGN KEY): Identifier of the list to which the task belongs.
  - `descripcion` (TEXT): Description of the task.
  - `completada` (BOOLEAN): Task status (`0` for pending, `1` for completed).

## Disclaimer

This program is provided for educational purposes only. It is intended to help users understand the basic functionality of the `sqlite3` library in Python. Error handling, best practices, and security considerations have not been implemented in this example. Please use this code responsibly and adapt it to your specific needs, incorporating proper error handling and following best practices for production code.


## Contributions

Contributions are welcome. If you want to improve this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.





# Gestión de Tareas con SQLite3

Este es un programa de gestión de tareas implementado en Python, que utiliza una base de datos SQLite3 para almacenar y gestionar listas de tareas. El programa permite a los usuarios crear listas de tareas, agregar tareas a las listas, completar tareas, eliminar tareas, y eliminar listas completas.

## Características

- **Crear listas de tareas**: Los usuarios pueden crear múltiples listas de tareas, cada una con su propio nombre.
- **Agregar tareas**: Los usuarios pueden agregar tareas a cualquier lista de tareas existente.
- **Completar tareas**: Los usuarios pueden marcar tareas como completadas.
- **Eliminar tareas**: Los usuarios pueden eliminar tareas específicas de una lista.
- **Eliminar listas**: Los usuarios pueden eliminar listas completas, junto con todas las tareas asociadas.
- **Almacenamiento persistente**: Todas las listas y tareas se almacenan en una base de datos SQLite (`tareas.db`), lo que garantiza que los datos se mantengan entre sesiones.

## Requisitos

- Python 3.x
- Biblioteca SQLite3 (incluida por defecto en Python)

## Instalación

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python 3.x instalado en tu sistema.

## Uso

1. **Ejecución del Programa**:
    - Abre una terminal y navega hasta el directorio donde se encuentra el archivo `gestion_tareas_sqlite3.py`.
    - Ejecuta el script con el siguiente comando:
      ```bash
      python gestion_tareas_sqlite3.py
      ```

2. **Interacción con el Menú**:
    - El programa presenta un menú interactivo que te permite seleccionar diferentes opciones:
      1. **Agregar una lista de tareas**: Crea una nueva lista de tareas.
      2. **Ver una lista de tareas**: Muestra las tareas de una lista específica, con opciones para agregar, completar o eliminar tareas.
      3. **Eliminar una lista de tareas**: Elimina una lista completa junto con sus tareas asociadas.
      4. **Salir**: Finaliza el programa.

3. **Ejemplo de Flujo de Trabajo**:
    - Selecciona "1. Agregar una lista de tareas" para crear una nueva lista.
    - Selecciona "2. Ver una lista de tareas" para ver y gestionar las tareas de la lista creada.
    - Agrega tareas, complétalas, o elimínalas según sea necesario.
    - Selecciona "3. Eliminar una lista de tareas" para eliminar una lista cuando ya no sea necesaria.

## Estructura de la Base de Datos

El programa utiliza una base de datos SQLite llamada `tareas.db`, que contiene las siguientes tablas:

- **`listas`**: Almacena las listas de tareas.
  - `id` (INTEGER, PRIMARY KEY): Identificador único de la lista.
  - `nombre` (TEXT): Nombre de la lista de tareas.

- **`tareas`**: Almacena las tareas asociadas a las listas.
  - `id` (INTEGER, PRIMARY KEY): Identificador único de la tarea.
  - `lista_id` (INTEGER, FOREIGN KEY): Identificador de la lista a la que pertenece la tarea.
  - `descripcion` (TEXT): Descripción de la tarea.
  - `completada` (BOOLEAN): Estado de la tarea (`0` para pendiente, `1` para completada).

## Descargo de responsabilidad / Aviso legal

Este proyecto ha sido desarrollado únicamente con fines educativos. No se recomienda su uso en entornos de producción o en aplicaciones comerciales sin una revisión exhaustiva y adaptaciones adicionales. El autor no se hace responsable de ningún daño o pérdida que pueda surgir del uso de este software.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

