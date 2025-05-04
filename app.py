from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de claves válidas (puedes mover esto a una base de datos)
CLAVES_VALIDAS = {"ABC123", "DEF456", "MI_CLAVE_PREMIUM"}

@app.route("/verificar_licencia", methods=["POST"])
def verificar_licencia():
    data = request.get_json()
    clave = data.get("clave")
    if clave in CLAVES_VALIDAS:
        return jsonify({"valida": True})
    return jsonify({"valida": False})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
