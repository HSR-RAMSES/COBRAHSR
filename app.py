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

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

PAGINA = '''<!DOCTYPE html>
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
 .botones{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
 button{background:#2f6df6;color:#fff;border:0;border-radius:6px;padding:8px 12px;font-size:13px;cursor:pointer}
 button.gd{background:#8b3dff} button.sec{background:#2a2350} button.wa{background:#25D366;color:#fff;font-weight:bold}
 main{flex:1;min-height:0;display:flex}
 .panel{flex:1;display:flex;flex-direction:column;min-width:0}
 .panel+.panel{border-left:1px solid #3b2a73}
 .titulo{font-size:12px;padding:6px 12px;background:rgba(15,6,40,.9);color:#a999d6}
 .area{position:relative;flex:1;display:flex;min-height:0;background:rgba(38,10,84,.55)}
 textarea{position:relative;z-index:1;flex:1;width:100%;resize:none;border:0;outline:none;background:transparent;color:#efe6ff;padding:12px;font-family:ui-monospace,Menlo,monospace;font-size:13px;line-height:1.5}
 iframe{flex:1;width:100%;border:0;background:#fff}
 .modal{position:fixed;inset:0;background:rgba(0,0,0,.7);display:none;align-items:center;justify-content:center;z-index:9;padding:16px}
 .modal.on{display:flex}
 .caja{background:#1a0f3a;border:1px solid #5b3fb5;border-radius:12px;padding:16px;width:100%;max-width:420px;max-height:80vh;overflow:auto}
 .caja h2{font-size:17px;margin-bottom:10px}
 .caja label{font-size:13px;color:#b8a8e6}
 input{width:100%;padding:10px;margin:4px 0 12px;border-radius:8px;border:1px solid #5b3fb5;background:#0f
