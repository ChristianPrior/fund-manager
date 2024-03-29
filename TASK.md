# Task

The goal is to generate a simple Django application with simply SQLite as the database, and with:

* A single Model called Fund, representing the data in the attached sample_fund_data.csv.
* A way to import such Fund objects by uploading a CSV file matching the sample provided, via a file upload form on a Django web page: the Django app should then parse that file and create corresponding Fund objects in the database.
* A web page displaying:
  * The list of funds available in the database as a table with one column per field on the Fund model.
  * A dropdown at the top of the page, allowing you to select a Strategy value, and filter the funds displayed on the page by one of the available Strategy choices.
  * At the bottom of the table, display the total number of Funds in the database.
  * If the current page is filtered by a Strategy value, then this number should be the number of Fund objects matching the filter.
  * At the bottom of the table, display one number that is the sum of all Fund AUM values (AUM is one number field listed in the sample CSV file).
* A REST API endpoint that can:
  * List Fund objects that are in the database, in a JSON format.
  * A way to filter the objects by the Strategy field, by appending a query parameter ?strategy=[value] to the URL of that endpoint.
  * Another endpoint to view a JSON representation of a single Fund object identified by its id field.
  * As a bonus, write one or more automated tests within the Django app, checking that some of the specs above are working. Tests can be run with the command `manage.py test`.

You do not need to worry about styling the pages to make them beautiful in any way unless you choose to.

As this exercise might be quite long, the candidate is free to skip some of the specifications above, to focus on the other ones, based on what area is more comfortable/fun.

Your code will be assessed based on the simplicity and cleanliness of the Python code, niceness of the HTML markup, cleverness of the data parsing and manipulation necessary for parsing an input file and persisting the data via the Django ORM, as well as making sure you are familiar with scaffolding a simple MVC Django app.

You will not be judged on the design and aesthetics of the pages, nor on the way the necessary static assets and dependencies are handled (if any).

The Django app can simply be run using the default `manage.py runserver` command. Use SQLite for the database.

Please create a GitHub repository for hosting and sharing the code with us. We will discuss and debrief on your submission during our next call.
