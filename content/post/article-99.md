
---
title: gunicorn + flask + factory mode + create_app
date: 2019-12-29 18:25:49.659189
Description: ""
Tags: []
Categories: []
DisableComments: false
---
I wrote a flask app using the application factory pattern. That means it
doesn't create an app instance automatically when you import it. You have to
call create_app for that. Now how do I run it in gunicorn?

[flask](https://stackoverflow.com/questions/tagged/flask "show questions
tagged 'flask'")
[gunicorn](https://stackoverflow.com/questions/tagged/gunicorn)

+++++++++++++++++++++++++++++++++++++++++++++++++

Create a file `wsgi.py` under your project with the following contents, then
point Gunicorn at it.

    
    
    from my_project import create_app
    
    app = create_app()
    
    
    gunicorn -w 4 my_project.wsgi:app
    # -w 4 specifies four worker processes

Gunicorn allows specifying a function call like `my_project:create_app()`. For
most cases, you can the skip making a `wsgi.py` file and tell Gunicorn how to
create your app directly.

    
    
    gunicorn -w 4 my_project:create_app()

Note that you may have to put the name in quotes for some shells.

    
    
    gunicorn -w 4 "my_project:create_app()"  
    


