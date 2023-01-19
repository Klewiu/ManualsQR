# 18/01/23 Initial Commit #
---------------------------------------------------------

# 18/01/23 Django Setup #
---------------------------------------------------------
- >python -m venv venv  - to create virtual environment
- switch to venv env by typing: >venv/scripts/activate
- >pip install django - to install django
- add .gitignore
- >django-admin startproject manualsqr - to create a new project
- change main django project name to src
- >pip install python-dotenv - install package to secure SECRET_KEY
- create .env file to store SECRET_KEY 
- change SETTINGS to use dotenv
- run >python manage.py migrate to test it

# 18/01/23 Install Pipreqs #
--------------------------------------------------------
- >pip install pipreqs - generates requirements.txt automaticly
- >pipreqs /path/to/project/home/location - to create requirements.txt

# 19/01/23 Install Bootstrap5 / test view #
--------------------------------------------------------
- >pip install django-bootstrap-v5
- add 'bootstrap5' to settings
- create templates folder in src and create 'base.html' in templates folder
- change in settings DIRS to 'DIRS': [BASE_DIR / 'templates'],
- >python manage.py startapp qr - create new app qr 
- create urls.py in new app
- use include in urls.py in manualsqr to include qr urls.py.
- update views.py in qr with test function
- create test.html template and store in templates/qr in qr app