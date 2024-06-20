# Subsurface
## Milestone Project 4 - Full Stack Development with Django
  * [Live link](https://subsurface-03d2c6e34bd7.herokuapp.com/)
  * [Wireframes](#)
  * [GitHub Repository](https://github.com/parduckids/milestone-project-four)
  * [Testing docs](/TESTING.md)

![image](/static/readme/3-devices-black.png)

## The Idea:

* "Subsurface" is your gateway to the underground music scene, offering the ultimate destination for underground music events and ticket sales across the UK's major cities. Our focus lies on the raw, unfiltered sounds of techno, house, noise, and experimental music. While countless event websites exist, none truly cater to the authentic underground scene. Subsurface fills that void, bringing you closer to the music that matters.

* Whether you're a devoted fan of the underground or a curious newcomer, Subsurface provides an unparalleled selection of events often overlooked by mainstream platforms. Join us and immerse yourself in the vibrant, pulsating heart of the UK's underground music culture.

* "Subsurface" is developed as my Milestone Project 4 for the Code Institute's Diploma in Web Application Development course. This project incorporates a range of technologies, including HTML, CSS, JavaScript, Django, and PostgreSQL. Multiple Django apps were used to structure the application effectively, and Stripe integration was implemented to handle secure ticket transactions.
---
- Please be aware that this web app was created as a portfolio project only, not for commercial or public use.

## Contents

- [User Experience](#user-experience)
  * [User Stories](#user-stories)
    + [Viewing and Navigation](#viewing-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and Searching](#sorting-and-searching)
    + [Purchasing and Checkout](#purchasing-and-checkout)
    + [Event Management](#event-management)
    + [Ticket Management](#ticket-management)
- [Design](#design)
  * [Overview](#overview)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Favicon](#favicon)
  * [Color Scheme](#color-scheme)
- [Features](#features)
  * [Navigation Bar](#navigation-bar)
  * [Footer](#footer)
  * [Authentication](#authentication)
  * [Messages](#messages)
  * [All Pages and CRUD Functionality](#all-pages-and-functionality)
- [Data Model](#data-model)
- [Tools & Documentations](#tools--documentations)
  * [Payments](#payments)
  * [Languages Used](#languages-used)
  * [Libraries & Frameworks](#libraries--frameworks)
  * [Other Tools](#other-tools)
  * [Design & Image Editing](#design--image-editing)
- [Extra Features for the Future](#extra-features-for-the-future)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)
  * [Credit for Content](#credit-for-content)
  * [Acknowledgements](#acknowledgements)

# User Experience
## User Stories
### Viewing and Navigation

| As a/an      | I want to be able to...                                               | So that I can...                         |
|--------------|----------------------------------------------------------------------|------------------------------------------|
| Event-goer   | View a list of events                                                | Quickly compare and select different event options |
| Event-goer   | View individual event details                                        | Find out further information about the event |
| Event-goer   | Quickly identify key features of events through icons and keywords   | Decide if it's appropriate for the type of event I want to attend |
| Event-goer   | See the price update automatically when I select ticket quantity     | Help me not to overspend |
| Event-goer   | See available dates                                                  | Know the event is available when I book it |
| Event-goer   | See the number of available tickets for each event                   | Know how many tickets are left before I make a decision |

### Registration and User Accounts

| As a/an        | I want to be able to...                        | So that I can...                               |
|----------------|-----------------------------------------------|------------------------------------------------|
| Registered User | Easily register for an account                | Have a personal account to for keeping track of my tickets |
| Registered User | Easily log in or log out                      | Access my personal info                        |
| Registered User | Easily recover my password                    | Access my account even if I've forgotten my password |
| Registered User | Have a personalized user page for my tickets            | See my personal order history use my tickets when needed |
| Registered User | Change my password                            | Ensure my account remains secure               |
| Registered User | Change my email                               | Keep my contact information up-to-date         |
| Registered User | Sign out                                      | Securely log out of my account                 |

### Sorting and Searching

| As a/an      | I want to be able to...                                                        | So that I can...                         |
|--------------|-------------------------------------------------------------------------------|------------------------------------------|
| Event-goer   | Sort/filter events by dedicated filters (e.g., city, date, genre)             | Easily identify suitable options for my experience |
| Event-goer   | Search for an event by name, description, or key feature                      | Find a specific event I'd like to attend |

### Purchasing and Checkout
- Registered User

| As a/an      | I want to be able to...                                                      | So that I can...                         |
|--------------|-----------------------------------------------------------------------------|------------------------------------------|
| Event-goer   | Select the event I want and book through the event page                     | Start the booking process                |
| Event-goer   | Easily enter my payment information                                         | Check out quickly with no hassles        |
| Event-goer   | View an order confirmation after checkout                                   | Know my order has gone through and I haven't made any mistakes |
| Event-goer   | Have my ticket purchase connected with my username                          | Easily access and manage my tickets      |

### Event Management
- (Administrator) 

| As a/an          | I want to be able to...                                 | So that I can...                         |
|------------------|---------------------------------------------------------|------------------------------------------|
| Administrator    | Upload, edit, and delete events                         | Manage the event listings efficiently    |
| Administrator    | Set ticket prices                                       | Ensure correct pricing for various events|
| Administrator    | Set the maximum ticket amount                           | Control the number of tickets available  |
| Administrator    | Display the number of available tickets                 | Inform event-goers of ticket availability|

### Ticket Management
- Registered User

| As a/an      | I want to be able to...                                  | So that I can...                         |
|--------------|---------------------------------------------------------|------------------------------------------|
| Event-goer   | Check my tickets in the "My Tickets" page                | Keep track of my bookings                |
| Event-goer   | Generate a QR code for my ticket                         | Use it to get into the venues            |


# Design

## Overview
The website design of "Subsurface" embodies a sleek, dark, and edgy aesthetic, perfectly suited for an underground scene event web app. The color scheme features deep blacks and muted grays, creating a mysterious and immersive atmosphere. The white text and yellow buttons add a touch of contrast, enhancing usability and drawing attention to key actions.

### Typography
- I use '[Cutive Mono]' and '[Major Mono Display]', these monospaced typefaces contribute to the site's edgy and modern aesthetic, with 'Cutive Mono' providing a clean, readable text and 'Major Mono Display' adding a bold, striking element to headings and key information.
- The fonts are imported from [Google Fonts](https://fonts.google.com/)
### Imagery

- To present the website with content, I sourced event images from [Resident Advisor](https://www.residentadvisor.net/) and [Headfirst Bristol](https://www.headfirstbristol.co.uk/). These images add authenticity and visual appeal to the site, showcasing the vibrant underground events featured on "Subsurface".

### Favicon
![image](/static/readme/favicon.png)
- Made with: [Canva](https://www.canva.com/)
- Conversion to .ico file: [Favicon.io](https://favicon.io/)

## Color scheme

![image](/static/readme/colors.png)
- Raisin Black (#28282B): A deep, dark gray that adds a touch of sophistication and mystery, perfect for creating a moody and intense atmosphere.

- Black (#000000): The ultimate dark color, providing a strong contrast and a clean, modern look, essential for a minimalist design.

- Slate Gray (#6C757D): A muted gray with a slight blue tint, offering a balanced, neutral tone that complements the darker elements without overpowering them.

- White (#FFFFFF): A pure, clean white that ensures clarity and readability, providing a stark contrast against the darker colors.

- Amber (#FFC007): A vibrant yellow that stands out, used to highlight key actions and elements, adding a touch of warmth to the design.






# Features

## Navigation Bar
- Logged Out
![image](/static/readme/navbar-logged-out.png)
- Logged in as user
![image](/static/readme/navbar-logged-in-as-user.png)
- Logged in as administrator
![image](/static/readme/navbar-logged-in-as-admin.png)

## Footer
- Logged out
![image](/static/readme/footer-logged-out.png)
- Logged in
![image](/static/readme/footer-logged-in.png)
- Logged in - Already subscribed to newsletter
  - When user is subscribed to the newsletter, it's stored in session and the email field and button is hidden
![image](/static/readme/footer-subscribed-in-session.png)


## Authentication 
### Django allauth templates redesigned

- Log In
![image](/static/readme/login.png)
- Log Out
![image](/static/readme/log-out.png)
- Register
![image](/static/readme/register.png)
- Change Email
![image](/static/readme/change-email.png)
- Change Password
![image](/static/readme/change-password.png)



## Messages 
- Upload event
![image](/static/readme/event-uploaded.png)
- Edit event
![image](/static/readme/event-edited.png)
- Delete event
![image](/static/readme/event-deleted.png)
- Ticket purchase successful
![image](/static/readme/ticket-purchase.png)
- Ticket purchase Issue
![image](/static/readme/purchase-cancelled.png)
- Subscribed to newsletter
![image](/static/readme/subscribed.png)
- Signed In
![image](/static/readme/signed-in.png)
- Signed Out
![image](/static/readme/signed-out.png)
- Registration - Confirmation email sent
![image](/static/readme/email-confirmation.png)
- Registration - Email Confirmed
![image](/static/readme/confirmed-message.png)



## All Pages and Functionality

### Index (Home) Page
- Displays featured events, which can be set on the create event page and later updated on the edit event page.
- The "Tell me more" button navigates users to the event detail page.
- The "Buy Tickets" button directs users to the login page (if not registered) or the buy ticket page.
![image](/static/readme/index.png)

### Events Page
- Shows all current and upcoming events, with filtering options by date, genre, and city. The page title updates based on the selected filters.
- The "Tell me more" button navigates users to the event detail page.
- The "Buy Tickets" button directs users to the login page (if not registered) or the buy ticket page.
![image](/static/readme/events.png)

### Filtered Events Page
- Displays events based on selected filters, with the title reflecting the filter criteria.
![image](/static/readme/filtered-events.png)

### Events Page (no events)
- Displays a message to the user when no events are available.
![image](/static/readme/no-events.png)

### Event Detail Page
- Shows a large image, event description, music link, and details about the event's date, venue, address, etc.
- Includes a "Buy Ticket" button for ticket purchases.
![image](/static/readme/event-details-1.png)
![image](/static/readme/event-details-2.png)

### About Page (with contact form)
- Explains the purpose and creation of Subsurface.
- Provides a contact form accessible to both registered and non-registered users.
![image](/static/readme/about.png)

### My Tickets Page
- Allows users to view their purchased tickets.
- Displays QR codes for event entry.
![image](/static/readme/my-tickets.png)

### QR Code for Tickets (with carousel if more than 1 ticket)
- Shows QR codes for purchased tickets. If more than one ticket is purchased, a carousel with incremented ticket numbers is available.
- QR codes are static; dynamic QR code generation will be a future enhancement.
![image](/static/readme/ticket-qr.png)

### Buy Ticket Page
- Allows users to purchase tickets for events.
- Prepopulates the username and adjusts the price based on the quantity selected.
![image](/static/readme/buy-ticket.png)
- Redirects users to the Stripe checkout page after entering details.
![image](/static/readme/finalise-ticket.png)


### Create Event Page
- Enables administrators to add new events.
- Supports image uploads via Cloudinary, including options for web URL and direct image upload.
- Uses a default image if no image is uploaded.
![image](/static/readme/upload-1.png)
![image](/static/readme/upload-2.png)

### Manage Events Page
- Allows administrators to view and modify all current, upcoming, and past events.
![image](/static/readme/manage.png)


### Delete Event Page
- Allows administrators to delete events.
![image](/static/readme/delete-1.png)
![image](/static/readme/delete-2.png)

### Edit Event Page
- Allows administrators to edit event details.
- Supports image uploads only via image URL.
![image](/static/readme/edit-1.png)
![image](/static/readme/edit-2.png)

# Data Model

- ContactMessage: Stores messages submitted through the contact form.
- Event: Stores details about events, including name, genre, location, organiser, schedule, description, and ticket info.
- Subscriber: Stores email addresses of newsletter subscribers and the date they subscribed.
- Ticket: Stores ticket purchase information, including event and user references, quantity, and purchase date.
- User: Stores user account details, including username, email, password, and profile information. (Created by [Django Allauth](https://docs.allauth.org/en/latest/))

![image](/static/readme/subsurface-db-diagram.png)




# Tools & Documentations


## Payments 

- [Stripe](https://stripe.com/gb)
  - I used Stripe to handle the ticket payment function

## Languages used:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


## Libraries & Frameworks

- [Django](https://www.djangoproject.com/)
  - I used Django to build this website, which is a high-level Python web framework. Subsurface features multiple apps with model, view and template layers. - I have also used Django to provide an admin view, create forms and test my website. Further features used include [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for user authentification.


- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language used for Python and HTML for dynamic content.

- [jQuery](https://jquery.com/)
  - Bootstrap Jquery.

- [Bootstrap 4](https://getbootstrap.com/) 
  - Used throughout the project for  responsiveness, cards for events as well as navigation

- [Google Fonts](https://fonts.google.com/)
  - Google fonts are used for better look
  

### Other Tools:


**[ElephantSQL](https://www.elephantsql.com/)**
* An advanced open-source database, hosted in the cloud, used for hosting the SQL database.

**[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)**
* The templating language used for Python to add the logic to HTML5

**[Github](https://github.com)**
* Used for version control throughout the whole project

**[GitPod](https://github.com)**
* Used as an online editor to code the project

**[Heroku](https://heroku.com)**
* Used for hosting everything for the project, creating a live link for the users

**[Cloudinary](https://cloudinary.com/)**
* Used for a smoother image upload user experience

##  Documentations:


* **[Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)**

* **[Heroku docs](https://devcenter.heroku.com/articles/getting-started-with-python)**

* **[jQuery docs](https://api.jquery.com/)**

* **[Markdown docs](https://www.markdownguide.org/cheat-sheet/)**

* **[Django](https://docs.djangoproject.com/en/5.0/)**

* **[Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)**



### Design & image editing

**[Adobe Photoshop](https://www.adobe.com/)**
* Compressing and resizing images.

**[Website Mockup Generator](https://websitemockupgenerator.com/)**
* Create a multi-screen size screenshot.

**[Real Favicon Generator](https://realfavicongenerator.net/)**
* Creating favicon from an image.

**[MacOS Screenshot & Screen recording](https://support.apple.com/en-gb/guide/mac-help/mh26782/mac)**
* Used for screen recording and screenshots

**[EzGif](https://ezgif.com/video-to-gif/)**
* Used to convert screen recordings to gifs

**[DBDiagram](https://dbdiagram.io/home)**
* Used for creating a visual database model


# Extra Features for the Future

- **Unified Login/Register Page**: Combined login and register functionality on a single page with JavaScript switching.

- **Account Deletion Option**: Allow users to delete their accounts.
- **Media Widget Integration**: Embed iframes for YouTube, SoundCloud, and Spotify widgets on event detail pages.

- **Event Organiser Accounts**: Event organiser accounts for venues and organisers with administrator access.

- **Dynamic QR Codes**: Generate dynamic QR codes for each ticket, with a scannable page that shows event name, username, ticket quantity, and validity.

- **User Profile Customization**: Allow users to customize their profiles with photos and personal information.

- **Social Media Integration**: Enable users to share events on social media platforms directly from the site.

- **Event Reviews and Ratings**: Allow users to leave reviews and ratings for events they have attended.

- **Global Events**: Expand event listings to include global events, not just those in the UK.


# Deployment

## Running locally

```python3 manage.py runserver```

## Libraries
```
pip install django
pip install cloudinary
pip install django-allauth
pip install stripe 
pip install psycopg2
pip install gunicorn dj-database-url psycopg2-binary
pip install django-heroku
```
## env.py used for running the project locally
```
import os

os.environ["ALLOWED_HOSTS"] = ""
os.environ["CLOUDINARY_CLOUD_NAME"] = ""
os.environ["CSRF_TRUSTED_ORIGINS"] = ""
os.environ["DB_HOST"] = ""
os.environ["DB_NAME"] = ""
os.environ["DB_PASSWORD"] = ""
os.environ["DB_PORT"] = ""
os.environ["DB_USER"] = ""
os.environ["DEBUG"] = ""
os.environ["DEFAULT_FROM_EMAIL"] = ""
os.environ["DISABLE_COLLECTSTATIC"] = ""
os.environ["EMAIL_HOST_PASSWORD"] = ""
os.environ["EMAIL_HOST_USER"] = ""
os.environ["SECRET_KEY"] = ""
os.environ["STRIPE_PUBLISHABLE_KEY"] = ""
```
- For deployment these are all set on Heroku

## Initial Setup
- The website is built using the [Code Institute's gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template) provided for this project.
- Development was carried out in [Gitpod](https://www.gitpod.io/), an online IDE linked to [GitHub](https://github.com/).

## ElephantSQL Database Setup
- **Navigate to ElephantSQL:** Log in via [ElephantSQL](https://www.elephantsql.com/) using the "Log in" button at the top right corner of the page.
- **Sign in with GitHub:** Choose the GitHub option for authentication and authorize ElephantSQL to access your GitHub account.
- **Create a New Team:** After logging in, add a team name, agree to the Terms of Service, confirm GDPR compliance, and provide your email.
- **Create Database Instance:** Click "Create New Instance", select the "Tiny Turtle" plan, choose a data center, and finalize the instance creation.

## Setting Up Gitpod with an External Database
- Install Required Packages
- In Gitpod, install psycopg2 by running the following command in the terminal:
```pip3 install psycopg2```

### Update Requirements
- Add the newly installed package to your requirements.txt file by executing:
```pip freeze > requirements.txt```

### Modify settings.py
- In your project's settings.py file, edit the DATABASES section to connect to your ElephantSQL database. Comment out the original sqlite3 configuration and replace it with the following code, ensuring to insert your actual ElephantSQL database URL. Do not commit this URL to your repository to avoid exposing sensitive information.

```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / "db.sqlite3",
}
}
```

```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'your-database-name',
'USER': 'your-database-user',
'PASSWORD': 'your-database-password',
'HOST': 'your-database-host',
'PORT': 'your-database-port',
}
}
```

### Check Database Connection
- To verify that you are connected to the external database, run the following command in the terminal. You should see a list of all migrations printed:
```python3 manage.py showmigrations```

### Migrate Database Models
- Apply migrations to your new database by executing:
```python3 manage.py migrate```

### Create a Superuser
- Set up a superuser for your new database by running the following command. Follow the prompts to create a username and password. The email address can be left blank:
```python3 manage.py createsuperuser```

## Heroku Deployment
- **Create Heroku App:** Log into [Heroku](https://www.heroku.com/) and create a new app, selecting the nearest region.
- **Configure Database:** In Heroku app settings, reveal and set Config Vars as per the env.py on the local build. Copy the database URL from ElephantSQL to Heroku's DB config var.
- **Connect to GitHub:** In the "Deploy" tab of your Heroku app, connect to your GitHub repository for automatic or manual deployment.
- **Deploy:** Use the "Deploy Branch" button in Heroku to start the build and deploy process.


# Testing
[Testing docs](/TESTING.md)

- Automated testing with django inbuilt test system [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
- Manual Testing
- HTML CSS and JS test sites described in the testing docs


# Credits
- **[Bootstrap](https://getbootstrap.com/)**: For providing the essential tools to craft an intuitive and responsive user interface.
- **[Heroku](https://heroku.com/)**: For their amazing cloud platform that lets me host my app.
- **[ElephantSQL](https://www.elephantsql.com/)**: For their reliable PostgreSQL database hosting service used in this project.
- **[jQuery](https://jquery.com/)**: For their robust library that has enabled me to enhance user interactions on my project.
- **[CodeInstitute](https://codeinstitute.net/)**: For their  [Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template) that made the coding experience as smooth as possible.
- **[Django](https://www.djangoproject.com/)**: For providing a powerful, high-level Python web framework that encourages rapid development and clean design.


## Credit for Content
- [Code Institute](https://codeinstitute.net/):
  - Boutique Ado walkthrough project for code snippets, authentication setup
- [Resident Advisor](https://www.residentadvisor.net):
  - For the events and inspiration as well as event images
- [Headfirst Bristol](https://www.headfirstbristol.co.uk):
  - For events and inspiration as well as event images


## Acknowledgements
- I'd like to thank to my mentor Chris Quinn for helping me make this project better.
- Also thank you to Code Institute & Bristol College team , especially for Manuel Perez for continuous support.

Adam Voros | 2024









  
