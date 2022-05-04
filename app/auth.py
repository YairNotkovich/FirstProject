from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, logout_user, login_user
from sqlalchemy import text, func
from flask import Blueprint
from app import Library as DB
from app.database.models import Customer



auth = Blueprint('auth', __name__)


auth = Blueprint('auth', __name__)

# I will add new customers using a regration page
@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def register_post(): 

    name = request.form.get('name')
    city = request.form.get('city')
    age = request.form.get('age')
    email = request.form.get('email')
    password = request.form.get('password')
    if DB.add_customer(name=name, city=city, age=age, email=email, password=password) :
        return redirect(url_for('auth.login'))
    else:
        flash('Email address already exists you might already have an account')
        return redirect(url_for('auth.register'))  



@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    if c_login(db = DB, email = email,password = password, remember = remember):
        return redirect(url_for('main.index'))

    else:
        flash('Please check your login details and try again or')
        return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def c_login(db, email , password, remember):
    with db.session() as session:

        customer = session.query(Customer).filter(
            func.lower(Customer.email) == email.lower()).first()
        if not customer or not customer.check_password(password):
            return False
        # if the user doesn't exist or password is wrong, reload the page
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        # session.expunge(customer)
        else:
            login_user(customer, remember=remember)
            session.close()
            return True