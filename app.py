"""
for subsequent pushes:
git add .
git commit -m "something happened"
git push
"""

from flask import Flask, render_template
from random_weapon import main

app = Flask(__name__)


def format_result(w_stars, w_type, w_mainstat, w_substattype, w_substat):
    return [f"{w_stars}* {w_type}", f"ATK {w_mainstat}{' '*4}{w_substattype} {w_substat}"]

@app.route("/")
def home():
    w_stars, w_type, w_mainstat, w_substattype, w_substat = main(0)
    return weapon_route(w_stars, w_type, w_mainstat, w_substattype, f"{w_substat}{'%' if w_substattype != 'Elemental Mastery' else ''}")

@app.route("/<w_stars>_<w_type>_<w_mainstat>_<w_substattype>_<w_substat>")
def weapon_route(w_stars, w_type, w_mainstat, w_substattype, w_substat):
    # reconstruct the result from the URL
    result = format_result(w_stars, w_type, w_mainstat, w_substattype, w_substat) + [f"https://gi-random-weapon.onrender.com/{w_stars}_{w_type}_{w_mainstat}_{w_substattype}_{w_substat}"]
    return render_template("page.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
