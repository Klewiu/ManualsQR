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

#24/01/23 Styling order_detail.html - uncompleted#
--------------------------------------------------------
- styling order_detail

#25/01/23 Update Home to display total water waste#
-------------------------------------------------------
- create count_water_waste function in models.py
- update context in Home view with result of model method ( count_water_waste ) that is called on each Order object
- displaying water waste info in template in home.
- change global font according to UI project

#26/01/23 Add textPrinter.js to print text when no Order#
-------------------------------------------------------
- create textPrinter.js
- add it to home.html
- print text with typying animation when no Order data.


#28/01/23 Update views to delete files when object is deleted
-------------------------------------------------------
- pre_delete signal automatically deletes files when order object is deleted

#28/01/23 Styling order_detail.html - part 2#
-------------------------------------------------------
- create new method in models.py to get single page_count of file and file2
- update views.py
- styling order_detail

#29/01/23 Create live filter with HTMX at home.html
-------------------------------------------------------
- create search filter with HTMX
- reorganize code to partials

#29/01/23 Styling order_detail.html - part 3#
-------------------------------------------------------
- change layout to grid - cols and rows
- hide searchbar if no data

#29/01/23 Finished styling order_detail.html - part 4#
---------------------------------------------------------
- style changes
- hide searchbar if no data in home.html

#29/01/23 Update search and prepare input for video#
----------------------------------------------------------
- update search filtering
- create model field for video embed (make migrations to db)
- update orderVideo logic to automatically show video status

#30/01/23 Styling movie view in order_detail #
----------------------------------------------------------
- style movie view in order_detail

#31/01/23 Styling qr_code - cllient view#
---------------------------------------------------------
- styling page qr_code.html
- add TypeItjs text when no manual (soruce: https://www.typeitjs.com/)
- update models.py - add language field to files
- update TypeItjs text in home page.

#31/01/23 Pagination of object_list at home.html
---------------------------------------------------------
- add pagination to object_list.html at home.html

#01/02/2023 Styling qr_code - client view part 2
-------------------------------------------------------
- styling page qr_code.html 
- fixed rounded corners in iframe with -webkit-border-radius in css
- fixed video styling in order_detail.html