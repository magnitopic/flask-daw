from flask import Flask, render_template, request, redirect, url_for
import os
import model.repositorio_tienda as rt
# from flask_session import Session

app = Flask(__name__)
app.secret_key = "abcd"
""" SESSION_TYPE = 'redis'
Session(app) """

import webservices
import admin

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("static/img/favicon.ico")


if __name__ == "__main__":
    print("WebServer is running ✅")
    app.run(debug=True)
