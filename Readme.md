# First Project  

### about me:
My name is Yair Notkovich.  
At the age of 40 (2022) I've decided to make a career change and take a leap in to  
software development.  
taking a 'Python Full-stack' course is my first step in to this world.

### The project:  
Creating a web application using `flask` and `sqlite3` database .  
The application will simulate Loans management in a book Library.  


[Source code on my github](https://github.com/YairNotkovich/FirstProject.git)  

[Deployed on Heroku](https://mypylibrary.herokuapp.com/) MIGHT TAKE A MINUTE TO LOAD  
heroku rests internal databases every hour or so

<br>
<br>

## Navigate the Document:
[Running the app](#running-the-app)
[Assignment as Given](#assignment-as-given)  
[Project Layout](#project-layout)  
[Writing Process:](#writing-process)
- [Defining the tables as requested](#defining-the-tables-as-requested)
- [common errors along development of the table classes](#common-errors-along-development-of-the-table-classes)
- [The tables in this project:](#the-tables-in-this-project)
- [Setting up the data base](#setting-up-the-data-base)
- [Creating a DAL and infrastructure](#creating-a-dal-and-infrastructure)
- [Testing](#testing)
- [Adding Logic](#adding-logic)
- [Web GUI](#web-gui)
- [ignoring with .gitignore](#ignoring-with-gitignore)  

[External link I referenced for help on this project:](#external-link-i-referenced-for-help-on-this-project)  
[TODO](#todo)  
[Problem - Solution](#problem---solution)

<br>
<br>


# Running the app:
> Before running! please make sure to install all required library's or run 'pip install -r requirements.txt'
> Please not: for showcase purpose at the first run, The app will put some DATA in the tables  
When you first run the app wait for the setup to finish:
```
Inserting Demo DATA,
this can take a while but its only for the first run
[============================================================] 100.0% ...inserting customers

[============================================================] 100.0% ...inserting books

[============================================================] 100.0% ...inserting Loans

Done!
```
 [The app is also deployed on heroku](https://mypylibrary.herokuapp.com/),  
 Note that is can take Up to a minute for the site to load if the database was reset by heroku

 > To run it from terminal please run 'py wsgi.py' or 'python3 wsgi.py

### Assignment as Given:

```
In this project you will implement a simple system to manage books library

 1. Create a simple sqlite database with 3 tables:
        Books:  
        • Id (PK)  
        • Name  
        • Author  
        • Year Published  
        • Type (1/2/3)  

        Customers:  
        • Id (PK)  
        • Name  
        • City  
        • Age 
        
        Loans:  
        • CustID  
        • BookID  
        • Loandate  
        • Returndate  

 2. The book type set the maximum loan time for the book:
        • 1 – up to 10 days  
        • 2 – up to 5 days  
        • 3 – up to 2 days  

 3. Create the DAL:  
        • Build a class for each entity  
        • Create a separate module for each class  
        • Build unit tests  

 4. Build a client application to use the DAL. Add the following operations (display a simple menu)
        • Add a new customer  
        • Add a new book  
        • Loan a book  
        • Return a book  
        • Display all books  
        • Display all customers  
        • Display all loans  
        • Display late loans  
        • Find book by name  
        • Find customer by name  
        • Remove book  
        • Remover customer 
```  
        

[back to top](#first-project) 
<br>
<br>

## Project Layout:
The project layout should comply with flask conventions  
i'll try to make it heroku ready  
##### ( I need to make sure i update it after any change i make ^^ )
        FS-LIBRARY/    
                ├── app/
                │   ├── __init__.py # initiation of the data base, app generator and blueprints registration
                |   ├── librarian.py
                │   ├── auth.py
                │   ├── main.py
                │   ├── test.ipynb
                │   ├── templates/
                │   │   ├── main/
                │   │   │  ├── index.html
                │   │   │  ├── about.html
                │   │   │  └── account.html
                │   │   │
                │   │   ├── auth/
                │   │   │  ├── login.html
                │   │   │  └── register.html
                │   │   │
                │   │   ├── librarian/
                │   │   │  ├── Librarian.html
                │   │   │  ├── add_book.html
                │   │   │  ├── add_customer.html
                │   │   │  ├── add_loan.html
                │   │   │  └── return_loan.html 
                │   │   │
                │   │   ├── base.html # the base tamplate
                │   │   └── mng-base.html # includes base.html
                │   │   
                │   ├── static/
                │   │   └── css/
                │   |   |   ├── style.css
                │   |   |   ├── more.css
                │   |   |   ├── dashboard.css
                │   |   |   ├── bootstrap.min.css
                │   |   |   └── bootstrap.min.css.map
                │   |   |── IMG/
                │   |   |       #images
                │   |   └── JS/
                │   │           some scripts
                │   └── database/
                │   │    ├──__init__.py
                │   │    └─ Library.sql
                │   │    └─ queries.py
                │   └── tools/
                │        ├──__init__.py
                │        └─ func.sql # functions used along the code
                │        └─ helpers.py # scripts for starting up the db
                │ 
                ├── requirements.txt
                ├── .gitignore 
                ├── books.json
                ├── names.json
                ├── Procfile
                ├── Readme.md
                └── wsgi.py

                   
[back to top](#first-project)                                
<br>
<br>

# Writing Process


### Defining the tables as requested
       This process toke me a really long time to figure out. I didn't want to go 'Ctrl+c Ctrl+v' with the example given in class  
       and tried to understand the "WHY" it was done that way.  
       I couldn't wrap my head around getting it to work when taking 'snippets' from several examples.  
       The problem was i was trying to combine different methods in the same process.  
       The solution was to be persistent with one method all way through.  



Eventually i went with the method shown at [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)


```python

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

# Example source: https://docs.sqlalchemy.org/en/13/orm/tutorial.html

```
### common errors along development of the table classes
I made changes to 'Customer' class along the way so after every change i made, i got the Error below  
when running the code to test it

for now the only way i know to overcome this error is to delete the database and make a new instance of it after every change

```python
---------------------------------------------------------------------------
File ~/python/Library V2/vlib/lib/python3.8/site-packages/sqlalchemy/orm/state.py:477, in InstanceState._initialize_instance(*mixed, **kwargs)
    474 manager.dispatch.init(self, args, kwargs)
    476 try:
--> 477     return manager.original_init(*mixed[1:], **kwargs)
    478 except:
    479     with util.safe_reraise():

File ~/python/Library V2/vlib/lib/python3.8/site-packages/sqlalchemy/orm/decl_base.py:1154, in _declarative_constructor(self, **kwargs)
   1152 for k in kwargs:
   1153     if not hasattr(cls_, k):
-> 1154         raise TypeError(
   1155             "%r is an invalid keyword argument for %s" % (k, cls_.__name__)
   1156         )
   1157     setattr(self, k, kwargs[k])

TypeError: 'password' is an invalid keyword argument for Customer
---------------------------------------------------------------------------
```

<br>
<br>


## The tables in this project:  
the tables are defined at database/models.py  

books - as required + added image url and description from json
customers - as required + email and password. also added active for adding/removing users. not functional
loans - as required
<br>
<br>

### Setting up the data base
I created the database as a class  
at database/__init__.py  
To initiate it you must create an instance of DB() and run instance.init_db  

```python
...
class DB():

    def __init__(self, metadata=Base, uri='', echo=False):

        self.engine = create_engine(uri, echo=echo)
        self.metadata = metadata

    def init_db(self):
        self.metadata.metadata.create_all(self.engine, checkfirst=True)
        self.insert_data()
...
```
<br>
<br>

### Creating a DAL and infrastructure
I chose to go with `SQLalchemy` and not `Flask-SQLalchemy` 
Flask-SQLalchemy is much more friendly to use but i wanted to deal with  
the regular SQLalchemy  

most of the DAL was defined in the DB class.  
using as 'db_name.func_name()'  
functions for repeating DB actions where created:  
```python
def add_book(self, book_name, author, year_published, book_type, img_url='', description='') # add a book
def add_customer(self, name, city, age, email, password) # add a customer
def loan_book(self, cust_id, book_id, loan_date=None, return_date=None) # create a loan
def return_book(self, loan_id, return_date) # return a book
```
for general use:
```python
def exe_stm(self, stm): # receives a SQL query in the form of plane text
def session(self): # returns an instance of Session()
```

<br>
<br>


### Testing  
While writing the code i tested the functions with tests.ipynb
<br>
<br>

### Adding Logic  
Executing the functions in DB and func.py is primarily done
inside the vies of main.py, auth.py and librarian.py
little modifications are made to the input before calling the functions
<br>
<br>

### Web GUI
I used album and dashboard bootstrap templates and modified the CSS to my desire
I found it very challenging getting th results i wanted
<br>
<br>

[back to top](#first-project) 

<br>
<br>

### ignoring with .gitignore
/env
<br>
<br>

### External link I referenced for help on this project:  
[mark down syntax](https://www.markdownguide.org/basic-syntax/)  
[git doc from class](https://docs.google.com/document/d/1A5I8fDshtHccZRMm91YZubH3bsow3Jh5wfIjfB0O9SE/edit?usp=sharing)  
[git-scm](https://git-scm.com/doc)  
[flask doc from class](https://docs.google.com/document/d/1KBvigLo1FXE2oPPp_B6h6op5vipb3gdac2Asi4k6jxk/edit?usp=sharing)  
[SQLAchemy Tutorials](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

[back to top](#first-project) 
<br>
<br>
# TODO
a sort of "Lion in the desert"  general guidelines TODO list

- [ ] Keep inline with the original task
- [ ] Update Readme.md
- [X] Define Tables()
- [x] add Customer()
- [x] login Customer ()
- [x] insert demo customers()
- [x] remove Customer()
- [ ] edit customer
- [x] add book()
- [x] remove book()
- [x] insert demo books()
- [x] loan book()
- [x] return book()
- [X] insert demo loans()
- [x] Librarian() - admin
- [X] Customer views
- [x] Librarian views
- [X] index.html
- [X] Base.html
- [x] Librarian.html
- [X] Customer.html
- [x] overdo 
- [x] about.html
- [x] Css
- [x] Cleanup



[back to top](#first-project) 
<br>
<br>
# Problem - Solution
Throughout the project i set my self objectives that created new problems  
here are some of them.  
P for problem and S for solution:

>#### P: I wanted a database filled wth data on first start up
>#### S:

>#### P: When trying to return a tuple from JINJA I get a string
>#### S: a func that returns list from string
```python
def return_list(string):
    new_list = []
    splitted = string.split(",")
    for s in splitted:
       st= s.strip("()[]'")
       new_list.append(st)
    return new_list

```

>#### P: When making a chnge to a book in the main page it scrolls away
>#### S: probably to learn JS. i did my best solving it with CSS
<br>

>#### P: The images for the books are not consistent in size
>#### S: modify the 'img-thumbnail' class to have a max height matching the smallest one i could find
>#### That class is now called 'book-img' 
```css
.book-img {
    padding: .25rem;
    background-color: #fff;
    border: 1px solid #dee2e6;
    border-radius: .25rem;
    max-width: 100%;
    max-height: 452px;
    height: auto
}
```
[back to top](#first-project) 