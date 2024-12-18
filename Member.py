import sqlite3
import tokenn
#import flask

conn=sqlite3.connect("library.db",check_same_thread=False)
cursor=conn.cursor()

def register(name,password):
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(20),
        password varchar(20)
    )
        '''
    )
    conn.commit()
    cursor.execute('''
    INSERT INTO members (name, password)
    VALUES (?, ?)
    ''', (name,password))
    conn.commit()
    cursor.execute('''
        select * from members
    ''')
    dic=cursor.fetchall()
    print(dic)

def login(name,password):
    cursor.execute(f'''
        select id from members 
        where name=? and password=?
    ''',(name,password))
    dic=cursor.fetchall()
    if(len(dic)==0):
        return "no such member exist"
    else:
        Token=tokenn.generate_token(dic[0][0],name)
        print(Token)
        user_id=tokenn.decode_token(Token)
        return user_id

login("saptaswa","abc123")
#register("kasiru","xyz123")