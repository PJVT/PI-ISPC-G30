import conexion_pythonmysql
import crudAsignatura

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