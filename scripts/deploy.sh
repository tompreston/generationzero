#!/bin/bash
# Deploy generationzero in the current directory.
# Note: We should use a proper database in the future. Maybe even something
#       with docker-compose.

DB="db.sqlite3"
VENV_DIR="venv"

# Try not to break anything!
is_env_safe()
{
	test -e $DB && test -d $VENV_DIR
}

verify()
{
	if ! is_env_safe; then
		echo "Error: environment is not safe, aborting."
		exit 1
	fi
}

deploy()
{
	# get latest changes
	git pull origin master

	# update deps, db, static files
	source $VENV_DIR/bin/activate
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py collectstatic
	deactivate

	touch generationzero/wsgi.py
	sudo /bin/systemctl reload apache2.service
}

verify
deploy
