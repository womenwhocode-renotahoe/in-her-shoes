from flask import render_template, url_for
from website import website

@website.route('/')
def index():
    return render_template('index.html')