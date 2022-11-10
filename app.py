from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contato_aluno")
def funil():
    return render_template("contato_aluno.html")        

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/apps integrados")
def apps_integrados():
    return render_template("apps_integrados.html")

@app.route("/entrar")
def entrar():
    return render_template("entrar.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")



if __name__ == "__main__":
    app.run(debug=True)