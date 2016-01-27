Generation Zero
===============
The Generation Zero website.

If you're new to Django, here's the layout:

    generationzero/       <- project directory
        generationzero/   <- settings and stuff
        magazine/         <- the `magazine` app
        manage.py         <- project control
        requirements.txt  <- packages reqired for this project

The idea is that the `magazine` app is generic so that it can be repurposed
for other projects (`my rad magazine website` or `generation one` etc).


Structure
---------
So, currently the website works like this:

    + splash_page (w/list of issues and categories)
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

Clone the repo:

    git clone https://github.com/tompreston/generationzero.git
    cd generationzero/

Setup a virtual environment directory called `venv` and then activate it:

    virtualenv-3.4 venv
    source venv/bin/activate

Your command line should change to indicate that you're now using the
virtual Python environment. Now install all of the required packages:

    pip install -r requirements.txt

This will install everything you need into the `venv` virtual environment
directory (so it doesn't litter your system files).

Create the database (notice how `python` now calls Python 3 since we're in
a 3.4 virtual environment):

    python manage.py migrate

Now create a superuser:

    python manage.py createsuperuser

Now run a test server:

    python manage.py runserver

Check out the website at:

    127.0.0.1:8000/
    127.0.0.1:8000/admin/

When you're done developing, make sure you deactivate the virtual
environment with:

    deactivate


Code Style Guidelines
---------------------
I'm super anal about these sorts of things but it doesn't matter if
you're not. The two rules I tend to follow are:

    - indent in Python is 4 SPACES (this is super important)
    - HTML is either 2 or 4 SPACES (but who cares it's HTML)
    - TABs are EVIL

If you're interested, it's worth reading:

    https://www.kernel.org/doc/Documentation/CodingStyle
    https://www.python.org/dev/peps/pep-0008/
    http://semver.org/

I disagree with Linus on the 8 spaces thing (maybe for C...)