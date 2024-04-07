from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        number=request.form.get("number")
        cv=int(number)*int(number)
        contex = {'number': number,
                  "cv": cv}
        if number != None:
            return render_template("number.html", **contex)
        else:
            return render_template("404.html")
    return render_template("index_7.html")


if __name__ == "__main__":
    app.run(debug=True)