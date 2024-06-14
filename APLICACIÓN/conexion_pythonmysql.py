import mysql.connector

class Cconexion

    def ConexionBD()
        try
            conexion = mysql.connector.connect(user='root', password='080910',
                                               host='271.0.0.1',
                                               database='mydb'
                                               port='3306')
            print("conexio exitosa")

            return conexion
            
        

        except mysql.connector.Error as error
            print("error al conectar bd")

            return conexion

    conexionBD()
