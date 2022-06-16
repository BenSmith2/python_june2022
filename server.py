from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST']) #when the user hits submit displays the information on the page when the user submits. 
def checkout():
    print(request.form)
    print("charging {{firstName lastName}} for {{count}} fruits")                 #add a print statement "charging customer {{customer name}} for {{count}} fruits"
    return render_template("checkout.html", straw = request.form['strawberry'], 
    rasp = request.form['raspberry'], apple = request.form['apple'],
    firstName = request.form["first_name"], lastName = request.form["last_name"],
    student_id = request.form["student_id"])


@app.route('/fruits') #display images of the fruits in the html page
def fruits():
    return render_template("fruits.html",)

if __name__=="__main__":   
    app.run(debug=True)    