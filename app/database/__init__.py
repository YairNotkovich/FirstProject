from sqlalchemy import create_engine, text, func,update
from sqlalchemy.orm import sessionmaker
from .models import Base, Book, Customer, Loan
from sqlalchemy.exc import IntegrityError
import json
from app.tools.helpers import random_published, random_type, rnd_loan_date, progress, wic, colors
from app.tools.func import cls
import random
import datetime


class DB():

    def __init__(self, metadata=Base, uri='', echo=False):

        self.engine = create_engine(uri, echo=echo)
        self.metadata = metadata

    def init_db(self):
        self.metadata.metadata.create_all(self.engine, checkfirst=True)
        self.insert_data()

    def insert_data(self):

        if self.has_data('loans'):
            return True
        cls()
        wic(colors.HEADER, 'Inserting Demo data,')
        wic(colors.BOLD , f'{colors.WARNING}this can take a while but its only for the first run')

        v1 = self.insert_big_cust()
        v2 = self.insert_books()
        v3 = self.insert_loans()
        if (v1, v2, v3):
            wic(colors.OKGREEN, 'Done!')
            return True
        
    def session(self):
        session = sessionmaker(self.engine)
        return session()

    # check if table is empty
    # returns False if empty
    # to be used primarily at startup
    def has_data(self, table=''):
        stm = text(f'''SELECT COUNT(id) FROM {table};''')
        with self.engine.connect() as conn:
            try:
                if conn.execute(stm).scalar() < 3:
                    return False
                else:
                    return True
            except Exception as e:
                print(e)

        '''
    def add(self,table, **kw):
        try:
            with self.engine.connect() as con:
                columns = tuple(kw.keys())
                values = tuple(kw.values())
                stm = f"INSERT INTO {table}{columns} VALUES {values};"
                con.execute(text(stm))
        except Exception as e:
            print(e)
        '''

    def exe_stm(self, stm):
        try:
            with self.engine.connect() as con:
                result =  con.execute(stm).all()
                return result
        except Exception as e:
            print(e)
        

    def add_book(self, book_name, author, year_published, type, img_url='', description=''):

        with self.session() as session:
            try:
                # check if the book already exists.
                # when working with the json list there are duplicates for sure

                if (session.query(Book).filter(func.lower(Book.author) == author.lower() and
                                               func.lower(Book.name) == book_name.lower()).first()):  # long if statement

                    # wic('Book already exists')
                    return False
                else:
                    # Else register and commit the seesion
                    new_book = Book(
                        name=book_name,
                        author=author,
                        year_published=year_published,
                        type=type,
                        img_url=img_url,
                        description=description
                    )

                    session.add(new_book)
                    session.commit()
                return True
            except IntegrityError:  # i want to catch only this error and fix all the rest
                session.rollback()

    def add_customer(self, name, city, age, email, password):

        with self.session() as session:
            try:
                # check if email exists and if so try again
                if (session.query(Customer).filter(func.lower(Customer.email) == email.lower()).first()):
                    # wic('email already exists')
                    return False
                else:
                    try:
                            # Else register and commit the seesion
                        new_customer = Customer(
                        name=name, city=city, age=age, email=email)
                        new_customer.set_password(password)
                        session.add(new_customer)
                        session.commit()
                    except:
                        return False
                return True
            except IntegrityError:  # i want to catch only this error and fix all the rest
                session.rollback()

    def remove_customer(self, customer_email):

        with self.session() as session:
            try:
                customer = session.query(Customer).filter(func.lower(
                    Customer.email) == customer_email.lower()).first()
                if customer and customer.id > 2:
                    session.delete(customer)
                    session.commit()
                    return True

                elif customer.id < 3:
                    # the coloring of the text is cool when i use jupiter,
                    # I didn't check if it works on terminal
                    # wic is defined locally
                    # wic('you cannot remove a Libraryan from the list')
                    session.rollback()

            except AttributeError:
                # wic('Customer not found')
                session.rollback()

            except IntegrityError:  # i want to catch only this error and fix all the rest
                session.rollback()

            return False

    def loan_book(self, cust_id, book_id, loan_date=None, return_date=None):
        with self.session() as session:

            # for Librarian control I added the
            # option to determin the date or make it automatic
            if not loan_date:
                loan_date = datetime.date.today()

            try:
                loan = Loan(
                    cust_id=cust_id,
                    book_id=book_id,
                    loan_date=loan_date,
                    return_date=return_date
                )
                session.add(loan)
                session.commit()
                return loan.id

            except AttributeError:
                session.rollback()

            except IntegrityError:  # i want to catch only this error and fix all the rest
                # wic('loan already registered')
                session.rollback()

            return False

    # return a book
    def return_book(self, loan_id, return_date):
        with self.session() as session:
            try:
                session.query(Loan).filter(Loan.id == loan_id).\
                update({"return_date": return_date }, synchronize_session="fetch")
                session.commit()
                return True
            except IntegrityError:  # i want to catch only this error and fix all the rest
                session.rollback()

    def insert_customers(self):

        #(name, city, age, email, password)
        if self.has_data('customers'):
            return True

        costumers = [
            ('Eyal', 'Tel Aviv', '18', 'Eyal@JohnBryce.co.il', 'eyalgold'),
            ('Yair', "Ra'anana", 40, 'Yair.notkovich@gmail.com', 'hashthis'),
            ('BobSponge', 'Bikini Bottom', 30, 'sponge@test.com', '123456'),
            ('Patrick', 'Bikini Bottom', 30, 'pat@test.com', '123456'),
            ('Sandy', 'Bikini Bottom', 30, 'sandy@test.com', '123456'),
            ('Squidward', 'Bikini Bottom', 30, 'sqwid@test.com', '123456'),
            ('ms.Puff', 'Bikini Bottom', 30, 'Puff@test.com', '123456'),
            ('mr.Crab', 'Bikini Bottom', 30, 'Money@test.com', '123456'),
            ('Liat', "Ra'anana", 43, 'Liat@test.com', '123456'),
        ]

        for customer in costumers:
            self.add_customer(name=customer[0], city=customer[1],
                              age=customer[2], email=customer[3], password=customer[4])
