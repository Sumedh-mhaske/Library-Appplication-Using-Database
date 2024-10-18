import sqlite3
import datetime

def get_date():
    date = datetime.date.today()
    
    full_date = date.day + '/' + date.month + '/' + date.year
    return full_date

def db_op(query):
    con = sqlite3.connect('library_app.db')
    con.execute(query)
    con.commit()
    con.close()

book_num = lambda : input('Enter Book Number : ')
stud_enr = lambda : input('Enter Student Enrollment Number : ')

def issue_book():
    pass

def return_book():
    pass

def view_not_ret():
    pass

def search_stud():
    pass

def search_book():
    pass

def stud_history():
    pass

def book_history():
    pass

def add_new_book():
    pass

def add_new_stud():
    enr = stud_enr()
    nm = input('Enter Student Name : ')
    mob = input('Enter Student Mobile Number : ')
    email = input('Enter Student Email : ')

    q = "insert into all_students value ({0}, '{1}', {2}, '{3}')".format(enr, nm, mob, email)
    db_op(q)
    print('New Student Added Succesfully...')

while True:
    input()
    print('Select operation')
    print('1 - Issue Book')
    print('2 - Return Book')
    print('3 - View Not Returned Book')
    print('Search Student')   
    print('Search Book')
    print('Student History')
    print('Book History')
    print('Add New Book')
    print('Add New Student')
    print('Exit')

    ch = int(input('Enter Your Choice : '))

    if ch == 1: issue_book()
    elif ch == 2: return_book()
    elif ch == 3: view_not_ret()
    elif ch == 4: search_stud()
    elif ch == 5: search_book()
    elif ch == 6: stud_history()
    elif ch == 7: book_history()
    elif ch == 8: add_new_book()
    elif ch == 9: add_new_stud()
    elif ch == 0: exit(0)
