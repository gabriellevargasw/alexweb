from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Automação-industrial.html")

@app.route("/pagina-2")
def pagina2():
    return render_template("Automação Industrial PG2.html")

@app.route("/pagina-3")
def pagina3():
    return render_template("pagina-3.html")

@app.route("/pagina-4")
def pagina4():
    return render_template("pagina-4.html")
 
@app.route("/index")
def index():
   return render_template("Automação-industrial.html")


if __name__ == "__main__":
    app.run(debug=True)
