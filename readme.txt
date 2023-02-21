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

#23/01/23 Order Model update and changes in forms, views, template, navbar #
--------------------------------------------------------
- update navbar logo to redirect to homepage
- update model with file2 field for ENG manual
- update models to set orderManual to True if file or file2 is used 
- update add_order view to set file fields to None if no file used
- update model, view, and detail template to count total water_waste from both file and file 2

#24/01/23 Styling order_detail.html - uncompleted #
--------------------------------------------------------
- styling order_detail

#25/01/23 Update Home to display total water waste #
-------------------------------------------------------
- create count_water_waste function in models.py
- update context in Home view with result of model method ( count_water_waste ) that is called on each Order object
- displaying water waste info in template in home.
- change global font according to UI project

#26/01/23 Add textPrinter.js to print text when no Order #
-------------------------------------------------------
- create textPrinter.js
- add it to home.html
- print text with typying animation when no Order data.


#28/01/23 Update views to delete files when object is deleted #
-------------------------------------------------------
- pre_delete signal automatically deletes files when order object is deleted

#28/01/23 Styling order_detail.html - part 2 #
-------------------------------------------------------
- create new method in models.py to get single page_count of file and file2
- update views.py
- styling order_detail

#29/01/23 Create live filter with HTMX at home.html #
-------------------------------------------------------
- create search filter with HTMX
- reorganize code to partials

#29/01/23 Styling order_detail.html - part 3 #
-------------------------------------------------------
- change layout to grid - cols and rows
- hide searchbar if no data

#29/01/23 Finished styling order_detail.html - part 4 #
---------------------------------------------------------
- style changes
- hide searchbar if no data in home.html

#29/01/23 Update search and prepare input for video #
----------------------------------------------------------
- update search filtering
- create model field for video embed (make migrations to db)
- update orderVideo logic to automatically show video status

#30/01/23 Styling movie view in order_detail #
----------------------------------------------------------
- style movie view in order_detail

