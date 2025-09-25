#from crypt import methods

#from httpx import request
from flask import Flask, render_template, url_for, request, redirect
from conexionLite import create_connection
db_file = "base.db"

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hola Mundo"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/mision", methods=['GET', 'POST'])
def mision():
    if request.method == 'POST':
        datos = request.form
        print(datos)
        return render_template('respuesta.html')
    else:
        return render_template('mision.html')

@app.route("/vision", methods=['GET', 'POST'])
def vision():
    if request.method == 'POST':
        datos = request.form
        print(datos)
    else:
        print("Metodo GET")
    return render_template('vision.html')

@app.route("/programas")
def programas():
    return render_template('programas.html')

@app.route("/listacarreras")
def listacarreras():
    conn = create_connection(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CARRERA;")
    programas = cursor.fetchall()
    return render_template('listacarreras.html', carreras = programas)

@app.route("/eliminar/<codigo>")
def eliminar(codigo):
    conn = create_connection(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CARRERA WHERE id = ?" , (codigo))
    conn.commit()
    conn.close()
    return redirect(url_for('programas.html'))

@app.route("/actualizar/<codigo>")
def actualizar(codigo):
    return redirect(url_for('programas.html'))

app.run(host='0.0.0.0', port=5000, debug=True)