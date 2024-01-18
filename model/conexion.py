import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "db_entrega"
        )
        if conexion:
            print("Database conection OK ✅")
    except:
        print("Database conection failed ❌")
        exit(1)
    return conexion