from flask import Flask, Response

app = Flask(__name__)

PAGINA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SKY WEEB</title>
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; color: #ece4ff; font-family: system-ui, sans-serif; }
  body { display: flex; flex-direction: column;
    background: linear-gradient(135deg, #0a0520, #1a0b3d 55%, #07173a); }
  header { display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
    padding: 8px 12px; background: rgba(20, 8, 50, 0.85);
    border-bottom: 1px solid #3b2a73; }
  .logo { flex: 1; min-width: 150px; font-size: 26px; font-weight: 900;
    letter-spacing: 3px;
    background: linear-gradient(90deg, #a855f7, #6d5cff 50%, #38a3ff);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    filter: drop-shadow(0 0 8px rgba(124, 77, 255, 0.55)); }
  .botones { display: flex; flex-wrap: wrap; gap: 6px; }
  button { background: #2f6df6; color: #fff; border: 0; border-radius: 6px;
    padding: 8px 12px; font-size: 13px; cursor: pointer; }
  button.gd { background: #8b3dff; }
  button.sec { background: #2a2350; }
  main { flex: 1; min-height: 0; display: flex; }
  .panel { flex: 1; display: flex; flex-direction: column; min-width: 0; }
  .panel + .panel { border-left: 1px solid #3b2a73; }
  .titulo { font-size: 12px; padding: 6px 12px; background: rgba(15, 6, 40, 0.9);
    color: #a999d6; }
  .area { position: relative; flex: 1; display: flex; min-height: 0;
    background: rgba(38, 10, 84, 0.55); }
  .marca { position: absolute; inset: 0; display: flex; align-items: center;
    justify-content: center; text-align: center; padding: 10px;
    font-size: clamp(34px, 10vw, 96px); font-weight: 900; letter-spacing: 4px;
    color: rgba(168, 85, 247, 0.16); transform: rotate(-12deg);
    pointer-events: none; user-select: none; }
  textarea { position: relative; z-index: 1; flex: 1; width: 100%; resize: none;
    border: 0; outline: none; background: transparent; color: #efe6ff;
    padding: 12px; font-family: ui-monospace, Menlo, Consolas, monospace;
    font-size: 13px; line-height: 1.5; tab-size: 2; }
  iframe { flex: 1; width: 100%; border: 0; background: #fff; }
  .modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);
    display: none; align-items: center; justify-content: center;
    z-index: 9; padding: 16px; }
  .modal.on { display: flex; }
  .caja { background: #1a0f3a; border: 1px solid #5b3fb5; border-radius: 12px;
    padding: 16px; width: 100%; max-width: 420px; max-height: 80vh; overflow: auto; }
  .caja h2 { font-size: 17px; margin-bottom: 10px; }
  .caja label { font-size: 13px; color: #b8a8e6; }
  input { width: 100%; padding: 10px; margin: 4px 0 12px; border-radius: 8px;
    border: 1px solid #5b3fb5; background: #0f0826; color: #fff; font-size: 15px; }
  .acciones { display: flex; gap: 8px; justify-content: flex-end; }
  .fila { display: flex; gap: 6px; align-items: center; padding: 8px 0;
    border-bottom: 1px solid #33276b; }
  .info { flex: 1; min-width: 0; display: flex; flex-direction: column; }
  .info small { color: #a999d6; font-size: 11px; }
  /* TECLADO DE SIMBOLOS ABAJO */
  .teclado { display: flex; gap: 6px; overflow-x: auto; padding: 8px 10px;
    background: #120834; border-top: 1px solid #3b2a73;
    scrollbar-width: thin; }
  .teclado button { flex: 0 0 auto; background: #2a2350; border: 1px solid #4a3590;
    font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 16px;
    font-weight: bold; padding: 10px 14px; min-width: 44px; }
  .teclado button:active { background: #8b3dff; }
  .teclado button.etiqueta { background: #1a0f3a; color: #c4b5fd; font-size: 12px; }
  @media (max-width: 700px) {
    main { flex-direction: column; }
    .panel + .panel { border-left: 0; border-top: 1px solid #3b2a73; }
  }
</style>
</head>
<body>
<header>
  <h1 class="logo">SKY WEEB</h1>
  <div class="botones">
    <button onclick="ejecutar()">▶ Ejecutar</button>
    <button class="gd" onclick="abrirGuardar()">💾 Guardar</button>
    <button class="sec" onclick="abrirLista()">📁 Mis creaciones</button>
    <button class="sec" onclick="ejemplo()">Ejemplo auto</button>
    <button class="sec" onclick="limpiar()">Limpiar</button>
  </div>
</header>
<main>
  <section class="panel">
    <div class="titulo">CÓDIGO (HTML + CSS + JS)</div>
    <div class="area">
      <div class="marca">HSRRAMSES</div>
      <textarea id="codigo" spellcheck="false">
<style>
  body { margin: 0; background: #87ceeb; overflow: hidden; height: 100vh; }
  .calle { position: absolute; bottom: 0; width: 100%; height: 30%;
    background: #333; border-top: 6px solid #666; }
  .linea { position: absolute; bottom: 14%; width: 200%; height: 6px;
    background: repeating-linear-gradient(90deg,#fff 0 60px,transparent 60px 120px);
    animation: calle 1s linear infinite; }
  .auto { position: absolute; bottom: 25%; left: -200px; width: 160px; height: 60px;
    animation: avanzar 6s linear infinite; }
  .cuerpo { position: absolute; bottom: 14px; width: 160px; height: 34px;
    background: #e53935; border-radius: 10px; }
  .techo { position: absolute; bottom: 44px; left: 35px; width: 80px; height: 28px;
    background: #c62828; border-radius: 14px 14px 0 0; }
  .rueda { position: absolute; bottom: 0; width: 30px; height: 30px;
    background: #111; border-radius: 50%; border: 5px solid #bbb;
    animation: girar 0.5s linear infinite; }
  .rueda::after { content: ""; position: absolute; top: 0; left: 50%;
    width: 4px; height: 100%; background: #bbb; }
  .r1 { left: 18px; } .r2 { right: 18px; }
  @keyframes avanzar { to { left: 110%; } }
  @keyframes girar { to { transform: rotate(360deg); } }
  @keyframes calle { to { transform: translateX(-120px); } }
</style>

<div class="calle"><div class="linea"></div></div>
<div class="auto">
  <div class="techo"></div>
  <div class="cuerpo"></div>
  <div class="rueda r1"></div>
  <div class="rueda r2"></div>
</div>
</textarea>
    </div>
  </section>
  <section class="panel">
    <div class="titulo">RESULTADO</div>
    <iframe id="vista" sandbox="allow-scripts"></iframe>
  </section>
</main>

<!-- BARRA DE SIMBOLOS -->
<div class="teclado" id="teclado">
  <button onclick="insertar('{')">{</button>
  <button onclick="insertar('}')">}</button>
  <button onclick="insertar('[')">[</button>
  <button onclick="insertar(']')">]</button>
  <button onclick="insertar('(')">(</button>
  <button onclick="insertar(')')">)</button>
  <button onclick="insertar('<')">&lt;</button>
  <button onclick="insertar('>')">&gt;</button>
  <button onclick="insertar('/')">/</button>
  <button onclick="insertar('\\\\')">\\</button>
  <button onclick="insertar('&quot;')">"</button>
  <button onclick="insertar(&quot;'&quot;)">'</button>
  <button onclick="insertar('`')">`</button>
  <button onclick="insertar(';')">;</button>
  <button onclick="insertar(':')">:</button>
  <button onclick="insertar('=')">=</button>
  <button onclick="insertar('+')">+</button>
  <button onclick="insertar('-')">-</button>
  <button onclick="insertar('*')">*</button>
  <button onclick="insertar('%')">%</button>
  <button onclick="insertar('&')">&amp;</button>
  <button onclick="insertar('|')">|</button>
  <button onclick="insertar('!')">!</button>
  <button onclick="insertar('?')">?</button>
  <button onclick="insertar('_')">_</button>
  <button onclick="insertar('#')">#</button>
  <button onclick="insertar('@')">@</button>
  <button onclick="insertar('$')">$</button>
  <button onclick="insertar('{}')">{ }</button>
  <button onclick="insertar('()')">( )</button>
  <button onclick="insertar('[]')">[ ]</button>
  <button class="etiqueta" onclick="insertar('<div></div>')">&lt;div&gt;</button>
  <button class="etiqueta" onclick="insertar('<style></style>')">&lt;style&gt;</button>
  <button class="etiqueta" onclick="insertar('<script></script>')">&lt;script&gt;</button>
</div>

<div class="modal" id="mGuardar">
  <div class="caja">
    <h2>Guardar creación</h2>
    <label for="nombre">Nombre del código</label>
    <input id="nombre" maxlength="60" placeholder="Ej. Auto en la calle">
    <label for="autor">Autor</label>
    <input id="autor" maxlength="60" placeholder="Tu nombre">
    <div class="acciones">
      <button class="sec" onclick="cerrar('mGuardar')">Cancelar</button>
      <button class="gd" onclick="guardar()">Guardar en mi teléfono</button>
    </div>
  </div>
</div>

<div class="modal" id="mLista">
  <div class="caja">
    <h2>Mis creaciones</h2>
    <div id="lista"></div>
    <div class="acciones" style="margin-top:12px">
      <button class="sec" onclick="cerrar('mLista')">Cerrar</button>
    </div>
  </div>
</div>

<script>
  const codigo = document.getElementById("codigo");
  const vista = document.getElementById("vista");
  const base = codigo.value;
  let t;

  function ejecutar() { vista.srcdoc = codigo.value; }
  function limpiar() { codigo.value = ""; ejecutar(); }
  function ejemplo() { codigo.value = base; ejecutar(); }
  function cerrar(id) { document.getElementById(id).classList.remove("on"); }

  // INSERTA EL SIMBOLO DONDE ESTA EL CURSOR
  function insertar(txt) {
    const s = codigo.selectionStart;
    const e = codigo.selectionEnd;
    codigo.setRangeText(txt, s, e, "end");
    codigo.focus();
    ejecutar();
  }

  function leer() {
    try { return JSON.parse(localStorage.getItem("sw_lista") || "[]"); }
    catch (e) { return []; }
  }
  function esc(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;")
            .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function descargar(it) {
    const doc = `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(it.nombre)}</title>
<meta name="author" content="${esc(it.autor)}">
</head>
<body>
<!-- Creación: ${esc(it.nombre)} | Autor: ${esc(it.autor)} | Hecho en SKY WEEB -->
${it.codigo}
</body>
</html>`;
    const url = URL.createObjectURL(new Blob([doc], { type: "text/html" }));
    const a = document.createElement("a");
    const limpio = it.nombre.replace(/[^a-z0-9áéíóúñ _-]/gi, "").replace(/ +/g, "_");
    a.href = url;
    a.download = (limpio || "creacion") + ".html";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
  }

  function abrirGuardar() {
    document.getElementById("nombre").value = "";
    document.getElementById("autor").value = localStorage.getItem("sw_autor") || "";
    document.getElementById("mGuardar").classList.add("on");
    document.getElementById("nombre").focus();
  }

  function guardar() {
    const nombre = document.getElementById("nombre").value.trim() || "Sin nombre";
    const autor = document.getElementById("autor").value.trim() || "Anónimo";
    const it = { id: Date.now(), nombre: nombre, autor: autor,
                 fecha: new Date().toLocaleString(), codigo: codigo.value };
    try {
      localStorage.setItem("sw_autor", autor);
      const l = leer();
      l.unshift(it);
      localStorage.setItem("sw_lista", JSON.stringify(l));
    } catch (e) {}
    descargar(it);
    cerrar("mGuardar");
  }

  function boton(txt, fn) {
    const b = document.createElement("button");
    b.className = "sec";
    b.textContent = txt;
    b.onclick = fn;
    return b;
  }

  function pintar() {
    const cont = document.getElementById("lista");
    const l = leer();
    cont.textContent = "";
    if (!l.length) { cont.textContent = "Aún no has guardado nada."; return; }
    l.forEach(function (it) {
      const fila = document.createElement("div");
      fila.className = "fila";
      const info = document.createElement("div");
      info.className = "info";
      const b = document.createElement("b");
      b.textContent = it.nombre;
      const s = document.createElement("small");
      s.textContent = it.autor + " · " + it.fecha;
      info.append(b, s);
      fila.append(
        info,
        boton("Abrir", function () { codigo.value = it.codigo; ejecutar(); cerrar("mLista"); }),
        boton("⬇", function () { descargar(it); }),
        boton("🗑", function () {
          localStorage.setItem("sw_lista",
            JSON.stringify(leer().filter(function (x) { return x.id !== it.id; })));
          pintar();
        })
      );
      cont.append(fila);
    });
  }

  function abrirLista() { pintar(); document.getElementById("mLista").classList.add("on"); }

  codigo.addEventListener("input", function () {
    clearTimeout(t);
    t = setTimeout(ejecutar, 400);
  });

  codigo.addEventListener("keydown", function (e) {
    if (e.key === "Tab") {
      e.preventDefault();
      const s = codigo.selectionStart;
      codigo.setRangeText("  ", s, codigo.selectionEnd, "end");
    }
  });

  ejecutar();
</script>
</body>
</html>
"""

@app.route("/")
def inicio():
    return Response(PAGINA, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
