from flask import Flask

app = Flask(__name__)

@app.route("/index")
def index():
    return "Hola Mundo"

app.run(host='0.0.0.0', port=81)