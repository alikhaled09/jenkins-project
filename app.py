
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("The Flask app is running and printed this in the console!")
    return "Hello from Jenkins simple Python App!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
