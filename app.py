from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("52.79.228.153", 27017, username="sparta", password="hh99")
db = client.dbsparta_plus_week3


@app.route("/")
def main():
    return render_template("01_main.html")


@app.route("/login")
def test_login():
    return render_template("02_login.html")


@app.route("/map")
def test_map():
    return render_template("03_map.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

