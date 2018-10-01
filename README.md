# Photo-Gallery
A personal gallery application that I display my photos for others to see
## By
* [Lewis Mutuma](https://mutumamutuma.github.io/Portfolio/)

## Application
=====================================================================================
<img src="/images/images/landingpage1.JPEG">

<img src="/images/images/Landingpage2.JPEG">
=====================================================================================

## User stories

The user should be able to:

+ [x] View different photos that interest me.
+ [x] Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
+ [x] Search for different categories of photos. (ie. Travel, Food)
+ [x] Copy a link to the photo to share with my friends.
+ [x] View photos based on the location they were taken.

## Prerequisites
+ [x] Python3.6

## Features In Photo Gallery
+ [x] search functionality based on image description.
+ [x] Bootstrap image model and copy link button.
+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Filter images based on category and location.

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/MutumaMutuma/Photo-Gallery.git
    $ cd Gallery
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```

## Hot to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

## Photo-Gallery Demo

This is the live link to Photo-Gallery [Click here](https://lewismutumagallery.herokuapp.com)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

## License ([MIT License](https://github.com/MutumaMutuma/Photo-Gallery/blob/master/LICENSE))
This project is licensed under the MIT Open Source license, (c) [Lewis Mutuma](https://github.com/MutumaMutuma)