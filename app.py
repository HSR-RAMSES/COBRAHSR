from flask import Flask, Response, request, jsonify
import sqlite3, hashlib
from datetime import datetime

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

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

PAGINA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SKY WEEB</title>
<style>
 *{box-sizing:border-box;margin:0;padding:0}
 html,body{height:100%;color:#ece4ff;font-family:system-ui,sans-serif}
 body{display:flex;flex-direction:column;background:linear-gradient(135deg,#0a0520,#1a0b3d 55%,#07173a)}
 header{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:8px 12px;background:rgba(20,8,50,.85);border-bottom:1px solid #3b2a73}
 .logo{flex:1;min-width:150px;font-size:26px;font-weight:900;letter-spacing:3px;background:linear-gradient(90deg,#a855f7,#6d5cff 50%,#38a3ff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
 .botones
