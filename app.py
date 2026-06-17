from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Entorno CI con funcionalidad a la espera</h1><p>Entorno de Integracion Continua Funcional</p>"
    #return "<h1>Funcionalidad a la espera</h1><p>Entorno de Integracion Continua Funcional</p>"
@app.route("/add/<a>/<b>")
def add(a, b):
    try:
        resultado = float(a) + float(b)
        return f"El resultado de {a} + {b} es: {resultado}"
    except ValueError:
        return "Error: Por favor ingrese numeros validos"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)