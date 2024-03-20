# Edgefolio Take Home Technical Task

Please see `TASK.md` for requirements.
All requirements have been implemented.

## Getting started

* Spin up a virtual environment using tool of choice
  * `pyenv virtualenv 3.12 fund-manager`
  * `pyenv activate fund-manager`
* Install pipenv and requirements
  * `pip install pipenv`
  * `pipenv install`
* Run server locally
  * `pipenv run src/manage.py runserver`
* Open a browser and navigate to the below
  * `http://127.0.0.1:8000/funds` for table display
  * `http://127.0.0.1:8000/funds/upload` for upload form
  * `sample_fund_data.csv` included in repo for uploading
* For the REST API, see unit tests or send the below requests
  * GET `http://127.0.0.1:8000/funds`
  * GET `http://127.0.0.1:8000/funds?strategy=Arbitrage`
  * GET `http://127.0.0.1:8000/funds/<id>`

## Tests

* `pipenv run src/manage.py test`
