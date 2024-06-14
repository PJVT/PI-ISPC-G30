import conexion_pythonmysql
import crudProfesor

def cargarDatosAsignatura():
    id_asignatura = ("ID Asignatura:")
    nombre = input("Nombre: ")
    carga_horaria = input("Carga Horaria: ")
    id_profesor = input("Profesor: ")
    
    query = "INSERT INTO Asignatra (id_signatura, nombre, carga_horaria, id_profesor) VALUES (%s, %s, %s, %s)"
    values = (id_asignatura, nombre, carga_horaria, id_profesor)
    
    conexion_pythonmysql.cursor.execute(query, values)
    conexion_pythonmysql.conn.commit()
    print("Datos cargados con éxito.")

def actualizarDatosAsignatura():
    id_asignatura = ("Actualizar ID Asignatura:")
    nombre = input("Actualizar Nombre: ")
    carga_horaria = input("Actualizar Carga Horaria: ")
    id_profesor = input ("Actualizar ID Profesor: ")
    
    query = "UPDATE Asignatura SET id_asignatura = %s , nombre = %s, carga_horaria = %s, id_profesor = %s WHERE id = %s"
    values = (id_asignatura, nombre, carga_horaria, id_profesor)
    
    conexion_pythonmysql.cursor.execute(query, values)
    conexion_pythonmysql.conn.commit()
    print("Datos cargados con éxito.")

def eliminarAsignatura():
    id_asignatura = input("ID de la Asignatura a eliminar: ")
    if(seleccionarAsignatura(id_asignatura)):
        query = "DELETE FROM Asignatura WHERE id = %s"
        values = (id_asignatura,)
        
        conexion_pythonmysql.cursor.execute(query, values)
        conexion_pythonmysql.conn.commit()
        print(f"Asignatura con ID {id_asignatura} eliminada con éxito.")

def seleccionarAsignatura(id):
    query = "SELECT * FROM Asignatura WHERE id = %s"
    values = (id,)
    conexion_pythonmysql.cursor.execute(query,values)
    asignaturaUnica = conexion_pythonmysql.cursor.fetchone()

    print(conexion_pythonmysql.cursor.rowcount, "Filas seleccionadas")

    if(conexion_pythonmysql.cursor.rowcount == 1):
        print(asignaturaUnica)
        return True
    else:
        print(f"No existe en la base de datos la asignatura con id: {id}")
        return False