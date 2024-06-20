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
    + [Navigation & Footer](#navigation-bar-and-footer)
    + [Rest of the site](#rest-of-the-site)
- [Manual Testing](#manual-testing)
    + [Testing Stripe](#stripe)
- [Automated Testing](#automated-testing)
- [LightHouse Testing](#lighthouse-testing)
- [Test Accounts](#user-accounts-for-testing)


# User Story Testing

## Viewing and Navigation

## Registration and User Accounts 

## Sorting and Searching

## Purchasing and Checkout

## Event Management

## Ticket Management

# Compatibility Testing

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
![image](/static/testing/too-much-padding.png)

- My tickets ticket cards images aren't the same size, creating an extra padding on smaller image size events, this could be fixed by adding 1024x1024 images for events which is advised on the site
![image](/static/testing/link-too-close.png)

# Color Contrast Testing

## Navigation Bar and Footer

## Rest of the site

# Manual Testing
## Stripe
- Test if the payment went through and include screenshot of stripe dashboard 

# Automated Testing

# LightHouse Testing

# User Accounts for Testing