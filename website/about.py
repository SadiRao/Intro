from flask import Blueprint, request, render_template

abouts = Blueprint('about', __name__)

@abouts.route('/about')
def about():
    return render_template('about.html')