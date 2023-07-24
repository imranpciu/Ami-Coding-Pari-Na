# Khoj The Search Django Web Application
# Description
Khoj The Search is a Django-based web application that allows users to perform searches on a list of input values. Users can enter a comma-separated list of integers as input values and then search for a specific value in the list. The application will display whether the search value is present in the input values or not.

# Features
1. User Authentication: The application provides user authentication using Django's built-in authentication system. Users can sign up, log in, and log out to access the search functionality.

2. Search Functionality: Users can enter a list of integers as input values and perform a search for a specific value within the input values. The application will display whether the search value is present or not.

3. History Tracking: The application stores the input values entered by each user along with the timestamp. Users can access their search history and view their previously entered input values.

4. API Endpoints: The application provides API endpoints to retrieve a user's input values within a specified date range. The API returns the input values in JSON format.

# Installation
1. Clone the repository to your local machine using the following command:
  > git clone https://github.com/imranpciu/Ami-Coding-Pari-Na.git
2. Navigate to the project directory:
  > cd Ami_Coding_Pari_Na
3. Create a virtual environment (optional but recommended) and activate it:
  > pipenv install (if you don't have pipenv install frist "pip install pipenv")
  > Active virtual environment: pipenv shell
4. Install the required packages:
  > pip install -r requirements.txt
5. Create a superuser to access the Django admin interface(optional):
  > python manage.py createsuperuser
6. Run the development server:
  > python manage.py runserver
7. Access the application in your web browser at: http://127.0.0.1:8000/
8. Finallay signup and then login
