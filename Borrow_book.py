import time
import hmac
import hashlib
import base64
import sqlite3
import tokenn

conn=sqlite3.connect("library.db",check_same_thread=False)
cursor=conn.cursor()
SECRET_KEY="abcdefghijklmnopqrstuvwxyz"

def is_logged_in(token):
    if not token:
        return False
    try:
        parts = token.split('|')
        if len(parts) != 4:
            return False
        user_data = '|'.join(parts[:3])
        received_token = parts[3]
        expected_token = base64.b64encode(
            hmac.new(SECRET_KEY.encode(), user_data.encode(), hashlib.sha256).digest()).decode('utf-8')
        if hmac.compare_digest(expected_token, received_token):
            return True
        else:
            return False
    except Exception as e:
        return False

def enter_book(user_id,book_id,book_name,title,author):
    print(f"{user_id} {book_id} {book_name} {title} {author}")
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS borowedbooks (
        user_id INTEGER,
        book_id INTEGER,
        book_name varchar(20),
        title varchar(20),
        author varchar(20),
        PRIMARY KEY (user_id, book_id)
    )
        '''
    )
    conn.commit()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS history (
        user_id INTEGER,
        book_id INTEGER,
        status varchar(20),
        PRIMARY KEY (user_id, book_id)
    )
        '''
    )
    conn.commit()
    cursor.execute('''
        select * from borowedbooks
        where user_id=? and book_id=? and book_name=? and title=? and author=?
    ''',(user_id,book_id,book_name,title,author))
    list=cursor.fetchall()
    print(list)
    if(len(list)==0):
        cursor.execute('''
            insert into borowedbooks(user_id,book_id,status)
            values(?,?,?,?,?)
        ''',(user_id,book_id,"borrowed"))
        conn.commit()
        cursor.execute('''
                    insert into history(user_id,book_id,book_name,title,author)
                    values(?,?,?,?,?)
                ''', (user_id, book_id, book_name, title, author))
        conn.commit()
        cursor.execute('''
            select * from borowedbooks
        ''')
        print(cursor.fetchall())
    else:
        print("already borowed this book")

def borrow(user_id,book_details):
    cursor.execute('''
        select name from members
        where id=?
    ''',(user_id))
    user_name=cursor.fetchall()[0][0]
    print(user_name)
    user_token=tokenn.generate_token(user_id,user_name)
    if is_logged_in(user_token):
        print("user is logged in")
        cursor.execute('''
            select * from books
            where book_name=? or title=? or author=?
        ''',(book_details,book_details,book_details))
        book=cursor.fetchall()
        print(book)
        user_id=tokenn.decode_token(user_token)
        for book in book:
            book_id=book[0]
            book_name=book[1]
            title=book[2]
            author=book[3]
            enter_book(user_id,book_id,book_name,title,author)
            return user_id
    else:
        print("User is not logged in")

def return_book(user_id,book_details):
    #user_id = tokenn.decode_token(user_token)
    cursor.execute('''
     delete from borowedbooks
     where user_id=? and (book_id=? or book_name=? or title=? or author=?)
    ''',(user_id,book_details,book_details,book_details,book_details))
    cursor.execute('''
                select * from borowedbooks
            ''')
    print(cursor.fetchall())
    cursor.execute('''
                select * from books
                where id=? or book_name=? or title=? or author=?
            ''', (book_details,book_details, book_details, book_details))
    book = cursor.fetchall()
    cursor.execute('''
                insert into borowedbooks(user_id,book_id,status)
                values(?,?,?,?,?)
            ''', (user_id, book[0][0], "returned"))
    conn.commit()

#borrow("2|saptaswa|1734529531|uCT/leKWzERwHFhKJaEFSfizJv7GQ0ZchU4M4RuSOZc=","Harper Lee")
#return_book("2|saptaswa|1734529531|uCT/leKWzERwHFhKJaEFSfizJv7GQ0ZchU4M4RuSOZc=","Harper Lee")
# cursor.execute('''
#                 select * from borowedbooks
#             ''')
# print(cursor.fetchall())