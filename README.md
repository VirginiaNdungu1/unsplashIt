# [splashIt](https://github.com/VirginiaNdungu1/unsplashIt)


## Web Application that allows you to see the world through the lense

## Prerequisites
      psycopg2==2.7.3.2
      Django==1.11.7
      django-bootstrap3==9.1.0
      olefile==0.44
      Pillow==4.3.0
      pytz==2017.3

## Installation

* `git clone <repository-url>` this repository
* `cd splashIt`

## Project Specifications

      Features 
       As an admin, I should be able to:
       
          Sign In to the admin dashboad
          create tags
          update tags
          delete tags
          views tags
          Post images
          update images
          delete images
       
      
        
       As a User, i should be able to:
       
        View Images
        View full size image on hover
        View image details
        Copy the image link of the image
        
        
## Known Bugs
Copy image link of the image does not work properly

## Running / Development

python manage.py runserver

Running on http://127.0.0.1:8000/ 

## Hosting / Production

### requirements
gunicorn==19.7.1
python-decouple==3.1
whitenoise==3.3.1
dj-database-url==0.4.2

[splashIt](https://splashit.herokuapp.com/)


### Running Tests

python3.6 manage.py test

## Technologies Used
       Python3.6
       django
       Postgres Database
       Bootstrap
       CSS
       HTML

    Deployment:
       Heroku


                 ## MIT (c) 2017 [Virginia Ndung'u]((https://github.com/VirginiaNdungu1/unsplashIt)
