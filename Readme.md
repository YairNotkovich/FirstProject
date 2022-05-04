# First Project  

### about me:
My name is Yair Notkovich.  
At the age of 40 (2022) I've decided to make a career change and take a leap in to  
software development.  
taking a 'Python Full-stack' course is my first step in to this world.

### The project:  
Creating a web application using `'flask'` and `'sqlite3'` database .  
The application will simulate Loans management in a book Library.  


[Source code on my github](https://github.com/YairNotkovich/Library-V3 "some files shown on the project layout are not included becaus they are set to be ignored by '.gitignore'.  
the zip file submitted will include all the files and folders.")  

<br>
<br>

## Navigate the Document:

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
<br>

# Running the app:
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
<br>
## Project Layout:
The project layout should comply with flask conventions  
i'll try to make it heroku ready  
##### ( I need to make sure i update it after any change i make ^^ )
        BOOKSTORE/    
                ├── app/
                │   ├── __init__.py # initiation of the data base, app generator and blueprints registration
                |   ├── models.py
                │   ├── auth.py
                │   ├── main.py
                │   ├── templates/
                │   │   ├── base.html # the base tamplate
                │   │   ├── auth/
                │   │   │   ├── login.html
                │   │   │   └── register.html
                │   │   └── main/
                │   │       ├── create.html
                │   │       ├── index.html
                │   │       └── update.html
                │   ├── static/
                │   │   └── css/
                │   |   ├── style.css
                    │   └── IMG/
                    │           #images
                    └── database/
                        ├── db.py
                        └─ Library.sql
                ├── requirements.txt           

                ├── tests/
                │       ├──testquery.ipynb
                ├── venv/
                └── .gitignore
                   
[back to top](#first-project)                                
<br>
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
<br>
<br>


### Setting up the data base

<br>
<br>


### Creating a DAL and infrastructure

<br>
<br>


### Testing

<br>
<br>

### Adding Logic

<br>
<br>

### Web GUI

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
- [ ] edit customer() - add the details that were not entered when registering
- [ ] Librarian() - admin
- [X] Customer views
- [ ] Librarian views
- [X] index.html
- [X] Base.html
- [ ] Librarian.html
- [X] Customer.html
- [ ] overdo 
- [ ] about.html
- [ ] Css
- [ ] Cleanup



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
