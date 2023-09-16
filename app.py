from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<test>')
def exercise_request(test):
    return f'exercise_request:{test}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/show_exercise')
def show_exercise():
    myname = request.args.get("my_name")
    if myname is None:
        return render_template('exercise.html')
    else : # exercise.html の formタグのaction属性を設定しない <form action="http://127.0.0.1:5000/exercise">
        return f'これはif文で条件分岐しています。\rあなたの名前は:{request.args.get("my_name")}'
    
@app.route('/exercise')
def exercise():
    return f'あなたの名前は:{request.args.get("my_name")}'

@app.route('/answer')
def answer():
    name = request.args.get("my_name")
    return render_template('answer.html',name=f"{name}")