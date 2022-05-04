import datetime
import random
import json


'''
mostly helper functions to assist with the
automation of crating values fot the tables
'''
DATE_FORMAT = '%d/%m/%y'


# generat random published date. to be used in insert books
def random_published():
    ago = random.randrange(60,365*5) # from 2 monthes ago to 5 years ago
    today = datetime.date.today()
    delta = today - datetime.timedelta(days = ago)
    return delta

# a range that covers all 3 types of loaning period and also overdo
def rnd_loan_date():
    ago = random.randrange(0,15)
    today = datetime.date.today() # also datetime format
    return today - datetime.timedelta(days = ago)

# warning in console - i am sure there is another way to do it...
# was easier for me to spot my prints when debuging
def wic(color,text):
    print(f'''{color}{text}\033[0m''')

# returns random int for the book type 1-3
def random_type():
    return random.randrange(1,4)

# now i have a new problem... if a customer's id is 5 and book id is 21
# pk will be the same as a customer with id 52 and book id 1
# so i need single digits to be in the format of 01 05 ets... 
# or simply put, customer id and book id will alway be separated by a 0
def generate_primary(c, b, d):

    striped_date = d.strftime("%d%m%y")
    stringed_cust_id = str(c)
    stringed_book_id = str(b)
    str_pk = striped_date + '0' + stringed_cust_id +'0' + stringed_book_id
    return int(str_pk)

# a function called at initial setup to put some customers in the database



# The MIT License (MIT)
# Copyright (c) 2016 Vladimir Ignatev
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('\033[94m[%s] %s%s ...%s\r\033[0m' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)



class colors:
    HEADER = ('\033[95m').strip("'")
    OKBLUE = ('\033[94m').strip("'")
    OKGREEN = ('\033[92m').strip("'")
    WARNING = ('\033[93m').strip("'")
    FAIL = ('\033[91m').strip("'")
    ENDC = ('\033[0m').strip("'")
    BOLD = ('\033[1m').strip("'")
    UNDERLINE = ('\033[4m').strip("'")
