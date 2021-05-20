from flask import Flask
from flask import request, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/demo', methods=['GET'])
def getDemo():
    return jsonify({
        'test': '123'
    });


if __name__ == '__main__':
    app.run()
