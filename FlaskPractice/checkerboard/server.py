from flask import Flask, render_template
from helpers import generate_checkerboard

app = Flask(__name__)    

@app.route('/')
def checkerboard():
    result = generate_checkerboard(8,8)
    return render_template("index.html", result = result)

@app.route('/<int:y>')
def checkerboard_2(y):
    result = generate_checkerboard(8,y)
    return render_template("index.html", result = result)
@app.route('/<int:x>/<int:y>')
def checkerboard_3(x,y):
    result = generate_checkerboard(x,y)
    return render_template("index.html", result = result)

@app.route('/<int:x>/<int:y>/<color1>/<color0>')
def checkerboard_4(x, y, color1, color0):
    result = generate_checkerboard(x,y)
    return render_template("index.html", result = result, color1 = color1, color0 = color0 )

if __name__=="__main__":       
    app.run(debug=True)    