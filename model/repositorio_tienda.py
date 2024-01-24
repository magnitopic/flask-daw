import model.conexion as db


def registrarDisco(nombre, artista, genero, precio, discografica, fecha):
    conn = db.conectar()
    sql = "INSERT INTO discos (nombre, artista, genero, precio, discografica, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nombre, artista, genero, precio, discografica, fecha)
    cursor = conn.cursor()
    cursor.execute(sql, (val,))
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


def registrarPedido(nombre, email, direccion, tarjeta,
                    telefono, caducidad, cvv, productos_session):
    conexion = db.conectar()
    sql = "insert into pedidos (nombre, email, direccion, tarjeta, telefono, caducidad, cvv) values (%s, %s, %s, %s, %s, %s, %s)"
    cur = conexion.cursor()
    cur.execute(sql, (nombre, email, direccion, tarjeta,
                      telefono, caducidad, cvv))
    id_pedido = cur.lastrowid
    for ps in productos_session:
        id_producto = ps["id_producto"]
        cantidad_producto = ps["cantidad_producto"]
        sql = "insert into productopedido (id_producto, id_pedido, cantidad_producto) values (%s, %s, %s)"
        cur.execute(sql, (id_producto, id_pedido, cantidad_producto))
    conexion.commit()
    cur.close()
    conexion.close()


def borrarDisco(id):
    conexion = db.conectar()
    sql = "delete from discos where id = %s"
    cur = conexion.cursor()
    cur.execute(sql, (id,))
    conexion.commit()
    cur.close()
    conexion.close()
    print("Disco borrado ❌💿")
