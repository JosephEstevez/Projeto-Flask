from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/joseph")
def joseph():
    return render_template("joseph.html")


@app.route("/users/<username>")
def users(username):
    return render_template("users.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
