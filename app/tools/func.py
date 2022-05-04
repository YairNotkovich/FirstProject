import datetime
import os


TYPES = [10,5,2]

# when getting the date a string, turn in back to list of int
# i need to meake sure to reformat the date to dd/mm/yyyy

def int_date(date, splitter ='/'):
    date = date.split(splitter)
    l_date = []
    for t in date:
        l_date.append(int(t))
    return l_date



def days_pass(loan_date,splitter = '-'):
    if type(loan_date) != datetime.date:
        date = int_date(loan_date, splitter)
        loan_date = datetime.date(date[0],date[1],date[2])
    today = datetime.date.today()
    delta = loan_date - today
    return delta.days



def return_list(string, splitter = ','):
    new_list = []
    splitted = string.split(splitter)
    for s in splitted:
       st= s.strip("()[]'")
       new_list.append(st)
    return new_list




def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def enum_book(loan_typ):
    book_types = enumerate(TYPES, start= 1)
    for index, typ in book_types:
        if loan_typ == index:
            return typ


def until(str_date, loan_type, is_enum = False):
    
    try:
        if not is_enum:
            loan_type = enum_book(loan_type)
        
        datetime_loan = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        return datetime_loan + datetime.timedelta(days = loan_type)
    except Exception as e:
        print(e)


def is_overdo(loan, loan_type, is_enum = False):
    if not is_enum:
        loan_type = enum_book(loan_type)
    if -(days_pass(loan,splitter= '-')) > loan_type:
        return True


def books_list(db,book):

    list =[]

    with db.session() as s:
        # id, name, author, img_url,description, year_published ,type
        for c in  s.query(book):
            book = (c.id, c.name, c.author,c.img_url, c.description, c.year_published, enum_book(c.type))
            list.append(book)

    return list