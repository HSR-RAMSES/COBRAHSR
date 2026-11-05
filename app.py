from flask import Flask, Response, request, jsonify
import sqlite3, hashlib
from datetime import datetime

app = Flask(__name__)
DB = "skyweeb.db"

# TU WHATSAPP - YA LISTO
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
 *{box-sizing:border
