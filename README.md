Generation Zero
===============
The [Generation Zero](http://www.generationzero.org.uk/) website.

CSS/frontend people! Yes *YOU*! We need your help! For free! Wee!
(Tom sucks at CSS - it needs a big tidy up)


Todo
----
- Issues page
- Fixed width of website on large displays
- Menu burger close cross
- Author page w/short bio at end of entry + social links
  - We need to discuss how the bio will work.
  - Is it the same for each entry by an author


Django
------
If you're new to Django, here's the layout:

    generationzero/       <- project directory
        generationzero/   <- settings and stuff
        magazine/         <- the `magazine` app
        static/           <- static files, css/js/images
        templates/        <- HTML templates for the website
            base.html     <- other templates inherit from this
            *.html        <- templates for views
        manage.py         <- project control
        requirements.txt  <- packages reqired for this project

In a perfect world the `magazine` app is generic so that it can be repurposed
for other projects, such as `my rad magazine website` or `generation one` etc.


Structure
---------
So, currently the website works like this:

    + home_page (w/list of issues and categories)
      + issue page (w/list of entries in that issue)
        - entry in issue page (w/breadcrumb back to issue)
      + category page (w/list of entries in that category)
        - entry in category page (w/breadcrumb back to category)
    - entry page (just on it's own atm)
    - archive TODO


Getting Started
---------------
Use pipenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

    git clone https://github.com/tompreston/generationzero.git
    cd generationzero/
    pipenv install -r requirements.txt
    pipenv shell

Run tests:

    python manage.py test

Create the database:

    python manage.py migrate

Load some test data (if available):

    python manage.py loaddata test_data.json

Now create a superuser:

    python manage.py createsuperuser

Finally, run the test server:

    python manage.py runserver

Check out the website at:

    127.0.0.1:8000/
    127.0.0.1:8000/admin/
