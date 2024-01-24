from flask import Flask, jsonify, request, session
from main import app
import model.repositorio_tienda as rt

ruta_webservices = "/web-services/"


@app.route(f"{ruta_webservices}/obtener-discos")
def ws_obtenerDiscos():
    discos = rt.obtenerDiscos()
    return jsonify(discos)


@app.route(f"{ruta_webservices}/obtenerDiscoPorId")
def obtenerDiscoPorId(id):
    disco = rt.obtenerDiscoPorId(id)
    return jsonify(disco)


# TODO: finish this
@app.route(f"{ruta_webservices}/agregarProductoCarrito", methods=["POST"])
def agregarProductoCarrito():
    id = request.get_json()["id"]
    cantidad = request.get_json()["cantidad"]
    if "carrito" not in session:
        session["carrito"] = []
    session["carrito"].append({"id": id, "cantidad": cantidad})
    return jsonify(["ok"])


@app.route(f"{ruta_webservices}/obtener-info-sesion")
def obtenerInfoSesion():
    return jsonify(session)


@app.route(f"{ruta_webservices}/obtenerDiscosCarrito")
def obtenerDiscosCarrito():
    returnValue = rt.obtenerDiscosCarrito(session["productos"])
    return jsonify(returnValue)


@app.route(f"{ruta_webservices}/vaciarCarrito")
def vaciarCarrito():
    session.clear()
    return jsonify(["ok"])


@app.route(f"{ruta_webservices}/registrarPedido")
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
    return jsonify(["ok"])
