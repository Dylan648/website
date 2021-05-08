from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    facePic = os.path.join(app.config['UPLOAD_FOLDER'], 'face.jpg')
    return render_template('about.html', face_pic=facePic)