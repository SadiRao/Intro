from flask import Blueprint, request, render_template, redirect, flash, url_for
from flask_mail import Mail, Message
from .database import db, User
import sqlite3

contacts = Blueprint('contact', __name__)

from website.__init__ import mail 

@contacts.route('/contact')
def contact():
    return render_template('contact.html')
@contacts.route('/submit', methods = ['GET', 'POST'])
def email():
    if request.method == 'POST':
        email=request.form['email'],
        message=request.form['msg'],
        msg = Message('New mail from website',
                  sender = 'email@gmail.com',
                  recipients = ['sadianadeem699@gmail.com'])
        msg.body = f"Email: {email}\nMessage: {message}"
        mail.send(msg)
        conn = sqlite3.connect('/Users/sadianadeem/Desktop/Website/instance/web.sqlite3')
        c = conn.cursor() 
        values = [str(email), str(message)]
        c.execute("INSERT INTO user(email, message) VALUES(?, ?)", values)
        conn.commit()
        conn.close()
        flash("Message sent successfully!")
        return redirect(url_for('contact.contact'))
    else:
        return render_template('contact.html')
    