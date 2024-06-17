import conexion_pythonmysql

def buscarPersona(dni):
    query = "SELECT * FROM Persona WHERE dni = %s"
    values = (dni,)
    conexion_pythonmysql.cursor.execute(query,values)
    personaUnica = conexion_pythonmysql.cursor.fetchone()

    print(conexion_pythonmysql.cursor.rowcount, "Filas seleccionadas")

    if(conexion_pythonmysql.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con DNI: {dni}")
        return False