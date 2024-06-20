### The Subsurface web app has been tested using:
- [User Story Testing](#user-story-testing)
    + [Viewing and Navigation](#viewing-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and Searching](#sorting-and-searching)
    + [Purchasing and Checkout](#purchasing-and-checkout)
    + [Event Management](#event-management)
    + [Ticket Management](#ticket-management)
- [Compatibility Testing](#compatibility-testing)
    + [Device Compatibility Testing](#device-compatibility-testing)
    + [Browser Compatibility Testing](#browser-compatibility-testing)
- [Code Review & Validation](#code-review-and-validation)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [Javascript Validation](#javascript-validation)
    + [Python Validation](#python-validation)
- [Unfixed Issues](#unfixed-issues)
- [Color Contrast Testing](#color-contrast-testing)
- [Manual Testing](#manual-testing)
    + [Testing Stripe](#stripe)
- [Automated Testing](#automated-testing)
- [LightHouse Testing](#lighthouse-testing)
- [Test Accounts](#user-accounts-for-testing)


# User Story Testing

## Event Browsing and Details

- As an Event-goer, I want to view a list of events so that I can quickly compare and select different event options.
    - Event-goers can browse events by navigating to the events page, where they will find a list of available events displayed as event cards with key information such as the event title, date, location.

- As an Event-goer, I want to view individual event details so that I can find out further information about the event.
    - Event-goers can click on an event card to access the event details page, which provides comprehensive information about the selected event, including a detailed description, date, time, location, ticket prices, and any additional relevant details.

- As an Event-goer, I want to quickly identify key features of events through icons and keywords so that I can decide if it's appropriate for the type of event I want to attend.
    - Event cards and event detail pages include clear icons and keywords that highlight the key features.

- As an Event-goer, I want to see the price update automatically when I select ticket quantity so that it can help me not to overspend.
    - On the event details page, when event-goers adjust the ticket quantity using the provided input or dropdown, the total price dynamically updates to reflect the selected quantity, ensuring transparency and helping users make informed decisions about their spending.

- As an Event-goer, I want to see available dates so that I know the event is available when I book it.
    - The event details page clearly displays the available dates for the event, allowing event-goers to easily identify when the event is scheduled to take place and ensure it aligns with their availability.

- As an Event-goer, I want to see the number of available tickets for each event so that I know how many tickets are left before I make a decision.
    - The event details page prominently shows the number of available tickets for the event, providing event-goers with real-time information about ticket availability and helping them make timely decisions to secure their desired tickets.


### Registration and User Accounts

- As a Registered User, I want to easily register for an account so that I can have a personal account for keeping track of my tickets.
    -The registration process is straightforward and user-friendly, requiring only essential information such as username, email address, and password. Upon successful registration, users can log in, buy tickets and use their tickets on the My Tickets page.

- As a Registered User, I want to easily log in or log out so that I can access my personal info.
    - The login process is simple and secure, allowing registered users to enter their email address and password to access their account. Once logged in, users can easily log out using the provided logout button or link.

- As a Registered User, I want to easily recover my password so that I can access my account even if I've forgotten my password.
    - The password recovery process is intuitive and efficient. Users can click on the "Forgot Password" link on the login page, enter their registered email address, and receive an email with instructions on how to reset their password securely.

- As a Registered User, I want to have a personalized user page for my tickets so that I can see my personal order history and use my tickets when needed.
    - Registered users have access to a dedicated user page that displays their personal order history, including details of their purchased tickets. The user page also provides options to view, download, or generate QR codes for their tickets, enabling easy access and use when needed.

- As a Registered User, I want to change my password so that I can ensure my account remains secure.
    - The user page includes a settings or profile section where registered users can easily change their password. The password change process requires users to enter their current password and then set a new password, ensuring the security of their account.

- As a Registered User, I want to change my email so that I can keep my contact information up-to-date.
    - The user page's settings or profile section also allows registered users to update their email address. Users can enter a new email address and confirm the change, ensuring their contact information remains accurate and up-to-date.

- As a Registered User, I want to sign out so that I can securely log out of my account.
    - The user page and navigation menu include a prominently displayed "Sign Out" or "Log Out" button or link, allowing registered users to securely log out of their account with a single click, ensuring the security of their session.

### Sorting and Searching
-   As an Event-goer, I want to sort/filter events by dedicated filters (e.g., city, date, genre) so that I can easily identify suitable options for my experience.
    - The events page provides a set of dedicated filters, such as city, date, and genre, which event-goers can use to narrow down the list of events based on their preferences. The filters are intuitive and user-friendly, allowing users to select multiple criteria and dynamically update the displayed events accordingly.


### Purchasing and Checkout

- As an Event-goer, I want to select the event I want and book through the event page so that I can start the booking process.
    - Event-goers can select the desired ticket quantity on the event details page and proceed to the booking process by clicking the "Get Tickets" button.

- As an Event-goer, I want to easily enter my payment information so that I can check out quickly with no hassles.
    - The checkout process provides a user-friendly form for event-goers to securely enter their payment information, with real-time validation.

- As an Event-goer, I want to view an order confirmation after checkout so that I know my order has gone through and I haven't made any mistakes.
    - After successful checkout, event-goers receive a ticket on their My Tickets page displaying a summary of the purchased tickets.

- As an Event-goer, I want to have my ticket purchase connected with my username so that I can easily access and manage my tickets.
    - Purchased tickets are automatically associated with the registered user's account, allowing easy access and management of tickets through their My Tickets page.


### Event Management

- As an Administrator, I want to upload, edit, and delete events so that I can manage the event listings efficiently.
    - The manage event page a dedicated page for administrators to manage event listings.
    - Administrators can easily upload new events by filling out a form with relevant details such as the event title, description, date, time, location, and ticket prices. They can also edit existing event details and delete events as needed, ensuring the accuracy and relevance of the event listings.

- As an Administrator, I want to set ticket prices so that I can ensure correct pricing for various events.

    - When creating or editing an event, administrators have the ability to set ticket prices for any events. The manage create/edit event pages provides input fields or options to specify the prices for each ticket type, allowing administrators to ensure accurate and appropriate pricing for various events.

- As an Administrator, I want to set the maximum ticket amount so that I can control the number of tickets available.

    - The admin panel allows administrators to set the maximum number of tickets available for each event. Administrators can specify the total ticket capacity or set limits for specific ticket types, ensuring control over the ticket availability and preventing overselling.

- As an Administrator, I want to display the number of available tickets so that I can inform event-goers of ticket availability.
    - The event details page dynamically displays the number of available tickets for each event based on the maximum ticket amount set by the administrator and the number of tickets already sold. This real-time information keeps event-goers informed about ticket availability and helps them make timely decisions when planning to attend events.


### Ticket Management

- As an Event-goer, I want to check my tickets in the "My Tickets" page so that I can keep track of my bookings.
    - Registered users have access to a dedicated "My Tickets" page within their user account. This page displays a list of all the tickets they have purchased,

## Device Compatibility Testing

### Responsiveness
* Responsiveness tests were done, using Google Chrome Developer Tools across different device screen sizes, including:

- iPhone SE
- iPhone 15 Pro
- Pixel 5
- iPad Mini
- iPad Air
- Surface Pro 7
- Galaxy Fold
- Samsung Galaxy A51/A71

Additionally, I tested the website on the following physical devices:

- iPhone 12 mini
- Nokia G22
- iPad Pro M3 
- Macbook Pro 16"
- Windows PC
- Samsung widescreen monitor



## Browser Compatibility Testing

The site was tested across different browsers to check compatibility:

- **Desktop Browsers:**
  - Google Chrome ( Mac OS)
  - Microsoft Edge ( Windows )
  - Mozilla Firefox
  - Opera
  - Brave

- **Mobile and Tablet Browsers:**
  - Google Chrome (Android)
  - Safari (iOS)
  - DuckDuckGo (iOS)
  - Microsoft Edge (iOS)
  - Mozilla Firefox (iOS)

No issues were encountered during browser testing.

# Code Review & Validation

## HTML Validation

### Home page
- Issue:
![image](/static/testing/index-error.png)
- Fixed: 
![image](/static/testing/index-fixed.png)
[Code Changes](https://github.com/parduckids/milestone-project-four/commit/9971018719bc59ec2ba2cb9baab688bc7209870e)
### Events page
![image](/static/testing/events.png)
### Event detail page
![image](/static/testing/event.png)
### Authentication
- Issue:
![image](/static/testing/login-error.png)
- Fixed 
![image](/static/testing/login-fixed.png)
[Code Changes](https://github.com/parduckids/milestone-project-four/commit/dcca14c4a9c743314b557fc367099260bf1d4050)


## CSS Validation  
![image](/static/testing/css-test.png)

## Javascript Validation
### All custom JS code has been tested with [JSHint](https://jshint.com/)
![image](/static/testing/jshint.png)

## Python Validation
- All Python files (except setting files) has been checked using a PEP8 linter to make sure they are compliant.
[Code Changes](https://github.com/parduckids/milestone-project-four/commit/20295f1c2794142e6566af648c06d9cb0bab9f46)

# Unfixed issues

- On the 'My Tickets' page, the qr code closing icon is overlaying the event name on some events
![image](/static/testing/x-in-text.png)

- Link a little bit too close to the text under it 

![image](/static/testing/link-too-close.png)


- My tickets ticket cards images aren't the same size, creating an extra padding on smaller image size events, this could be fixed by adding 1024x1024 images for events which is advised on the site

![image](/static/testing/too-much-padding.png)


# Color Contrast Testing
- Calculating contrast ratio with [Coolors](https://coolors.co/contrast-checker/112a46-acc8e5)
![image](/static/testing/color-contrast.png)

# Manual Testing

- I thoroughly tested the website's functionality by clicking every button, link, and interactive element on each page. I navigated through the site, checking the responsiveness, event browsing, filtering, user registration, account management, and ticket purchasing features. All components worked as expected, ensuring a smooth user experience.

## Stripe
![image](/static/testing/buy-ticket-1.png)
![image](/static/testing/buy-ticket-2.png)
![image](/static/testing/buy-ticket-3.png)
![image](/static/testing/buy-ticket-4.png)


# Automated Testing

# LightHouse Testing

## Home page

### Desktop

![image](/static/testing/lh-home-desktop.png)

### Mobile 

![image](/static/testing/lh-home-mobile.png)

## Events page

### Desktop

![image](/static/testing/lh-event-desktop.png)

### Mobile 

![image](/static/testing/lh-event-mobile.png)

## Event Detail page

### Desktop

![image](/static/testing/lh-event-detail-desktop.png)

### Mobile 

![image](/static/testing/lh-event-detail-mobile.png)

Adam Voros | 2024