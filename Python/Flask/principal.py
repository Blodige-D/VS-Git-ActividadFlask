from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Menu():
    return render_template("index.html")

@app.route("/Diego")
def Diego1():
    return render_template("Diego/Inicio.html")

@app.route("/Diego/DatosBasicos")
def Diego2():
    return render_template("Diego/DatosBasicos.html")

@app.route("/Diego/DatosAcademicos")
def Diego3():
    return render_template("Diego/DatosAcademicos.html")

@app.route("/Diego/DatosTecnologicos")
def Diego4():
    return render_template("Diego/DatosTecnologicos.html")

if __name__ == "__main__":
    app.run(debug = True)