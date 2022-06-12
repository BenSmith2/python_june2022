from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<int:x>/<int:y>')
def checkerboard_3(x, y):
    result = generate_checkerboard(x, y)
    return render_template("index.html", result = result)

def generate_checkerboard(x, y):
    result= []

    for j in range (0, y):
        temp = []
        for i in range(0, x):
            temp.append((i + j) % 2)
        result.append(temp)

    return result


if __name__=="__main__":# Run the app in debug mode.
    app.run(debug=True) # Run the app in debug mode.