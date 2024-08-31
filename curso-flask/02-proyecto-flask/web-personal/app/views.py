from flask import render_template, Blueprint
# from app import app

base = Blueprint('base', __name__)

@base.route('/home')
def home():
    return render_template('home.html')

@base.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@base.route('/contact')
def contact():
    return render_template('contact.html')
