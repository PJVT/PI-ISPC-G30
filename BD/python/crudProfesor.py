import conexion_pythonmysql

def ingresarInformacionProfesor():
    id_profesor = input ("Ingrese ID de profesor: ")
    id_asignatura = input ("Ingrese ID de Asignatura")
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    telefono = input("Ingrese el teléfono de la persona: ")
    localidad = input("Ingrese la localidad de la persona: ")
    codigo_postal = input("Ingrese el código postal de la persona: ")

    conexion_pythonmysql.cursor.execute ("SELECT p.dni, p.nombre, p.apellido, p.telefono, p.codigo_postal FROM Persona AS p JOIN Profesor As Pr ON p.id_alumno = Pr.dni" )

    query = "INSERT INTO Profesor (id_profesor, id_asignatura, dni, nombre, apellido, telefono, localidad, codigo_postal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (dni, nombre, apellido, telefono, localidad, codigo_postal)

    conexion_pythonmysql.cursor.execute(query, values)
    conexion_pythonmysql.conn.commit()
    print("Información ingresada con éxito.")

def actualizarInformacionProfesor():
    dni = input("ID del Profesor a actualizar: ")
    if(buscarPersona(dni)):
        nombre = ("Nuevo Nombre")
        apellido = input("Nuevo Apellido: ")
        telefono = input("Nuevo Teléfono: ")
        localidad = input("Nueva Localidad")
        codigo_postal = input("Nuevo Código Postal: ")
        id_asignatura = input("Nuevo ID de Asignatura")
        
        query = "UPDATE Profesor SET nombre = %s, apellido = %s, telefono = %s, localidad = %s, codigo_postal = %s, id_asignatura = %s WHERE dni = %s"
        values = (nombre, apellido, telefono, localidad, codigo_postal)
        
        conexion_pythonmysql.cursor.execute(query, values)
        conexion_pythonmysql.conn.commit()
        print(f"Profesor con DNI {dni} actualizada con éxito.")
    else:
        print(f"Profesor con DNI {dni} NO EXISTE por lo tanto no puede ser modificado.")

def buscarPersona(dni):
    query = "SELECT * FROM Persona WHERE dni = %s"
    values = (id,)
    conexion_pythonmysql.cursor.execute(query,values)
    personaUnica = conexion_pythonmysql.cursor.fetchone()

    print(conexion_pythonmysql.cursor.rowcount, "Filas seleccionadas")

    if(conexion_pythonmysql.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con DNI: {dni}")
        return False