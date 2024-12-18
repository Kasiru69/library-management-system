# How to Run the Project
# Prerequisites
Python 3.x installed on your machine.
<br>
SQLite3 installed for the database.
<br>
# Steps to Run
# 1. Clone the repository
git clone https://github.com/Kasiru69/library-management-system/tree/master
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
<h1>Assumptions</h1>
<pre>
  1. Each user has a unique name for login.
  2. Users can borrow multiple books at a time but cannot borrow the same book twice.
  3. Token-based authentication ensures secure access to certain endpoints.
</pre>
<h1>Limitations</h1>
<ol>
  <li><h2>Database</h2>
    <ul>
      <li>SQLite3 is used, which may not scale well for larger systems or concurrent users.</li>
      <li>No encryption is used for storing passwords (can be improved with hashing).</li>
    </ul>
  </li>
  <li><h2>Error Handling</h2>
    <ul>
      <li>Error messages are minimal and may not be user-friendly. This can be enhanced further.</li>
    </ul>
  </li>
  <li><h2>Token Expiry</h2>
    <ul>
      <li>The current implementation does not include token expiration for simplicity.</li>
    </ul>
  </li>
</ol>



