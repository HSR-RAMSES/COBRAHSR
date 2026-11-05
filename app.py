from flask import Flask, Response, request, jsonify
import sqlite3, hashlib
from datetime import datetime
import pathlib

app = Flask(__name__)
DB = "skyweeb.db"
NUMERO_WHATSAPP = "523342699274"

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init():
    c = db()
    c.execute("CREATE TABLE IF NOT EXISTS usuarios (telefono TEXT PRIMARY KEY, nombre TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS creaciones (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, autor TEXT, telefono_autor TEXT, fecha TEXT, codigo TEXT, clave TEXT)")
    c.commit(); c.close()
init()

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def get_pagina():
    texto = pathlib.Path("index.html").read_text(encoding="utf-8")
    return texto.replace("TU_NUMERO", NUMERO_WHATSAPP)

@app.route("/")
def inicio():
    return Response(get_pagina(), mimetype="text/html")

@app.route("/api/registro", methods=["POST"])
def registro():
    d = request.get_json()
    c = db()
    c.execute("INSERT OR REPLACE INTO usuarios VALUES (?,?)", (d["telefono"], d["nombre"]))
    c.commit(); c.close()
    return jsonify({"ok": True})

@app.route("/api/guardar", methods=["POST"])
def guardar():
    d = request.get_json()
    c = db()
    c.execute("INSERT INTO creaciones (nombre,autor,telefono_autor,fecha,codigo,clave) VALUES (?,?,?,?,?,?)",
        (d["nombre"], d["autor"], d["telefono"], datetime.now().strftime("%d/%m %H:%M"), d["codigo"], sha(d["clave"])))
    c.commit(); c.close()
    return jsonify({"ok": True})

@app.route("/api/creaciones")
def lista():
    c = db()
    rows = c.execute("SELECT id,nombre,autor,fecha FROM creaciones ORDER BY id DESC").fetchall()
    c.close()
    return jsonify([dict(r) for r in rows])

@app.route("/api/abrir", methods=["POST"])
def abrir():
    d = request.get_json()
    c = db()
    r = c.execute("SELECT codigo,clave FROM creaciones WHERE id=?", (d["id"],)).fetchone()
    c.close()
    if not r or r["clave"] != sha(d["clave"]):
        return jsonify({"error": "clave"}), 403
    return jsonify({"codigo": r["codigo"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
