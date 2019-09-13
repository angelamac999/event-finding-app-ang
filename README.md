# Free Event Finder App Template

To get started with this template:

1. Click "use template" to create your own repository with the same files and directory structure.
2. Clone the repository to your machine.
3. Open terminal/powershell
4. Navigate to the repository and create a new virtualenvironment called `venv`
5. Activate your new `venv`
6. Install the project dependencies using: `pip install -r requirements.txt`

To configure the database:
1. Type `psql` then hit enter.
2. Type `CREATE DATABASE nameofyournewdatabase;` then hit enter.
3. Type `\l` then press enter to confirm your new database is there and ready to go.
4. Type `\q` to escape the psql shell.
5. Create a new superuser - you should be familiar with how to do this (hint, it was in the django tutorial :) )
6. Then update the settings.py to use whatever you just named your database and your username.
7. Type `python3 manage.py runserver` and open up http://localhost:8000/event-finder/ to confirm all is well!

Once you are set up and ready to go, these are your tasks:

1. Add a new "venue" field to the Event model
2. Create a many to many relationship between the events and categories
3. Modify the index page to show the events with their categories.
5. Modify the events page to show all the event information, including the categories.
6. Create a page that has a form to create a new event. This event should then appear on the index page.

Once you have completed these tasks you can start working on:

1. The My Account page. We are not doing anything with users until next week, but you can definitely get the my account page started and styled by just using some dummy data.
2. Make it responsive - put those css and bootstrap skills to the test!
3. Add filters for location and category to the index page.