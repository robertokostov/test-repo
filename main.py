from datetime import datetime
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello():
    dictionary = dict()

    dictionary['date'] = datetime.now()
    dictionary['pod'] = 'localhost'
    dictionary['env'] = 'staging'

    return json.dumps(dictionary, default=str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
