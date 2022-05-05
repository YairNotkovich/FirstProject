import datetime
from flask import flash
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app.database.queries import loans_with_overdo
from app import Library as DB
from app.database import Book
from app.database.queries import  books_list
from app.tools.func import int_date

admin = Blueprint('admin', __name__)


@admin.route('/Librarian')
@login_required
def main():
    loans = loans_with_overdo(DB)

    return render_template('Librarian.html', name = current_user.name, loans = loans, total = len(loans))


@admin.route('/overdo')
@login_required
def overdo_pg():
    over = []
    loans = loans_with_overdo(DB)
    for loan in loans:
        if loan[8]:
            over.append(loan)
    return render_template('overdo.html', name = current_user.name, loans = over, total = len(over))


@admin.route('/books')
@login_required
def books_pg():
    books = books_list(DB, Book)
    return render_template('books.html', name = current_user.name, books = books, total = len(books))


@admin.route('/customers')
@login_required
def customers_pg():
    customers = DB.exe_stm("SELECT * FROM customers")
    return render_template('customers.html', name = current_user.name, customers = customers, total = len(customers))



@admin.route('/add_customers',methods=['GET', 'POST'])
@login_required
def add_customers():
    added = False
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        if DB.add_customer(name=name, city=city, age=age, email=email, password=password) :
            added = True 
        else:
            flash('Email address already exists you might already have an account')
            return redirect(url_for('admin.add_customers'))  
    return render_template("add_customer.html", name = current_user.name, added=added)


@admin.route('/add_book',methods=['GET', 'POST'])
@login_required
def add_book():
    added = False
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        date_list= int_date(request.form.get('pub'),'-')
        published = datetime.date(date_list[0], date_list[1], date_list[2])
        type = request.form.get('type')
        
        if DB.add_book(title,author,published,type):
            added = True 
        else:
            flash('')
            return redirect(url_for('admin.add_book'))  
    return render_template("add_book.html", name = current_user.name, added=added)



@admin.route('/add_loan',methods=['GET', 'POST'])
@login_required
def add_loan():
    added = False
    if request.method == 'POST':
        book = request.form.get('book')
        customer = request.form.get('cust')
        
        if request.form.get('date') == '':
            loan_date = datetime.date.today()
        else:
            date_list= int_date(request.form.get('date'),'-')
            loan_date = datetime.date(date_list[0], date_list[1], date_list[2])
        
    
        if DB.loan_book(book,customer,loan_date):
            added = True  
    return render_template("add_loan.html", name = current_user.name, added=added)


@admin.route('/return_loan',methods=['GET', 'POST'])
@login_required
def return_loan():
    added = False
    if request.method == 'POST':
        loan = request.form.get('loan')
        if request.form.get('date') == '':
            loan_date = datetime.date.today()
        else:
            date_list= int_date(request.form.get('date'),'-')
            return_date = datetime.date(date_list[0], date_list[1], date_list[2])
        
    
        if DB.return_book(loan,return_date):
            added = True  
    return render_template("return_loan.html", name = current_user.name, added=added)
