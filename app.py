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
 input{width:100%;padding:10px;margin:4px 0 12px;border-radius:8px;border:1px solid #5b3fb5;background:#0f0826;color:#fff;font-size:15px}
 .acciones{display:flex;gap:8px;justify-content:flex-end}
 .fila{display:flex;gap:6px;align-items:center;padding:8px 0;border-bottom:1px solid #33276b}
 .info{flex:1;min-width:0;display:flex;flex-direction:column}
 .info small{color:#a999d6;font-size:11px}
 .separador{margin:14px 0 6px;font-size:13px;color:#c4b5fd;font-weight:bold;border-top:1px solid #33276b;padding-top:10px}
 .teclado{display:flex;gap:6px;overflow-x:auto;padding:8px 10px;background:#120834;border-top:1px solid #3b2a73}
 .teclado button{flex:0 0 auto;background:#2a2350;border:1px solid #4a3590;font-family:monospace;font-size:16px;font-weight:bold;padding:10px 14px;min-width:44px}
 @media(max-width:700px){main{flex-direction:column}.panel+.panel{border-left:0;border-top:1px solid #3b2a73}}
</style>
</head>
<body>
<header>
 <h1 class="logo">SKY WEEB</h1>
 <div class="botones">
  <button onclick="ejecutar()">Ejecutar</button>
  <button class="gd" onclick="abrirGuardar()">Guardar</button>
  <button class="sec" onclick="abrirLista()">Mis creaciones</button>
  <button class="sec" onclick="ejemplo()">Ejemplo auto</button>
  <button class="sec" onclick="limpiar()">Limpiar</button>
  <a href="https://wa.me/TU_NUMERO?text=Hola%20Ramses%2C%20me%20puedes%20pasar%20la%20contrase%C3%B1a%20para%20ver%20tu%20creaci%C3%B3n%20en%20SKY%20WEEB%3F" target="_blank"><button class="wa">Pedir contrasena</button></a>
  <span id="yo" style="font-size:12px;color:#c4b5fd"></span>
 </div>
</header>
<main>
 <section class="panel"><div class="titulo">CODIGO</div><div class="area"><textarea id="codigo" spellcheck="false"><h1 style="color:white">Hola SKY WEEB</h1></textarea></div></section>
 <section class="panel"><div class="titulo">RESULTADO</div><iframe id="vista" sandbox="allow-scripts allow-popups allow-top-navigation allow-same-origin"></iframe></section>
</main>
<div class="teclado">
 <button onclick="insertar(&quot;{&quot;)">{</button><button onclick="insertar(&quot;}&quot;)">}</button><button onclick="insertar(&quot;&lt;&quot;)">&lt;</button><button onclick="insertar(&quot;&gt;&quot;)">&gt;</button><button onclick="insertar(&quot;/&quot;)">/</button><button onclick="insertar(&quot;&quot;&quot;)">&quot;</button><button onclick="insertar(&quot;=&quot;)">=</button><button onclick="insertar(&quot;;&quot;)">;</button>
</div>
<div class="modal on" id="mRegistro"><div class="caja">
 <h2>Bienvenido a SKY WEEB</h2><p style="font-size:13px;color:#b8a8e6;margin-bottom:12px">Registrate para guardar y ver creaciones. Solo nombre y telefono.</p>
 <label>Tu nombre</label><input id="regNombre" placeholder="Ej. Ramses">
 <label>Tu numero de telefono</label><input id="regTel" placeholder="Ej. 3312345678" inputmode="numeric">
 <div class="acciones"><button class="gd" onclick="registrar()">Entrar</button></div>
</div></div>
<div class="modal" id="mGuardar"><div class="caja">
 <h2>Guardar creacion</h2>
 <label>Nombre del codigo</label><input id="nombre" placeholder="Ej. Auto en la calle">
 <label>Contrasena para verlo
