from flask import render_template, url_for
from website import website

@website.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@website.route('/')
@website.route('/index')
def index():
    return render_template('index.html')

@website.route('/beagirl')
def beagirl():
    return render_template('beagirl.html')

@website.route('/about')
def about():
    return render_template('about.html')

@website.route('/give')
def give():
    return render_template('give.html')

@website.route('/contact')
def contact():
    return render_template('contact.html')