from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diy-guides')
def diy_guides():
    return render_template('diy_guides.html')

@app.route('/science')
def science():
    return render_template('science.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if _name_ == '_main_':
    app.run(debug=True)