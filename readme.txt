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

# 19/01/23 Setup OR Model and Initialize HomePage #
---------------------------------------------------------
- setup Order Model
- register Order Model in AdminPage
- setup view and urls to display orders at homepage
- create static folder and style.css file
- update static policy in settings.py

# 19/01/23 Client Page - first step #
---------------------------------------------------------
- set static root in SETTINGS
- create 'client.html' in qr/templates
- create 'style.css' in src/static folder
- add some styling 
- update ATS_logo to static folder

# 20/01/23 Resolve conflicts + client front step 2 #
---------------------------------------------------------
- resolve conflicts
- styling client.html front and css

#21/01/23 Setting the iframe in client html #
---------------------------------------------------------
- setting iframe css for embed + rounded corners

# 22/01/23 Create QR code and basic logic for application (requirements.txt updated!)#
----------------------------------------------------------
- update home page with orders displayed in cards
- ceate detail page
- create add_order page with form and setup QR code generation in detail page
- create manual upload and download
- create test qr code view page for client side

#22/01/23 Styling home and addOrder form #
---------------------------------------------------------
- >pip install crispy-bootstrap5 - to install crispy forms
- update settings with above
- change styling in add+order.html by adding chrispy tag
- create navbar.html and include it in base.html
- move new order button to navbar + add bootstrap icon

#22/01/23 Styling Home / table with bootstrap icons #
---------------------------------------------------------
- change home function view to Home class ListView
- update url with above change
- update home.html - display data in table using bootstrap icons
- update style.css
- prevent some errors adding if check in qr_code.html

#22/01/23 Create Delete order functionality & add logo redirect to home #
---------------------------------------------------------
- create OrderDeleteView with template & url for delete confirmation
- update ASSEMBLE QR logo (span element) to route to home page

#22/01/23 New icons in Nabar / Home style for mobile #
---------------------------------------------------------
- add new icons in Navbar - user for user managment, Ad for chanel marketing,
- change button styling from primary to secondaray
- add return button in add_order.html
- mobile optimalization for table in home

#23/01/23 Updates icons in order table #
---------------------------------------------------------
- update icon for more friendly-use

#23/01/23 Water waste count for PDF pages #
--------------------------------------------------------
- > pip install PyPDF2==3.0.1 to install PyPDF2
- in models.py in file add validator to accept only PDF Files 
- in models.py add method to calculate PDF number of pages using PyPDF2
- use that function in views.py in order_detail to calculet water waste on manuals for production orderQuantity
- pass above to template and display it in order_detail.html

#23/01/23 Order Model update and changes in forms, views, template, navbar
--------------------------------------------------------
- update navbar logo to redirect to homepage
- update model with file2 field for ENG manual
- update models to set orderManual to True if file or file2 is used 
- update add_order view to set file fields to None if no file used
- update model, view, and detail template to count total water_waste from both file and file 2