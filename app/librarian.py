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

    return render_template('librarian/Librarian.html', name = current_user.name, data = loans, total = len(loans),Title="Loans")


@admin.route('/librarian',methods=["POST"])
@login_required
def reports():

    if "loans" in request.form:
        title = "Loans"
        data = loans_with_overdo(DB)
        

    if "overdo" in request.form:
        title = "Overdo"
        data = []
        loans = loans_with_overdo(DB)
        for loan in loans:
            if loan[8]:
                data.append(loan)

    if "books" in request.form:
        title = "Books"
        data = books_list(DB, Book)

    if "customers" in request.form:
        title = "Customers"
        data = DB.exe_stm("SELECT * FROM customers")


    return render_template('librarian/Librarian.html', name = current_user.name, data = data, total = len(data),Title = title)



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
    return render_template("librarian/add_customer.html", name = current_user.name, added=added)


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
    return render_template("librarian/add_book.html", name = current_user.name, added=added)



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
    return render_template("librarian/add_loan.html", name = current_user.name, added=added)


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
    return render_template("librarian/return_loan.html", name = current_user.name, added=added)
