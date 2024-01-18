import model.conexion as db



def registrarDisco(nombre, artista, genero, precio, fecha):
    conn = db.conectar()
    sql = "INSERT INTO discos (nombre, artista, genero, precio, fecha) VALUES (%s, %s, %s, %s, %s)"
    val = (nombre, artista, genero, precio, fecha)
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    cursor.close()
    print("Nuevo disco registrado ➕💿")

def obtenerDiscos():
    conexion = db.conectar()
    sql = "select * from discos"
    cur = conexion.cursor(dictionary = True)
    cur.execute(sql)
    discos = cur.fetchall()
    cur.close()
    conexion.close()
    return discos
