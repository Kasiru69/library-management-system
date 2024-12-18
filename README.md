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
The code is split into modules:
<br>
Member.py: Handles user registration and login. <br>
Borrow_book.py: Manages book borrowing and returning. <br>
Search_book.py: Implements book search functionality. <br>



