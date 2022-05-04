from flask import Blueprint, redirect, render_template, request
from flask_login import current_user
from flask_login import login_required
from app import Library as DB
from app.database.queries import view_loans, book_list_overdo, books_list
from app.tools.func import days_pass, return_list, enum_book
from app.database.models import Book
import datetime
main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    TODAY = datetime.date.today()
    try:
        id = current_user.id
    except:
        id = None
    loans = view_loans(DB, id)
    books = books_list(DB , Book)
   
    if request.method == 'POST':
        if "loan_book" in request.form:

            book = request.form.get('loan_book')         
            DB.loan_book(current_user.id,book, TODAY)
            return redirect(request.url + f'#{book}')

        if "return_book" in request.form:

            loan = return_list(request.form.get('return_book'))
            print(loan)               
            DB.return_book(loan_id= int(loan[0]), return_date= TODAY)           
            field = int(loan[3])
            
            return redirect(request.url + f'#{int(field)}')

    return render_template('index.html',books = books, loans = loans, days_pass = days_pass, enum = enum_book, today = TODAY.strftime('%Y,%M,%D') )


@main.route('/welcome')
@login_required
def welcome():

    return render_template('welcome.html', name = current_user.name)

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/account',methods=['GET', 'POST'])
@login_required
def account():

    if request.method == 'POST':
        if "return" in request.form:
            loan = request.form.get('return')
            DB.return_book(loan, datetime.date.today())

    return render_template('account.html')

