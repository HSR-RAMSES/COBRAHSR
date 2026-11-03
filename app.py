from flask import Flask, request, jsonify
import sys
import io
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>COBRAHSR CONSOLE</title>
<style>
body { margin:0; background:#010409; color:white; font-family: monospace; display:flex; flex-direction:row; height:100vh; }
.left { width:50%; display:flex; flex-direction:column; border-right:2px solid #ffd700; }
.right { width:50%; background:#0e1525; padding:0; display:flex; flex-direction:column; }
.header { background:#161b22; padding:12px; color:#ffd700; font-weight:bold; text-align:center; font-size:13px; border-bottom:1px solid #333; }
textarea { flex:1; background:#010409; color:#00ff88; font-size:15px; padding:15px; border:none; outline:none; resize:none; }
.buttons { display:flex; gap:5px; padding:8px; background:#010409; }
.btn-run { flex:2; background:#ffd700; color:black; border:none; padding:14px; font-weight:bold; cursor:pointer; font-size:15px; border-radius:6px; }
.btn-save { flex:1; background:#00c853; color:white; border:none; padding:14px; font-weight:bold; cursor:pointer; font-size:14px; border-radius:6px; }
.btn-run:active, .btn-save:active { opacity:0.7; }
#output { white-space:pre-wrap; color:#e6edf3; padding:15px; flex:1; overflow:auto; font-size:14px; }

/* VERSION CELULAR */
@media (max-width: 768px) {
  body { flex-direction:column; }
  .left { width:100%; height:55vh; border-right:none; border-bottom:2px solid #ffd700; }
  .right { width:100%; height:45vh; }
}
</style>
</head>
<body>
<div class="left">
<div class="header">COBRAHSR > COMANDOS.PY</div>
<textarea id="code" spellcheck="false">name = 'conta'
print(name)

# Prueba aqui tu codigo
for i in range(5):
    print(f"Cobra {i}")
</textarea>
<div class="buttons">
<button class="btn-run" onclick="run()">▶ EJECUTAR</button>
<button class="btn-save" onclick="saveTxt()">💾 TXT</button>
</div>
</div>
<div class="right">
<div class="header">> RESULTADO</div>
<pre id="output">Listo para ejecutar...</pre>
</div>

<script>
async function run(){
  let code = document.getElementById('code').value;
  document.getElementById('output').innerText = "Ejecutando...";
  let res = await fetch('/run', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({code})});
  let data = await res.json();
  document.getElementById('output').innerText = data.output;
}

function saveTxt(){
  let code = document.getElementById('code').value;
  let blob = new Blob([code], {type: 'text/plain'});
  let url = URL.createObjectURL(blob);
  let a = document.createElement('a');
  a.href = url;
  let fecha = new Date().toISOString().slice(0,10);
  a.download = `COBRAHSR_comandos_${fecha}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code','')
    old_stdout = sys.stdout
    sys.stdout = captured = io.StringIO()
    try:
        exec(code, {})
        output = captured.getvalue()
        if not output:
            output = ">> Ejecutado OK (sin print)"
    except Exception:
        output = traceback.format_exc()
    finally:
        sys.stdout = old_stdout
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run()
