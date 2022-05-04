
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
# columns and data types
from sqlalchemy import Column, Integer, SmallInteger, String, Date, UnicodeText ,Boolean 
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, func
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()

class Book(Base):

    # As required
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable = False)
    author = Column(String(30), nullable = False)
    year_published = Column(Date, nullable = False)
    type = Column(SmallInteger, nullable = False) # the type is the loan period enumerated 1-3

    # My addition to the table
    img_url = Column(UnicodeText)
    description = Column(UnicodeText)

    # return value from enum
    def enum_book(self):
        book_types = enumerate([10,5,2], start= 1)
        for index, typ in book_types:
            if self.type == index:
                 return typ
            


class Customer(UserMixin, Base):

    # As required
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    city = Column(String(30))
    age = Column(SmallInteger)

    
    # My addition to the table
    email = Column( String(50), unique = True, index = True, nullable = False)
    hashed_password = Column(String(200), nullable = False)
    active = Column(Boolean, nullable = False, default=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Loan(Base):

    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cust_id = Column(None, ForeignKey('customers.id'))
    book_id = Column(None, ForeignKey('books.id'))
    loan_date = Column(Date, nullable = False)
    return_date = Column(Date)
    
