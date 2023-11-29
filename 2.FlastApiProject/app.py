from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_URL = ("https://www.googleapis.com/customsearch/v1?"
           "key=AIzaSyApv3HSbuBNWxx2HCxgbsDIlrAZR36wNN8&"
           "cx=017576662512468239146:omuauf_lfve"
           )


@app.route("/", methods=["GET", "POST"])
def index():
    items = {}
    if request.method == "POST":
        user_input = request.form["user_input"]

        response = requests.get(f"{API_URL}&q={user_input}")
        items = response.json().get("items", {})

        with open("output.json", "w") as json_file:
            json.dump(response.json(), json_file, indent=4)

    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
