from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
happiness_list = []

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

@app.route("/<name>")
def name(name):
    return render_template("index.html", user =name)

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
