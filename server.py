from itertools import count
import random 
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "shh"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html') 


@app.route('/rand', methods=['POST'])
def rand():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset(): 
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True) 