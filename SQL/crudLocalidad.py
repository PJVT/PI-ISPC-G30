import conexion_pythonmysql

def buscarLocalidad(codigo_postal):
    query = "SELECT * FROM Localidad WHERE codigo_postal = %s"
    values = (codigo_postal,)
    conexion_pythonmysql.cursor.execute(query,values)
    ciudadUnica = conexion_pythonmysql.cursor.fetchone()

    print(conexion_pythonmysql.cursor.rowcount, "Filas seleccionadas")

    if(conexion_pythonmysql.cursor.rowcount == 1):
        print(ciudadUnica)
        return True
    else:
        print(f"No existe en la base de datos la ciudad con Código Postal: {codigo_postal}")
        return False