from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    from controller import *
    app.run(debug=True, host="127.0.0.1", port=8080)