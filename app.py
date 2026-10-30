from flask import Flask, render_template
import pandas as pd
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Display Data From SQLite
@app.route("/data")
def data():

    conn = sqlite3.connect("database.db")

    df = pd.read_sql(
        "SELECT * FROM sales",
        conn
    )

    records = df.values.tolist()

    conn.close()

    return render_template(
        "data.html",
        records=records
    )


# Display Charts
@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html"
    )


if __name__ == "__main__":
    app.run(debug=True)