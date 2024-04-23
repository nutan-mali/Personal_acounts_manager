# House Inventory Management System

This Django project is designed to manage Expense, Tags, and equipment inventory. Users can define Expense, add Cost , and data and some details of Tag.

# Setup Instructions

Clone the repository:  git clone https://github.com/tnutan-mali/Personal_acounts_manager/

Install dependencies:  cd Expence
pip install -r requirements.txt

Run migrations: python manage.py migrate


Create a superuser (admin) to access the admin panel:  python manage.py createsuperuser


Start the development server:   python manage.py runserver


Access the application at http://localhost:8000/ in your web browser.

# Check URLs :

 http://localhost:8000/
   http://localhost:8000/expense_list/
   
   http://localhost:8000/add_expense/

   
   http://localhost:8000/tag_list/
   http://localhost:8000/add_tag/
   
   http://localhost:8000/delete/<int:id>/
   
  http://localhost:8000/room_report/ tag_report/<int:tag_id>/
    
  

# Directory Structure

house_inventory/: Main project directory.

house_app/: Django app for managing Expense and Tag.

models.py: Contains models for Expense, Tag, .

views.py: Includes views for creating, listing, and managing Expense and Tag.

forms.py: Django forms for creating and editing Tag, Expense.

templates/: HTML templates for user interface.

admin.py: Admin panel configurations.

static/: Static files like CSS, JavaScript, images, etc.

requirements.txt: Lists project dependencies.

README.md: This file.



