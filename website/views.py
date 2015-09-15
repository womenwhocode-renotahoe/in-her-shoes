from flask import render_template
from website import website

@website.route('/')
def index():
<<<<<<< HEAD
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

@website.route('/two_girls')
def two_girls():
    return render_template('two_girls.html')
=======
    return render_template('index.html')
>>>>>>> 3498abed7eaddc54b63ea1401e2c3ee366ac1b16
