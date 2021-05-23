from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    if( request.method  == 'GET'):
        return jsonify({
            'message': 'METHOD GET DEMO'
        });
    else:
        json_data = request.get_json()
        try:
            return jsonify({
                'message': json_data['message']
            })
        except:
            return jsonify({
                'error': 404,
                'message': 'is empty'
            }), 404

if __name__ == '__main__':
    app.run()
