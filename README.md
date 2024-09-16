This project uses Django framework, make sure python is installed. Check with: python --version
If not installed, download and install it from python.org.

Pip is a python package manager. It should come with Python, but you can check with: pip --version
If not, install it: python -m ensurepip --upgrade

This project needs a virtual envirnment to run as it's a good practice to use a virtual environment to isolate your Django project dependencies.
To install: pip install virtualenv

Clone this repo to your desired destination/repository. https://github.com/Rafikitaban/python-project.git

Move into the cloned directory: cd python-project

Create a Virtual Environment using the command: python -m virtualenv (name your virtualenv)

Activate the Virtualenv.
On Windows:(name of your virtualenv)\Scripts\activate
On macOS/Linux: source (name of your virtualenv)/bin/activate
Note: when using gitbash, this command works: source (name of your virtualenv)\Scripts\activate

Ensure that MySQL is installed and running on your machine. You also need the Python MySQL client library to allow Django to connect to MySQL
Install mysql client via pip using the command: pip install mysqlclient

Configure your database settings in your settings.py file and the database setting should be configured for MySQL. Update it  as follows:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # Or your MySQL server's IP
        'PORT': '3306',  # Default MySQL port
    }
}
Replace 'your_database_name', 'your_mysql_user', and 'your_mysql_password' with the actual database name and credentials.

Create your database in MySQL before making migrations using the following commands:
mysql -u your_mysql_user -p
CREATE DATABASE your_database_name;

Remember to use your own credentials in ‘your_mysql_user’ and your password in -p and your own database name in ‘ your_database_name’
Now, you can run the python manage.py migrate command. This will apply all the migrations and set up the database schema in MySQL.
Use the command: python manage.py migrate

Make sure django is installed. Check with: python -m django --version / django-admin --version
If not installed, then use the command: pip install django / python -m pip install django

Move into the project repository: cd maycohort
Run the project using this command: python manage.py runserver

Visit http://127.0.0.1:8000/ to view the project and use CTRL + C to close it when done.
To deactivate the virtual env, move back to the cloned repo and use the command: deactivate

