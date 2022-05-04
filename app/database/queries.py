from re import S
from sqlalchemy import text
from app.tools.func import enum_book, is_overdo, int_date
import datetime

# can return customer specific by customer id
def view_loans(db, current = None):
    add = ''
    if current:

        add = f"WHERE loans.cust_id = {current }"

    stm =text(f'''
    SELECT 
    loans.id AS Loan,
    customers.id AS Customer_id,
    customers.name AS Customers,
    books.id AS Book_id,
    books.name as Book,
    loans.loan_date as Loan_date,
    loans.return_date as return_date,
    books.type as type
    FROM loans
    INNER JOIN customers ON customers.id = loans.cust_id
    INNER JOIN books ON books.id = loans.book_id
    {add} ORDER BY loans.return_date IS NULL DESC, loans.return_date  ASC; ''' )
    
    result = db.exe_stm(stm)
    return result



def books_extended(db, current = None):
    add = ''
    if current:
        add = f"AND loans.cust_id = {current}"

    stm =text(f'''
    SELECT 
    books.id AS book,
    books.name AS Title,
    books.author AS author,
    books.year_published AS Published,
    books.img_url AS IMG,
    books.description AS description,
    loans.id AS Loan,
    loans.loan_date as Loan_date,
    loans.return_date as Return_date,
    loans.cust_id AS Customer,
    books.type AS Loan_Type
    FROM books
    LEFT JOIN loans ON books.id = loans.book_id 
    {add}
     ; ''' )
    result = db.exe_stm(stm)
    return result


    # all books and intersection with current user, loan status and overdo
# returns a list of dicts
def book_list_overdo(db, current):
    books =[]
    query = books_extended(db, current)
    keys = ['book id', 'book title', 'author', 'published','img url', 'description', 'loan_id', 'loan date','return date','customer']
    for book in query:
        new_book ={}
        for i, key in enumerate(keys):
            new_book.update({key:book[i]})
        new_book.update({'loan type': enum_book(int(book[10]))})
        if book[7]:
            date  = int_date(book[7],splitter= '-')
            print(date)
            date_obj = datetime.date(date[0],date[1],date[2])
            print(date_obj)
            print(new_book['loan type'])
            over = is_overdo(date_obj,int(new_book['loan type']),is_enum= True)
        else:
            over = False
        new_book.update({'overdo': over})

        books.append(new_book)

    return books


# returns a python list of all the loans and puts true on overdo
def loans_with_overdo(db):
    loans = view_loans(db)
    new_list = []
    for loan in loans:
        temp_loan=[]
        for item in loan:
            temp_loan.append(item)
        temp_loan.append(is_overdo(temp_loan[5],temp_loan[7]))
        new_list.append(temp_loan)
    return new_list


def books_list(db,book_object):
    list =[]
    with db.session() as s:
        # id, name, author, img_url,description, year_published ,type
        for c in  s.query(book_object):
            book = (c.id, c.name, c.author,c.img_url, c.description, c.year_published, enum_book(c.type))
            list.append(book)

    return list