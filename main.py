from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def index():
    return 'Welcome to the Flask API!'

if __name__ == '__main__':
    app.run(debug=True)
