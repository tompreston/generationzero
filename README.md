Generation Zero
===============
The [Generation Zero](http://www.generationzero.org.uk/) website.

Todo
----
- Author page w/short bio at end of entry + social links
- Issues page


Django
------
If you're new to Django, here's the layout:

    generationzero/       <- project directory
        generationzero/   <- settings and stuff
        magazine/         <- the `magazine` app
        static/
            css/          <- stylesheets
        templates/        <- HTML templates for the website
            base.html     <- other templates inherit from this
            *.html        <- templates for views
        manage.py         <- project control
        requirements.txt  <- packages reqired for this project

The idea is that the `magazine` app is generic so that it can be repurposed
for other projects (`my rad magazine website` or `generation one` etc).


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

TODO: Can an entry be a part of many categories? So can someone write
something that goes into `Art` and `Tech` or should we keep it to one
category. Remember: just because you CAN do something doesn't mean that
you SHOULD!


Getting Started
---------------
This is how I work, your milage may vary.

First, you'll need `pip` and `virtualenv` installed. Go get them and
then come back.

Clone the repo:

    git clone https://github.com/tompreston/generationzero.git
    cd generationzero/

Setup a virtual environment directory called `venv` and then activate it:

    virtualenv venv
    source venv/bin/activate

Your command line should change to indicate that you're now using the
virtual Python environment. Now install all of the required packages:

    pip install -r requirements.txt

This will install everything you need into the `venv` virtual environment
directory (so it doesn't litter your system files).

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

When you're done developing, make sure you deactivate the virtual
environment with:

    deactivate

