from flask import Flask, render_template

app = Flask(__name__)

#app = Flask(__name__, static_folder='./templates/images')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")

@app.route("/bukatu")
def bukatu():
    return render_template("bukatu.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
