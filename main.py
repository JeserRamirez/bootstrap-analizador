from flask import Flask, render_template, request
from ply import lex

app = Flask(__name__)


def procesarCadena(entrada):
    # Implement your logic to process the input string
    # For demonstration purposes, let's assume the processing is converting the string to uppercase
    cadenaProcesada = entrada.upper()
    return cadenaProcesada

def checkSintaxisCorrect(entrada):
    if entrada != "":
        return True
    return "Error de sintaxis"

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION'
)

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f'Caracter erroneo: {t.value[0]}')
    t.lexer.skip(1)

analizadorLexico = lex.lex()

def analizarLexico():
    codigoFuente = "2 mas 2"
    analizadorLexico.input(codigoFuente)

    for token in analizadorLexico:
        print(token)

@app.route("/", methods=["GET", "POST"])
def homepage():
    cadenaProcesada = None

    if request.method == "POST":
        entrada = request.form.get("entrada")
        cadenaProcesada = procesarCadena(entrada)

    return render_template("index.html", title="Lenguajes y Automatas II", cadenaProcesada=cadenaProcesada)

@app.route("/analisis-sintactico.html")
def analisis_sintactico():

    return render_template("analisis-sintactico.html")

@app.route("/analisis-lexico.html", methods=["GET","POST"])
def analisis_lexico():
    return render_template("analisis-lexico.html")

if __name__ == "__main__":
    app.run(debug=True)

