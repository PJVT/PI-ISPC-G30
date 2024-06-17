import conexion_pythonmysql
import buscarPersona

def ingresar_informacion():
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    telefono = input("Ingrese el teléfono de la persona: ")
    localidad = input("Ingrese la localidad de la persona: ")
    codigo_postal = input("Ingrese el código postal de la persona: ")

    query = "INSERT INTO persona (dni, nombre, apellido, telefono, localidad, codigo_postal) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (dni, nombre, apellido, telefono, localidad, codigo_postal)

    conexion_pythonmysql.cursor.execute(query, values)
    conexion_pythonmysql.conn.commit()
    print("Información ingresada con éxito.")

def actualizar_persona():
    id = input("DNI de la Persona a actualizar: ")
    if(buscarPersona(id)):
        nombre = ("Nuevo Nombre")
        apellido = input("Nuevo Apellido: ")
        telefono = input("Nuevo Teléfono: ")
        localidad = input("Nueva Localidad")
        codigo_postal = input("Nuevo Código Postal: ")
        
        query = "UPDATE Persona SET nombre = %s, apellido = %s, telefono = %s, localidad = %s, codigo_postal = %s, WHERE dni = %s"
        values = (nombre, apellido, telefono, localidad, codigo_postal)
        
        conexion_pythonmysql.cursor.execute(query, values)
        conexion_pythonmysql.conn.commit()
        print(f"Persona con DNI {id} actualizada con éxito.")
    else:
        print(f"Persona con DNI {id} NO EXISTE por lo tanto no puede ser modificada.")

def eliminar_persona():
    id = input("DNI de la Persona a eliminar: ")
    if(buscarPersona(id)):
        query = "DELETE FROM Persona WHERE dni = %s"
        values = (id,)
        
        conexion_pythonmysql.cursor.execute(query, values)
        conexion_pythonmysql.conn.commit()
        print(f"Persona con DNI {id} eliminada con éxito.")
    else:
        print(f"Persona con DNI {id} NO EXISTE por lo tanto no puede ser eliminada.")

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