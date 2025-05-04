from flask import Flask, request, jsonify
import os

app = Flask(__name__)

CLAVES_VALIDAS = ["DEF456", "ABC123"]

@app.route("/")
def home():
    return jsonify({"status": "Server is running"})

@app.route("/verificar")
def verificar():
    clave = request.args.get("clave")
    if not clave:
        return jsonify({"valida": False, "error": "No se proporcionó clave"}), 400
    if clave in CLAVES_VALIDAS:
        return jsonify({"valida": True})
    return jsonify({"valida": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
