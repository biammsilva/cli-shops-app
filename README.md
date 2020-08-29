# Stylight coding assessment - Budget notifications

## Setting up:

### Python application

Pre-requirements:

* Python >= 3.6
* Virtualenv

**Setting up:**

* Create a virtual environment:

    `virtualenv -p python3 env`

* Activate the environment:

    `source env/bin/activate`

* Install the dependencies:

    `pip install -r requirements.txt`
    
* Set up de Database:

    `python setup.py`

**Running:**

`python main.py`

## Application usage:

To scan the budgets and send the alerts:

`python main.py check`

If you'd like to scan another dates too use "--searching-date":

`python main.py check --searching-date 2020-01-20`

To list the budgets:

`python main.py list-budgets`

To list the shops:

`python main.py list-shops`

Doubts?

`python main.py --help`


