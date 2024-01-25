from flask import Flask, render_template, request, redirect, url_for
import os
import model.repositorio_tienda as rt

app = Flask(__name__)
app.secret_key = "abcd"

import webservices
import admin

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    print("WebServer is running ✅")
    app.run(debug=True)
