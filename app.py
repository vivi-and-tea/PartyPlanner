from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pygal
from pygal.style import RedBlueStyle, Style

app = Flask(__name__)
app.debug = True

style = Style(
    font_family='googlefont:Barlow',
    background='transparent')

#Basics:
## Ask Class and Race of party members
## Create categories to put 'points' into
## Display subsets of character types in graph by points.

## TODO:
#1. Create categories to break data into for display.
#2. Create forms to submit the required data.
#3. Collect data and distribute points into certain categories.


@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        if request.form.get('name1'):
            name1 = int(request.form.get('name1'))
        if request.form.get('name2'):
            name2 = int(request.form.get('name2'))
        return render_template('data.html', name1=name1, name2=name2 )
    return render_template('index.html')

@app.route('/charts/')
def line_route():

    pie_chart = pygal.Pie(inner_radius=.4, style=style, legend_at_bottom=True)
    pie_chart.title = 'Your Party'
    pie_chart.add('Tank', 25)
    pie_chart.add('Support', 25)
    pie_chart.add('Spellcaster', 50)
    pie_chart.render()
    chart = pie_chart.render_data_uri()

    return render_template( 'charts.html', chart = chart)

if __name__ == "__main__":
    app.run(debug=True)
