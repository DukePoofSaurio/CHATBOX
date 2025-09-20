import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='C:\Users\ESTUDIANTES\Downloads\SQLiteDatabaseBrowserPortable',
            #host='aqui va el link de cuando este en casa'
            user='root',
            password='',
            database='clasesistemas'
        )
        print("Coneccion Exitosa!")
    except Error as e:
        print(f"Error al conectar la Base de Datos")
    return connection