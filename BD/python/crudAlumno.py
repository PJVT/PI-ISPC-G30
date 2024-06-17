import conexion_pythonmysql

def ingresar_informacion_alumno():
    nro_legajo = input("Ingrese Número de Legajo")
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    telefono = input("Ingrese el teléfono de la persona: ")
    e_mail = input("Ingrese su correo eléctronico")
    localidad = input("Ingrese la localidad de la persona: ")
    codigo_postal = input("Ingrese el código postal de la persona: ")

    conexion_pythonmysql.cursor.execute ("SELECT  p.dni, p.nombre, p.apellido, p.telefono, p.codigo_postal FROM Persona AS p JOIN Alumno As A ON p.id_alumno = A.dni" )

    query = "INSERT INTO Profesor (nro_legajo, dni, nombre, apellido, telefono, e_mail, localidad, codigo_postal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nro_legajo, dni, nombre, apellido, telefono, e_mail, localidad, codigo_postal)

    conexion_pythonmysql.cursor.execute(query, values)
    conexion_pythonmysql.conn.commit()
    print("Información ingresada con éxito.")

def actualizarInformacionAlumno():
    dni = input("ID del Alumno a actualizar: ")
    if(buscarPersona(dni)):
        nombre = ("Nuevo Nombre")
        apellido = input("Nuevo Apellido: ")
        telefono = input("Nuevo Teléfono: ")
        localidad = input("Nueva Localidad")
        codigo_postal = input("Nuevo Código Postal: ")
        
        query = "UPDATE Alumno SET nombre = %s, apellido = %s, telefono = %s, localidad = %s, codigo_postal = %s WHERE dni = %s"
        values = (nombre, apellido, telefono, localidad, codigo_postal)
        
        conexion_pythonmysql.cursor.execute(query, values)
        conexion_pythonmysql.conn.commit()
        print(f"Alumno con DNI {dni} actualizado con éxito.")
    else:
        print(f"Alumno con DNI {dni} NO EXISTE por lo tanto no puede ser modificado.")


def buscarPersona(id):
    query = "SELECT * FROM Persona WHERE dni = %s"
    values = (id,)
    conexion_pythonmysql.cursor.execute(query,values)
    personaUnica = conexion_pythonmysql.cursor.fetchone()

    print(conexion_pythonmysql.cursor.rowcount, "Filas seleccionadas")

    if(conexion_pythonmysql.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con DNI: {id}")
        return False

