from crypt import methods
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Dojo Survey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process_form():

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/form_result")

@app.route('/form_result')
def form_result():
    
    return render_template("form_result.html")

if __name__=="__main__":      
    app.run(debug=True) 