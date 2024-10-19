import sqlite3
import datetime

def get_date():
    date = datetime.date.today()
    
    full_date = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    return full_date


def db_op(query):
    con = sqlite3.connect('library_app.db')
    con.execute(query)
    con.commit()
    con.close()


book_num = lambda : input('Enter Book Number : ')
stud_enr = lambda : input('Enter Student Enrollment Number : ')


def issue_book():
    bnum = book_num()
    senr = stud_enr()
    idate = get_date()
    ret_date = 'NA'
    ret_status = 'NO'

    q = "insert into all_issued values ({0}, {1}, '{2}', '{3}', '{4}')".format(bnum, senr, idate, ret_date, ret_status)
    db_op(q)
    print('Book Issued Succesfully...')


def return_book():
    bnum = book_num()
    rdate = get_date()

    q = "update all_issued set return_date = '" + rdate + "', return_status = 'YES' where book_number = " + bnum
    db_op(q)
    print('Data Updated Succesfully..')


def view_not_ret():
    q = "select * from all_issued where return_status = 'NO'"

    con = sqlite3.connect('library_app.db') 
    cur = con.cursor()
    cur.execute(q)
    data = cur.fetchall()

    for d in data:
        print(d, end='\n\n')

    cur.close()
    con.close()


def search_stud():
    enr = stud_enr()

    q = 'select student_name, student_mobile_num, student_email from all_students where stud_enrollment_num = ' + enr
    con = sqlite3.connect('library_app.db')
    cur = con.cursor()
    cur.execute(q)

    data = cur.fetchone()
    print('Student Name :', data[0])
    print('Student Mobile Number :', data[1])
    print('Student Email :', data[2])

    cur.close()
    con.close()


def search_book():
    bnum = book_num()

    q = 'select book_title, book_author, book_publication from all_books where book_number = ' + bnum
    con = sqlite3.connect('library_app.db')
    cur = con.cursor()
    cur.execute(q)

    data = cur.fetchone()
    print('Book Title :', data[0])
    print('Book Author Name :', data[1])
    print('Book Publications :', data[2])

    cur.close()
    con.close()


def stud_history():
    enr = stud_enr()

    q = 'select book_number, issue_date, return_date, return_status from all_issued where stud_enrollment_num = ' + enr
    con = sqlite3.connect('library_app.db')
    cur = con.cursor()
    cur.execute(q)

    data = cur.fetchall()
    for d in data:
        print('Book Issued :', d[0])
        print('Book Issued Date :', d[1])
        print('Book Returned Date :', d[2])
        print('Book Returned Status :', d[3])

    cur.close()
    con.close()


def book_history():
    bnum = book_num()

    q = 'select stud_enrollment_num, issue_date, return_date, return_status from all_issued where book_number = ' + bnum
    con = sqlite3.connect('library_app.db')
    cur = con.cursor()
    cur.execute(q)

    data = cur.fetchall()
    for d in data:
        print('Book Issued Student Enrollment Number :', d[0])
        print('Book Issued Date :', d[1])
        print('Book Returned Date :', d[2])
        print('Book Returned Status :', d[3])

    cur.close()
    con.close()


def add_new_book():
    bnum = book_num()
    btitle = input('Enter Book Title : ')
    bauth = input('Enter Book Author Name : ')
    bpub = input('Enter Book Publications Name : ')

    q = "insert into all_books values ({0}, '{1}', '{2}', '{3}')".format(bnum, btitle, bauth, bpub)
    db_op(q)
    print('New Book Added Succesfullly...')


def add_new_stud():
    enr = stud_enr()
    nm = input('Enter Student Name : ')
    mob = input('Enter Student Mobile Number : ')
    email = input('Enter Student Email : ')

    q = "insert into all_students values ({0}, '{1}', {2}, '{3}')".format(enr, nm, mob, email)
    db_op(q)
    print('New Student Added Succesfully...')


while True:
    input()
    print('Select operation')
    print('1 - Issue Book')
    print('2 - Return Book')
    print('3 - View Not Returned Book')
    print('4 - Search Student')   
    print('5 - Search Book')
    print('6 - Student History')
    print('7 - Book History')
    print('8 - Add New Book')
    print('9 - Add New Student')
    print('0 - Exit')

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
