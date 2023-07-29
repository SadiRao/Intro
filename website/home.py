from flask import Blueprint, render_template
homes  = Blueprint('home', __name__)

@homes.route('/')
def home():
    return render_template('home.html')