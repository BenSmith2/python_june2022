from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def say(name):
    print (name)
    return "hello, "+ name

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ""

    for i in range(0, num):
        output += f"<p>{word}</p>"

    return output