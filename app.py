from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=["https://welikenodes.onelike.biz/", "http://localhost:3000"])
app.debug = True

@app.route("/", methods=['GET'])
def home():
    url = request.args['url']
    try:
        data = requests.get(url)
        # print(data.json())
        return data.json()
    except:
        raise Exception("Invalid URL")

@app.errorhandler(Exception)
def exception_handler(error):
    return repr(error), 503


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)