from flask import Flask, render_template, session, redirect

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = "password"

@app.route('/')
def index():

    if 'counter_1' not in session:
        session['counter_1'] = 0

    return render_template('index.html')

@app.route('/counter/test')
def manipulate_counter():

    session[f'counter_1'] += 1

    return redirect('/')

@app.route('/reset')
def reset():

    session[f'counter_1'] = 0

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

