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


@app.route("/David")
def David1():
    return render_template("David/PRINCIPAL.html")

@app.route("/David/DatosBasicos")
def David2():
    return render_template("David/DATOS PERSONALES.html")

@app.route("/David/DatosAcademicos")
def David3():
    return render_template("David/FORMACION.html")

@app.route("/David/DatosTecnologicos")
def David4():
    return render_template("David/TECNOLOGIAS.html")


@app.route("/Fabian")
def Fabian1():
    return render_template("Fabian/principal.html")

@app.route("/Fabian/DatosBasicos")
def Fabian2():
    return render_template("Fabian/datosB.html")

@app.route("/Fabian/DatosAcademicos")
def Fabian3():
    return render_template("Fabian/datosA.html")

@app.route("/Fabian/DatosTecnologicos")
def Fabian4():
    return render_template("Fabian/datosT.html")

if __name__ == "__main__":
    app.run(debug = True)