from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contato")
def funil():
    return render_template("contato_aluno.html")        

if __name__ == "__main__":
    app.run(debug=True)