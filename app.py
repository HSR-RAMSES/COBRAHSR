from flask import Flask, request, jsonify
import sys
import io
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>COBRAHSR CONSOLE</title>
<style>
body { margin:0; background:#0a0e14; color:white; font-family: monospace; display:flex; height:100vh; }
.left { width:50%; display:flex; flex-direction:column; border-right:2px solid #ffd700; }
.right { width:50%; background:#0e1525; padding:20px; overflow:auto; }
.header { background:#111; padding:10px; color:#ffd700; font-weight:bold; text-align:center; }
textarea { flex:1; background:#010409; color:#00ff88; font-size:16px; padding:15px; border:none; outline:none; resize:none; }
button { background:#ffd700; color:black; border:none; padding:12px; font-weight:bold; cursor:pointer; font-size:16px; }
button:hover { background:white; }
#output { white-space:pre-wrap; color:#d2d2d2; }
</style>
</head>
<body>
<div class="left">
<div class="header">COBRAHSR > COMANDOS.PY</div>
<textarea id="code" spellcheck="false">nmae = 'cobra'
colors = 'azul'*2
print(nmae)
print(colors)
for i in range(3):
    print(f"Cobra {i} lista")</textarea>
<button onclick="run()">▶ EJECUTAR (Ctrl+Enter)</button>
</div>
<div class="right">
<div class="header">> RESULTADO</div>
<pre id="output">Esperando comando...</pre>
</div>

<script>
async function run(){
  let code = document.getElementById('code').value;
  document.getElementById('output').innerText = "Ejecutando...";
  let res = await fetch('/run', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({code})});
  let data = await res.json();
  document.getElementById('output').innerText = data.output;
}
document.addEventListener('keydown', e => { if(e.ctrlKey && e.key === 'Enter'){ run(); } });
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
            output = ">> Código ejecutado sin errores (sin print)"
    except Exception:
        output = traceback.format_exc()
    finally:
        sys.stdout = old_stdout
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run()
