from flask import Flask, render_template, Response, request, redirect
import numpy as np

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/accountsanalysis')
def accountsanalysis():
    return render_template('accountsanalysis.html')

@app.route('/alertsanalysis')
def alertsanalysis():
    return render_template('alertsanalysis.html')

@app.route('/transactionsanalysis')
def transactionsanalysis():
    return render_template('transactionsanalysis.html')


if __name__=="__main__":
    app.run(debug=True)