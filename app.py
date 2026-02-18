# Author: Amonn Burns
# Date: 1/27/26
# File:course.py
# Description: Combines all files and runs application

from flask import Flask, render_template
from course import c1, c2


app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('course.html', courses= [c1, c2])

@app.route('/lab02')
def lab02():
    return render_template('course.html', courses= [c1, c2])

if __name__ == '__main__':
    app.run()
