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
    
    locations = {'farm': [10, 20]}

    gold = random.randint(locations[request.form['location']][0], locations[request.form['location']][0])
    session['activities'].append({'message': f"Gained {gold} gold at the {request.form['location']}"})

    session['gold'] += gold
    print(request.form)

    return redirect('/')

@app.route('/restart', methods=["POST"])
def restart():
    session.clear()

    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True)