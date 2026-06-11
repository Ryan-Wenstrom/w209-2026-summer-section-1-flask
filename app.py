from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/getData/<int:year>")
def getData(year):
    revenue = pd.read_csv(os.path.join(APP_FOLDER, "static/data/1_Revenues.csv"))

    if year < 1942 or year > 2008:
        return "Error in the year range"

    filteredRevenue = revenue[revenue["Year4"] == year][
        ["Name", "Year4", "Total Revenue", "Population (000)"]
    ]

    return filteredRevenue.to_json(orient="records")


@app.route("/api")
def api():
    return {"x": 20}


@app.route("/players/count")
def count_players():
    con = sqlite3.connect("players_20.db")
    cur = con.cursor()
    result = cur.execute("SELECT COUNT(*) FROM players")
    return {"count": result.fetchone()[0]}


@app.route("/players/get_nationality")
def get_nationality():
    con = sqlite3.connect("players_20.db")
    cur = con.cursor()
    player = request.args.get('player')
    result = cur.execute(f"SELECT nationality FROM players where short_name = '{player}'")
    return {"nationality": result.fetchone()[0]}

if __name__ == "__main__":
    app.run()