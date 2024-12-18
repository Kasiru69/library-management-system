import sqlite3

conn=sqlite3.connect("library.db",check_same_thread=False)
cursor=conn.cursor()

def book(book_name,title,author):
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name varchar(20),
        title varchar(20),
        author varchar(20)
    )
        '''
    )
    conn.commit()
    cursor.execute('''
        insert into books (book_name,title,author)
        values(?, ?, ?)
    ''',(book_name,title,author))
    conn.commit()
    cursor.execute('''
        select * from books
    ''')
    print(cursor.fetchall())

#book("The Great Gatsby", "The Great Gatsby", "F. Scott Fitzgerald")
#book("1984", "1984", "George Orwell")
#book("To Kill a Mockingbird", "To Kill a Mockingbird", "Harper Lee")
#book("Pride and Prejudice", "Pride and Prejudice", "Jane Austen")
#book("The Catcher in the Rye", "The Catcher in the Rye", "J.D. Salinger")
#book("Mansfield Park","Mansfield Park","Jane Austen")