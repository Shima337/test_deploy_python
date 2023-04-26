from flask import Flask, render_template, request, Response, jsonify
import time, json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return "HELLO WORLD2"




if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True)





