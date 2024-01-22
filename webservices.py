from flask import Flask, jsonify, request, session
from __main__ import app
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

    return


@app.route(f"{ruta_webservices}/vaciarCarrito")
def vaciarCarrito():

    return


@app.route(f"{ruta_webservices}/registrarPedido")
def registrarPedido():
    return
