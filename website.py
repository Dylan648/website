from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')