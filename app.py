from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


@app.route("/")
def home():
    return render_template('index.html')
