from flask import Flask, render_template
from random_weapon import main

app = Flask(__name__)

@app.route("/")
def home():
    result = main(0)
    return render_template("page.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
