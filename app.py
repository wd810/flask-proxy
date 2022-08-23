from crypt import methods
from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
app.debug = True

@app.route("/", methods=['GET'])
def home():
    url = request.args['url']
    data = requests.get(url)
    print(data.json())
    return data.json()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)