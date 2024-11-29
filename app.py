from flask import Flask, render_template, request
import random

app = Flask(__name__)

def roll_dice(sides, number):
    return [random.randint(1, sides) for _ in range(number)]

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        sides = int(request.form.get("sides"))
        number = int(request.form.get("number") or 1)
        results = roll_dice(sides, number)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
