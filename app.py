from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Server is working!'


@app.route('/data', methods=['POST'])
def data():
    return make_response(jsonify({"response": "Successful"}), 200)


if __name__ == '__main__':
    app.run()
