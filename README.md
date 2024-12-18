# How to Run the Project
# Prerequisites
Python 3.x installed on your machine.
<br>
SQLite3 installed for the database.
<br>
# Steps to Run
# 1. Clone the repository
git clone https://github.com/yourusername/library-management-system.git
<br>
cd library-management-system
<br>
# 2. Set Up Virtual Environment
python -m venv venv
<br>
source venv/bin/activate
# 3. Install Dependencies
pip install -r requirements.txt

# 4. Initialize the Database
python create_db.py

# 5. Run the Application
python main.py

# 6. Test the Api
Use Postman, cURL, or any HTTP client to test the API endpoints.

# Design Choices
1. Modular Architecture
<br>
<pre>
  The code is split into modules:
  Member.py: Handles user registration and login. 
  Borrow_book.py: Manages book borrowing and returning. 
  Search_book.py: Implements book search functionality. 
</pre>
2. Authentication
<br>
<pre>
  JSON Web Tokens (JWT) are used for user authentication to ensure secure access to API endpoints.
</pre>
3. Database
<br>
<pre>
  SQLite3 is used as the database for simplicity and portability.
  Tables:
  Members: Stores user information.
  Books: Stores details about available books.
  Borrowed_Books: Tracks borrowed and returned books.
</pre>
4. Search Functionality
<br>
<pre>
  The search endpoint allows users to search for books by any detail (e.g., title, author).
</pre>
<br>
<h1>Assumptions</h1>
<pre>
  1. Each user has a unique name for login.
  2. Users can borrow multiple books at a time but cannot borrow the same book twice.
  3. Token-based authentication ensures secure access to certain endpoints.
</pre>



