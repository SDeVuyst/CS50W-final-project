<!-- ABOUT THE PROJECT -->
# About C50W final project - Cswebfunding

Cswebfunding is a site where you can support other people's dreams or have your own dream realized.  
The idea comes from a Kickstarter-like website, but with my touch and execution.

[![Video Demo](http://img.youtube.com/vi/LhwgGsaPAlc/0.jpg)](http://www.youtube.com/watch?v=LhwgGsaPAlc)
[Video Demo](https://youtu.be/LhwgGsaPAlc)

## Built With

- Python
  * [Django](https://www.djangoproject.com/)
  * [django-notifications-hq](https://pypi.org/project/django-notifications-hq/)
- Javascript
- HTML & CSS
  * [Bootstrap](https://getbootstrap.com/)

## Distinctiveness and Complexity

In Cswebfunding you can create listings, donate and comment to listings and much more. You can also search for listings and view other people's profiles. You will get notifications if someone commented, donated on/to your listing, or if your listing has been closed.

I have also tried my best to make this a 'fun' site by adding various animations.

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information is saved in a SQLite Database.
All web pages of the project are mobile-responsive.

(note. If you interpret this as a social network. I have asked this in the CS50 discord to be sure, and they reassured me it's not!)

## What is in each file
* `cswebfunding`
  * `static`
    * `cswebfunding.js` - contains all javascript functions, using fetch to eg. donate etc. and asynchronously update DOM
    * `styles.css` - contains all css stles
  * `templates`
    * `index.html` - index page that displays basic info
    * `layout.html` - base template that all other HTML-files use, includes navbar
    * `listing.html` - shows info about a specific listing
    * `listings.html` - shows cards that display different listings, can be sorted/filtered
    * `login.html` -  login page
    * `newlisting.html` - page to create new listing
    * `profile.html` - shows info about specific user
    * `register.html` - page to register
  * `admin.py` - makes sure that User, Listing, Comment and Donation can be viewed in /admin
  * `models.py` - contains the User, Listing, Comment and Donation model
  * `urls.py` - contains all the URLs
  * `views.py` - backend of the application, contains multiple functions so everything is updated in the db and the right responses are returned to user
* `media` - contains default images for user, listing and the index picture
  * `media`- contains user uploaded images

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Django
  ```sh
  pip install Django
  ```
  
* django notifications hq
  ```sh
  pip install django-notifications-hq 
  ```

### Installation

1. Clone the repo

2. Run migrations to create a database (make sure you are in the FINAL PROJECT directory!)
    ```sh
    py manage.py makemigrations cswebfunding
    ```
    ```sh
    py manage.py migrate
    ```
    
3. [Optional] Create admin account
    ```sh
     py manage.py createsuperuser
     ```
     
5. Set up a local server

    ```sh
    py manage.py runserver
    ```

<!-- USAGE EXAMPLES -->
## Usage

### Creating an account
Creating an account is easy, click on 'Register' at the top of the page and fill out the form. After Registering, you will be automatically logged in and redirected to the index page.

The form consists out of:
* Preview of 'About the Author' section (see Viewing listings)
* Username
* Email address
* Profile picture
* Description
* Password

### Creating a listing
If you are logged in, you can create a listing by clicking on 'New Listing'. Fill out the form and you'll be redirected to your newly created listing!

The form consists out of:
  * Preview of listing 
  * Title
  * Description
  * Type (Good Cause or Project)
  * Category
  * Goal in $
  * Image
  * Final Date


### Scrolling listings
Click on the listings dropdown and select one of the options. You'll be presented with a page of listings. On the top left, there is a button to filter out categories or to sort the listings.

Listings are limited to 9 listings per page. If there are more than 9 listings, a page selector will appear.

If you search for a listing, you will also be redirected to this page.

### Viewing listings
You can view a listing by pressing it on the Scrolling listings page (see above). 

The listing page displays:

* Title
* Image
* About the Author
* Progressbar of money collected
* Donation button
* Create comment
* Other comments

You can delete your comment by pressing the delete button underneath the comment.

If you are the author of the listing and wish to close it prematurely, you can do that by pressing the 'Close Listing' button. Otherwise, the listing will automatically close when the final date is reached.

### Viewing accounts
You can view an account by pressing the 'About the Author' section on a listing or by clicking on a comment. 

The profile page displays:

* Username
* Profile Picture
* Description
* Last 3 comments
* Listings

### Add balance
By clicking on the Add balance button, a modal appears where you can add balance.
With balance you can donate to listings. 
(Note. this is not designed to handle payments and should therefore not be considered secure. The user can just type in the amount they would like to receive.)

### Admin Page

In the admin Page, reachable by going to /admin in the URL and logging in with a superuser, you can edit, delete or create:

* Listings
* Users
* Comments
* Donations
* Notifications
