from flask import Flask, request, jsonify

app = Flask(__name__)

CLAVES_VALIDAS = ["DEF456", "ABC123"]

@app.route("/verificar")
def verificar():
    clave = request.args.get("clave")
    if clave in CLAVES_VALIDAS:
        return jsonify({"valida": True})
    return jsonify({"valida": False})

if __name__ == "__main__":
    app.run(debug=True)
