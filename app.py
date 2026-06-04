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

if __name__ == "__main__":
    app.run()