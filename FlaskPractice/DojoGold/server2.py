from flask import Flask, redirect, render_template, request, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'adglifheiaposaurpaosduhgfapowr'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session["activities"] = []
    print(session)
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process():
    print(request.form)

    i =0
    for x in request.form.keys():
        if x == "farm":
            i += random.randint(10, 20)
            session["activities"].append (f"you found {i} gold in the {x} {datetime.now()}")
            return i
        elif x == "cave":
            i += random.randint(5, 10)
            session["activities"] += [f"you found {i} gold in the {x} {datetime.now()}"]
            return i
        elif x == "house":
            i += random.randint(2,5)
            session["activities"] += [f"you found {i} gold in the {x} {datetime.now()}"]
            return i
        elif x == "casino":
            i += random.randint(-50, 50)
            session["activities"] += [f"you found {i} gold in the {x} {datetime.now()}"]
            return i

    session['gold'] += gold_found()
    print(request.form)

    return redirect('/')

@app.route('/restart', methods=["POST"])
def restart():
    session.clear()

    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True)