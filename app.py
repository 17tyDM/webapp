from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def index():
    return 'Another Response'