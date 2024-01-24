from flask import Flask, jsonify, request, session
from main import app
import model.repositorio_tienda as rt

ruta_webservices = "/web-services/"


@app.route(ruta_webservices)
def web_services():
    return "Servicio activo 🌐"

@app.route(f"{ruta_webservices}/obtener-discos")
def ws_obtenerDiscos():
    discos = rt.obtenerDiscos()
    return jsonify(discos)


@app.route(f"{ruta_webservices}/obtenerDiscoPorId")
def obtenerDiscoPorId(id):
    disco = rt.obtenerDiscoPorId(id)
    return jsonify(disco)


@app.route(f"{ruta_webservices}/agregarProductoCarrito", methods=["POST"])
def agregarProductoCarrito():
    id = request.get_json()["id"]
    cantidad = request.get_json()["cantidad"]
    if "productos" not in session:
        session["productos"] = []

    productos = session["productos"]
    encontrado = False
    for p in productos:
        if p["id_producto"] == id:
            encontrado = True
            p["cantidad_producto"] += cantidad

    if not encontrado:
        productos.append({"id_producto": id, "cantidad_producto": cantidad})
    session["productos"] = productos

    return jsonify(["ok"])


@app.route(f"{ruta_webservices}/obtenerDiscosCarrito")
def obtenerDiscosCarrito():
    returnValue = rt.obtenerDiscosCarrito(session["productos"])
    return jsonify(returnValue)


@app.route(f"{ruta_webservices}/vaciarCarrito")
def vaciarCarrito():
    session.clear()
    return jsonify(["ok"])


@app.route(f"{ruta_webservices}/registrarPedido", methods=["POST"])
def registrarPedido():
    nombre = request.get_json()["nombre"]
    email = request.get_json()["email"]
    direccion = request.get_json()["direccion"]
    tarjeta = request.get_json()["tarjeta"]
    telefono = request.get_json()["telefono"]
    caducidad = request.get_json()["caducidad"]
    cvv = request.get_json()["cvv"]
    # Aquí se debería validar los datos de nuevo
    rt.registrarPedido(nombre, email, direccion, tarjeta,
                       telefono, caducidad, cvv, session["productos"])
    session.clear()
    return jsonify(["ok"])
