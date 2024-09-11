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

Make sure django is installed. Check with: python -m django --version / django-admin --version
If not installed, then use the command: pip install django / python -m pip install django

Move into the project repository: cd maycohort
Run the project using this command: python manage.py runserver

Visit http://127.0.0.1:8000/ to view the project and use CTRL + C to close it when done.
To deactivate the virtual env, move back to the cloned repo and use the command: deactivate

