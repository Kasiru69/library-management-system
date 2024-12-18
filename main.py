import create_db
from flask import Flask, request, jsonify
import Member
import Borrow_book
import Search_book

app=Flask(__name__)

#user register
@app.route('/request',methods=['POST'])
def Register():
    data=request.get_json()
    print(f"{data['name']} {data['password']}")
    Member.register(name=data['name'],password=data['password'])
    return jsonify(data)

#user login
@app.route('/login',methods=['POST'])
def Login():
    data=request.get_json()
    print(f"{data['name']} {data['password']}")
    user_id=Member.login(name=data['name'],password=data['password'])
    return jsonify(user_id)

#borrow books
@app.route('/borrow',methods=['POST'])
def Borrow():
    data = request.get_json()
    status=Borrow_book.borrow(data['id'],data['book'])
    return jsonify(status)

#return borrowed book
@app.route('/return_book',methods=['POST'])
def return_book():
    data = request.get_json()
    status=Borrow_book.borrow(data['id'],data['book'])
    return jsonify(status)

#search book
@app.route('/search_book',methods=['POST'])
def Searchbook():
    data = request.get_json()
    list_of_books=Search_book.Book(data)
    return list_of_books

if __name__=='__main__':
    app.run(debug=True)
