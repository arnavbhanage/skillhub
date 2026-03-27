from app import db 
from flask import request
from flask_login import UserMixin
from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])


def signup():
    email=request.form.get('email')
    password=request.form.get('password')
    passwordver=request.form.get('passwordver')
    #add verification email system later
    if request.method == 'POST':
    # your logic here
        if(password==passwordver):
            return
