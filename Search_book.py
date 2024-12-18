import sqlite3

conn=sqlite3.connect("library.db",check_same_thread=False)
cursor=conn.cursor()

def Book(book_details):
    list_of_books=[]
    print(book_details)
    cursor.execute('''
     select * from books
     where id=? or book_name=? or title=? or author=?
    ''',(book_details['id'],book_details['book_name'],
         book_details['title'],
         book_details['author']
         ))
    list_of_books=cursor.fetchall()
    return list_of_books