# Ill need somthing bigger than this...

# ill generate some random ppl from a json list of first names
    def insert_big_cust(self):
        if self.has_data('customers'):
            #wic('customers already has startup data')
            return True
        self.insert_customers()
        with open("names.json", 'r') as js:
            name_list = json.loads(js.read())
        i = 0
        while i < 200:

            random_index = random.randint(0, len(name_list)-1)
            name = name_list[random_index]
            if self.add_customer(name, 'Happy place', random.randint(18, 90), name+'@test.com', '123456'):
                i += 1
            progress(i, 200, 'inserting customers')
        print('\n')
        return True

    def insert_books(self):
        if self.has_data('books'):
            #wic('books already has startup data')
            return True
        with open("books.json", 'r') as js:
            lists = json.loads(js.read())
        i = 0
        for list in lists["results"]["lists"]:
            for book in list["books"]:
                self.add_book(
                    book["title"],
                    book["author"],
                    random_published(),
                    random_type(),
                    img_url=book["book_image"],
                    description=book["description"]
                )
                i += 1
            progress(i, 230, 'inserting books')
        print('\n')

        return True

    def insert_loans(self):

        if self.has_data('loans'):
            #wic('loans already has startup data')
            return True
        for i in range(200):
            loan_date = rnd_loan_date()
            return_date = loan_date + \
                datetime.timedelta(days=random.randrange(1, 15))

            self.loan_book(random.randint(0, 200), random.randint(
                0, 200), loan_date=loan_date, return_date=random.choice([None, return_date, return_date]))
            progress(i, 199, 'inserting Loans')
        print('\n')
        return True
