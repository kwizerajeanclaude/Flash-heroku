from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def welc():
    return "Hello friends!!"


if __name__ == "__main__":
    app.run()