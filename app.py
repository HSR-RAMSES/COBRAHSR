from flask import Flask, Response

app = Flask(__name__)

PAGINA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Consola HTML en vivo</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; background: #0f1117; color: #e6e6e6;
    font-family: system-ui, sans-serif; }
  header { display: flex; gap: 8px; align-items: center; padding: 8px 12px;
    background: #181b24; border-bottom: 1px solid #2a2f3d; }
  header h1 { font-size: 15px; flex: 1; }
  button { background: #2f6df6; color: #fff; border: 0; border-radius: 6px;
    padding: 7px 12px; font-size: 13px; cursor: pointer; }
  button.sec { background: #2a2f3d; }
  main { display: flex; height: calc(100% - 49px); }
  .panel { flex: 1; display: flex; flex-direction: column; min-width: 0; }
  .panel + .panel { border-left: 1px solid #2a2f3d; }
  .titulo { font-size: 12px; padding: 6px 12px; background: #131620; color: #8a93a8; }
  textarea { flex: 1; width: 100%; resize: none; border: 0; outline: none;
    background: #0f1117; color: #d7e3ff; padding: 12px;
    font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px;
    line-height: 1.5; tab-size: 2; }
  iframe { flex: 1; width: 100%; border: 0; background: #fff; }
  @media (max-width: 700px) {
    main { flex-direction: column; }
    .panel + .panel { border-left: 0; border-top: 1px solid #2a2f3d; }
  }
</style>
</head>
<body>
<header>
  <h1>Consola HTML en vivo</h1>
  <button onclick="ejecutar()">▶ Ejecutar</button>
  <button class="sec" onclick="ejemplo()">Ejemplo auto</button>
  <button class="sec" onclick="limpiar()">Limpiar</button>
</header>
<main>
  <section class="panel">
    <div class="titulo">CÓDIGO (HTML + CSS + JS)</div>
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
  </section>
  <section class="panel">
    <div class="titulo">RESULTADO</div>
    <iframe id="vista" sandbox="allow-scripts"></iframe>
  </section>
</main>
<script>
  const codigo = document.getElementById("codigo");
  const vista = document.getElementById("vista");
  let t;

  function ejecutar() { vista.srcdoc = codigo.value; }
  function limpiar() { codigo.value = ""; ejecutar(); }
  function ejemplo() { location.reload(); }

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
de
