from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
happiness_list = []

def calculate_avg():
    global happiness_list
    sum = 0
    for i in happiness_list:
        sum += i

    if(happiness_list == []):
        return "No Data"
    return (sum/len(happiness_list))

@app.route("/")
def home():
    average_happiness = calculate_avg()
    return render_template("home.html", avg = average_happiness)

@app.route("/<name>")
def name(name):
    return render_template("index.html", user =name)

@app.route("/survey", methods=["POST", "GET"])
def survey():
    if request.method == "POST":
        review = request.form["nm"]
        happiness_list.append(int(review))
        average_happiness = calculate_avg()
        return render_template("home.html", avg=average_happiness)
    else:
        return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug = True)