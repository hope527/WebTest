import sqlite3
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def tt():
    con = sqlite3.connect('fund.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM basic_information")
    data = cur.fetchall()

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
