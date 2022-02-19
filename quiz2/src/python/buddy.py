from flask import Flask

app = Flask(__name__)


@app.route("/buddy/list", method=['GET'])
def listBuddy():
    return "<p>Hello, World!</p>"


if __name == '__main__':
    app.run(debug=False, host='0.0.0.0')
