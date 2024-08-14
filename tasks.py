import sqlite3

def conectar_db():
    return sqlite3.connect('tareas.db')

def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS listas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lista_id INTEGER,
        descripcion TEXT NOT NULL,
        completada BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY(lista_id) REFERENCES listas(id)
    )
    ''')
    conexion.commit()


































def agregar_lista(conexion, nombre_lista):
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO listas (nombre)
    VALUES (?)
    ''', (nombre_lista,))
    conexion.commit()

def agregar_tarea(conexion, lista_id, descripcion):
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO tareas (lista_id, descripcion)
    VALUES (?, ?)
    ''', (lista_id, descripcion))
    conexion.commit()

def completar_tarea(conexion, tarea_id):
    cursor = conexion.cursor()
    cursor.execute('''
    UPDATE tareas
    SET completada = 1
    WHERE id = ?
    ''', (tarea_id,))
    conexion.commit()

def eliminar_tarea(conexion, tarea_id):
    cursor = conexion.cursor()
    cursor.execute('''
    DELETE FROM tareas WHERE id = ?
    ''', (tarea_id,))
    conexion.commit()

def eliminar_lista(conexion, lista_id):
    cursor = conexion.cursor()
    cursor.execute('''
    DELETE FROM tareas WHERE lista_id = ?
    ''', (lista_id,))
    cursor.execute('''
    DELETE FROM listas WHERE id = ?
    ''', (lista_id,))
    conexion.commit()

def mostrar_tareas(conexion, lista_id):
    cursor = conexion.cursor()
    cursor.execute('''
    SELECT * FROM tareas WHERE lista_id = ?
    ''', (lista_id,))
    tareas = cursor.fetchall()
    return tareas

def mostrar_listas(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
    SELECT listas.id, listas.nombre, COUNT(tareas.id) as num_tareas
    FROM listas
    LEFT JOIN tareas ON listas.id = tareas.lista_id
    GROUP BY listas.id, listas.nombre
    ''')
    listas = cursor.fetchall()
    return listas

def main():
    conexion = conectar_db()
    crear_tablas(conexion)

    while True:
        print("\nMenú Principal:")
        print("1. Agregar una lista de tareas")
        print("2. Ver una lista de tareas")
        print("3. Eliminar una lista de tareas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_lista = input("Ingresa el nombre de la nueva lista: ")
            agregar_lista(conexion, nombre_lista)
        
        elif opcion == "2":
            listas = mostrar_listas(conexion)
            if not listas:
                print("No hay listas disponibles.")
                continue

            for lista in listas:
                print(f"ID: {lista[0]}, Nombre: {lista[1]}, Tareas: {lista[2]}")
                
            lista_id = int(input("Ingresa el ID de la lista que deseas ver: "))
            tareas = mostrar_tareas(conexion, lista_id)
            
            if not tareas:
                print("No hay tareas en esta lista.")
            else:
                for tarea in tareas:
                    estado = "Completada" if tarea[3] else "Pendiente"
                    print(f"ID: {tarea[0]}, Descripción: {tarea[2]}, Estado: {estado}")

            while True:
                print("\nMenú de la Lista:")
                print("1. Agregar una tarea")
                print("2. Completar una tarea")
                print("3. Eliminar una tarea")
                print("4. Regresar al menú principal")

                opcion_lista = input("Selecciona una opción: ")

                if opcion_lista == "1":
                    descripcion = input("Ingresa la descripción de la nueva tarea: ")
                    agregar_tarea(conexion, lista_id, descripcion)
                
                elif opcion_lista == "2":
                    tarea_id = int(input("Ingresa el ID de la tarea que deseas completar: "))
                    completar_tarea(conexion, tarea_id)
                
                elif opcion_lista == "3":
                    tarea_id = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
                    eliminar_tarea(conexion, tarea_id)
                
                elif opcion_lista == "4":
                    break
                
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

        elif opcion == "3":
            listas = mostrar_listas(conexion)
            if not listas:
                print("No hay listas disponibles.")
                continue

            for lista in listas:
                print(f"ID: {lista[0]}, Nombre: {lista[1]}, Tareas: {lista[2]}")

            lista_id = int(input("Ingresa el ID de la lista que deseas eliminar: "))
            eliminar_lista(conexion, lista_id)
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
    conexion.close()

if __name__ == "__main__":
    main()
