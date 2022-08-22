from cgitb import text
from flask import Flask, request
import requests

app = Flask(__name__)
app.debug = True

@app.route("/<url>")
def home(url):
    data = request.json
    lch = requests.get(data['url'])
    print(lch.json())
    return lch.json()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)