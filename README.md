# Subsurface
## Milestone Project 4 - Full Stack Development with Django
  * [Live link](https://subsurface-03d2c6e34bd7.herokuapp.com/)
  * [Wireframes](#)
  * [GitHub Repository](https://github.com/parduckids/milestone-project-four)
  * [Testing docs](#)

![image](/static/readme/3-devices-black.png)

## The Idea:

* "Subsurface" is your gateway to the underground music scene, offering the ultimate destination for underground music events and ticket sales across the UK's major cities. Our focus lies on the raw, unfiltered sounds of techno, house, noise, and experimental music. While countless event websites exist, none truly cater to the authentic underground scene. Subsurface fills that void, bringing you closer to the music that matters.

* Whether you're a devoted fan of the underground or a curious newcomer, Subsurface provides an unparalleled selection of events often overlooked by mainstream platforms. Join us and immerse yourself in the vibrant, pulsating heart of the UK's underground music culture.

* "Subsurface" is developed as my Milestone Project 4 for the Code Institute's Diploma in Web Application Development course. This project incorporates a range of technologies, including HTML, CSS, JavaScript, Django, and PostgreSQL. Multiple Django apps were used to structure the application effectively, and Stripe integration was implemented to handle secure ticket transactions.
---

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

## Footer

## Authentication 
- Django allauth templates redesigned

## Messages 


## All Pages and Functionality

### Index (Home) Page

### Events Page

### Event Detail Page

### About Page

### Login Page

### Register Page

### My Tickets Page

### Change Email Page

### Change Password Page

### Sign Out Page

### Buy Ticket Page

### Create Event Page

### Manage Events Page

### Delete Event Page

### Edit Event Page


# Data Model
- image for db diagram



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


# Deployment

# Testing
[Testing docs](#)

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


## Ackowledgements
- I'd like to thank to my mentor Chris Quinn for helping me make this project better.
- Also thank you to Code Institute & Bristol College team , especially for Manuel Perez for continuous support.









  
