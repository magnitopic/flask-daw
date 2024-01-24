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


def obtenerDiscosCarrito(productos_sesion):
    ids_sql = []
    productos_sesion = sorted(productos_sesion, key=lambda p: p["id_producto"])
    for p in productos_sesion:
        if isinstance(p["id_producto"], int):
            ids_sql.append(str(p["id_producto"]))
    ids_sql_consulta = ",".join(ids_sql)
    sql = "select * from discos where id in (" + \
        ids_sql_consulta + ") order by id asc"
    conexion = conexion.cursor(dictionary=True)
    cur.execute(sql)
    discos_en_carrito = cur.fetchall()

    resp = []
    for i, ps in enumerate(productos_sesion):
        resp.append({
            "disco": discos_en_carrito[i],
            "cantidad": productos_session[i]["cantidad_producto"]
        })
    cur.close()
    conexion.close()
    return resp


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


def obtenerPedidos():
    conexion = db.conectar()
    sql = """select p.id, p.nombre, p.email, p.direccion, p.tarjeta, p.telefono, p.caducidad, p.cvv, 
    pp.id_producto, pp.cantidad_producto 
    from pedidos p, productopedido pp, discos d
    where p.id = pp.id and d.id = pp.id_producto
    order by p.id desc"""
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    pedidos_completo = cur.fetchall()
    cur.close()
    conexion.close()
    return pedidos_completo


def borrarDisco(id):
    conexion = db.conectar()
    sql = "delete from discos where id = %s"
    cur = conexion.cursor()
    cur.execute(sql, (id,))
    conexion.commit()
    cur.close()
    conexion.close()
    print("Disco borrado ❌💿")
