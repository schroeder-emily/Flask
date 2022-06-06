from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')
def index():
    siblings = [
        {'first_name': 'Emily', 'last_name': 'Schroeder'},
        {'first_name': 'Katie', 'last_name': 'Talton'},
        {'first_name': 'Brian', 'last_name': 'Schroeder'},
        {'first_name': 'Jennifer', 'last_name': 'Murphy'},
    ]
    return render_template("index.html", users=siblings)

if __name__=="__main__":   
    app.run(debug=True) 
    