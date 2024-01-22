import model.conexion as db


def registrarDisco(nombre, artista, genero, precio, discografica, fecha):
    conn = db.conectar()
    sql = "INSERT INTO discos (nombre, artista, genero, precio, discografica, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nombre, artista, genero, precio, discografica, fecha)
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    cursor.close()
    print("Nuevo disco registrado ➕💿")
    return cursor.lastrowid


def obtenerDiscos():
    conexion = db.conectar()
    sql = "select * from discos"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    discos = cur.fetchall()
    cur.close()
    conexion.close()
    return discos

def obtenerDiscoPorId(id):
    conexion = db.conectar()
    sql = "select * from discos where id = %s"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql, (id,))
    disco = cur.fetchone()
    cur.close()
    conexion.close()
    return disco

def obtenerDiscosCarrito():
    conexion = db.conectar()
    sql = "select * from discos where id in (select id_producto from productopedido)"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    discos = cur.fetchall()
    cur.close()
    conexion.close()
    return discos


def borrarDisco(id):
    conexion = db.conectar()
    sql = "delete from discos where id = %s"
    cur = conexion.cursor()
    cur.execute(sql, (id,))
    conexion.commit()
    cur.close()
    conexion.close()
    print("Disco borrado ❌💿")
