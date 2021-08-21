<!-- ABOUT THE PROJECT -->
# About C50W final project - Cswebfunding

Cswebfunding is a site where you can support other people's dreams or have your own dream realised.  
The idea comes from a kickstarter-like website, but with my own touch and execution.

### Built With

- Python
  * [Django](https://www.djangoproject.com/)
  * [django-notifications-hq](https://pypi.org/project/django-notifications-hq/)
- Javascript
- HTML & CSS
  * [Bootstrap](https://getbootstrap.com/)

### Distinctiveness and Complexity

In Cswebfunding you can create listings, donate and comment to listings and much more. You can also search for listings and view other peoples profiles. You will get notifications if someone commented or donated on/to your listing.

I have also tried my best to make this a 'fun' site by adding various animations.

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in a SQLite Database.
All webpages of the project are mobile-responsive.

(note. If you interpret this as a social network. I have asked this in the CS50 discord to be sure, and they reassured me it's not!)

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
2. Set up local server (make sure you are in the FINAL PROJECT directory!)

    ```sh
    py manage.py runserver
    ```

<!-- USAGE EXAMPLES -->
## Usage

### Creating an account
Creating an account is easy, click on 'Register' on the top of the page and fill out the form. After Registering, you will be automatically logged in and redirected to the index page.

The form consists out of:
* Preview of 'About the Author' section (see Viewing listings)
* Username
* Email adress
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
Click on the listings dropdown and select one of the options. You'll be presented a page of listings. On the topleft there is a button to filter out categories or to sort the listings.

Listings are limited to 9 listings per page. If there are more than 9 listings, a page selector will appear.

If you search for a listing, you will also be redirected to this page.

### Viewing listings
You can view a listing by pressing it on the Scolling listings page (see above). 

The listing page displays:

* Title
* Image
* About the Author
* Progressbar of money collected
* Donation button
* Create comment
* Other comments

You can delete your comment by pressing the delete button underneath the comment.

If you are the author of the listing, and wish to close it prematurely, you can do that by pressing the 'Close Listing' button. Otherwise the listing will automatically close when the enddate is reached.

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

In the admin Page, reachable by going to /admin in the url and logging in with a superuser, you can edit, delete or create:

* Listings
* Users
* Comments
* Donations
* Notifications
