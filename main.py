from flask import Flask, render_template, request, redirect, url_for
import os
import model.repositorio_tienda as rt

app = Flask(__name__)

ruta_admin = "/admin"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route(f"/{ruta_admin}")
def admin():
    return render_template("index-admin.html")


@app.route(f"/{ruta_admin}/registrar-disco", methods=["GET"])
def registrarDisco():
    return render_template("registrar-disco.html")


@app.route(f"/{ruta_admin}/guardar-disco-nuevo", methods=["POST"])
def registrarDiscoPost():
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    genero = request.form["genero"]
    precio = request.form["precio"]
    discografica = request.form["discografica"]
    fecha = request.form["fecha"]
    foto = request.files["foto"]
    registry_id = rt.registrarDisco(nombre, artista, genero, precio, discografica, fecha)
    ruta_actual = os.path.dirname(__file__)
    ruta_imagen = os.path.join(ruta_actual, f"static/img/{registry_id}.jpg")
    foto.save(ruta_imagen)
    return render_template("registrar-disco_ok.html")


@app.route(f"/{ruta_admin}/listar-discos")
def listarDiscos():
    discos = rt.obtenerDiscos()
    return render_template("listado-discos.html", discos=discos)


@app.route(f"/{ruta_admin}/borrar-disco/<int:id>")
def borrarDisco(id):
    rt.borrarDisco(id)
    ruta_imgen = os.path.join(os.path.dirname(__file__), f"static/img/{id}.jpg")
    os.remove(ruta_imgen)
    return redirect("/admin/listar-discos")


if __name__ == "__main__":
    print("WebServer is running ✅")
    app.run(debug=True)
