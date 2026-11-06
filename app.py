from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def inicio():
    return send_file("galaxia-flores-azules.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