#31/01/23 Styling qr_code - cllient view #
---------------------------------------------------------
- styling page qr_code.html
- add TypeItjs text when no manual (soruce: https://www.typeitjs.com/)
- update models.py - add language field to files
- update TypeItjs text in home page.

#31/01/23 Pagination of object_list at home.html #
---------------------------------------------------------
- add pagination to object_list.html at home.html

#01/02/2023 Styling qr_code - client view part 2 #
-------------------------------------------------------
- styling page qr_code.html 
- fixed rounded corners in iframe with -webkit-border-radius in css
- fixed video styling in order_detail.html

#02/02/2023 Styling qr_code - client view part 3 #
-------------------------------------------------------
- qr_code.html - put img inside button to add shadow
- add footer bootstrap icon (need styling...)
- update syles.css 

#03/02/2023 Add update form and style home table buttons
-------------------------------------------------------
- add update form
- show small text on mouseover on table buttons


#05/02/2023 Initial QR code print setup
-------------------------------------------------------
- add qr_print url
- initial qr code print setup

#05/02/2023 Styling footer in qr_code - client view part 4#
-------------------------------------------------------
- styling footer in qr_code
- disable hypersctipt search bar toggle

#05/02/2023 Add marketing app to provide marketing communication on carousel#
-------------------------------------------------------
-> python manage.py startapp marketing to start new app
-update settings with new app
- create urls.py and path to main marketing.html view
- crete forms.py in marketing
- create marketing model
- update admin.py

#05/02/2023 Fix navbar view in mobile #
------------------------------------------------------
- fixed navbar styling in mobile


#05/02/2023 Update the QR print with orderCompany and orderName
------------------------------------------------------
- update the QR print with orderCompany and orderName
- styling of the related pages

#06/02/2023 Marketing app - Create and List views#
------------------------------------------------------
- update modes.py with label, caption, slide
- update URLs with new views
- create marketing ListView and CreateView
- create templates for above views
- some styling

#06/02/2023 Marketing app - DeleteView#
------------------------------------------------------
- delete view for marketing
- style marketing - add table for data
- text changes in create_Ad

#06/02/2023 Marketing app - Update qr_code with marketing ad part1#
------------------------------------------------------
- pass marketing qs to qr_code view
- update carousel with marketing template tags and for loop

#07/02/2023 Carousel & Marketigng view updates#
------------------------------------------------------
- update Marketing model - only label and file
- update Carousel - only grapics + one default slide with ecology statistics
- fixed form to catch file and store in media
- add position:inherit in body in css to prevent clicking over layers

#08/02/2023 Carousel default + captions + water_waste
------------------------------------------------------
- add water_waste data to carousel in qr
- update style.css for captions in Carousel
- change water_watste displaing info when value changes for bigger

#08/02/2023 Delete slide when deleting marketing ad
------------------------------------------------------
- update views.py in marketign - add signals to delete slide(file)

#08/02/2023 Water_waste in home value changes on amount
------------------------------------------------------
- update home.html change L to m3 when value changes

#08/02/2023 Add validator for slides in marketing
------------------------------------------------------
- marketing model - validate slide height to be strictly 300px using Pillow
- marketing model - validate slide extension with FileExtensionValidator
- fix blank space in qr_code.html in title 

#09/02/2023 Create Notifications app with HTMX -p1
------------------------------------------------------
- create Notifications app
- add to settings
- include Notifications urls in main urls
- register new model in admin
- create Notification model
- create urls with HTMX urls
- create NotificationListView and add add_notification views
- create notifications.html with add form with HTMX
- create notifications-list with for loop on Notifications and error tag
- add link to new app in navbar

#09/02/2023 Typo & readme update
------------------------------------------------------
- update readme.txt
- typo in comments

#10/02/2023 Delete notifications with HTMX
------------------------------------------------------
- update urls with delete path in htmx patterns
- update views with delete_notification
- update notifications-list html with delet bootstrap icon and HTMX delet&target
- style htmx confirm with sweetalert2
- update base.html with script for htmx and csrf token for delete request

#11/02/2023 Delete notifications with HTMX - p2
------------------------------------------------------
- update delete confirm - change title to icon = "question"

#12/02/2023 Update add_order form
------------------------------------------------------
- update models.py with new fields (needs migration!)
- update add_order form with new file fields
- change template to use widget_tweaks with _hyperscript
- >pip install django-widget-tweaks
- update form logic and validation in forms.py

#12/02/2023 Update styling Notification & Marketigng    
------------------------------------------------------
- update create_Ad.html styling header + container
- update notifications-list.html - list size in mobile

#13/02/2023 Update add_order and update_order logic
------------------------------------------------------
- update models.py with validators from validators.py
- update add_order function to clear fileLanguage fields on error
- update update_order function with django messages
- update update_order template with widget_tweaks and javascript to delete fileLanguage when file is deleted
- update forms.py to override label names for file-loaded fields

#13/02/2023 Email on add_order with emial_list from Notification    
------------------------------------------------------
- update add_order with send_mail
- update settings with google gmail account
- update env

#13/02/2023 Fix styling in order_detail.html   
------------------------------------------------------
- fix div and classes in order_detail

#15/02/2023 Loading spinner with Bootstrap & AJAX   
------------------------------------------------------
- add Bootstrap loading spinner to order_detail & qr_code
- create spinner.js 
- import spinner.js + jquery in base.html
- import spinner.js + jquery in qr_code.html
- update syle.css with .spinner class

#15/02/2023 TypeIt in Marketing and Notifications 
------------------------------------------------------
- add TypeIt text in marketing when nothing has been added
- add TypeIt tex in notifications when nothing has been added
- add scripts for above
- plus some styling in marketing.html
- add new button in order_detail.html to view client page directly

#16/02/2023 Joing QR code with Default Image
------------------------------------------------------
- joining in qr/views.py default image qr_over_1.png with generated qr code using PILLOW and BytesIO
- update qr_print.html - styling PDF 3x8 with joined image + add BACK button to detail page
- add width for joined graphics in style.css
- make TypeIt text faster

#17/02/2023 qr_print new button save PNG
------------------------------------------------------
- add new button in qr_print to save qr_code in PNG
- update styling in order_detail.html

#18/02/2023 styling update_order        
------------------------------------------------------
- styling update_order
- add button in order_detail to update_order
- styling search bar in home.html

#19/02/2023 initial login/logout and user management setup       
------------------------------------------------------
- create login logic and template
- create logout route and view
- create adminpage panel

#19/02/2023 user register and logout     
------------------------------------------------------
- create register new user form
- create logout functionality
- initial setup for htmx user delete

#19/02/2023 delete user with HTXM and hyperscript
------------------------------------------------------
- delete user functionality with no rerender

#20/02/2023 fixed url display when cancel search button
------------------------------------------------------
- home.html search input - fixed url when cancel search button.

#20/02/2023 fixed styling and some errors
------------------------------------------------------
- marketing.html - hide table when no content was added
- qr models.py - higher max_length in order.company & order.name
- order_detail - styling buttons - same color as in home in order table
- qr_code - different styling for only one manual
- qr_code - set carousel speed
- spinner.js - add if to prevent script err when no movie
- style.css - new class for qr_code with one manual
- update.html - add back button
- user-list.html - hide in mobile, make responsive.

#20/02/2023 add user permissions and couple enhancements
------------------------------------------------------
- add user permissions
- add superuser(admin) field for creating and updating user
- add helper text for new & update order

#21/02/2023 qr_print changes
------------------------------------------------------
- add user permissions
- add superuser(admin) field for creating and updating user
- add helper text for new & update order
