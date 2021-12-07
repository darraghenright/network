from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from `http://service:5000`'

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
