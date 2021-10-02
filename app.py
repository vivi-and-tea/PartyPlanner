from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pygal

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/charts/')
def line_route():

    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    pie_chart.render()
    chart = pie_chart.render_data_uri()

    return render_template( 'charts.html', chart = chart)

if __name__ == "__main__":
    app.run(debug=True)
