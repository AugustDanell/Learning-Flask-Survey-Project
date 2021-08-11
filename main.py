from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import matplotlib
app = Flask(__name__)
happiness_list = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    has_left_review = db.Column(db.Boolean())

    def __init__(self, name, email, review):
        self.name = name
        self.email = email
        self.review = review

def calculate_data():
    global happiness_list
    highest = 0
    lowest = 10

    sum = 0
    for i in happiness_list:
        sum += i
        if(i > highest):
            highest = i
        if(i < lowest):
            lowest = i

    if(happiness_list == []):
        return "No Data",-1,-1
    return (sum/len(happiness_list)), highest, lowest

@app.route("/")
def home():
    average_happiness, high, low = calculate_data()
    if(average_happiness == "No Data"):
        return render_template("home.html", avg = average_happiness, high="No Data", low= "No Data")
    else:
        return render_template("home.html", avg=average_happiness, high=high, low = low)

@app.route("/stats")
def name():
    return render_template("stats.html")

@app.route("/survey", methods=["POST", "GET"])
def survey():
    if request.method == "POST":
        review = request.form["nm"]
        happiness_list.append(int(review))
        average_happiness, highest, lowest = calculate_data()
        return render_template("home.html", avg=average_happiness, high=highest, low= lowest)
    else:
        return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug = True)
