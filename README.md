# Stylight coding assessment - Budget notifications

## Python application

### Prerequisites:

* Python3
* Virtualenv

### Setting up:

* Create a virtual environment:

        virtualenv -p python3 env

* Activate the environment:

        source env/bin/activate

* Install the dependencies:

        pip install -r requirements.txt
    
* Set up de Database:

        python setup.py

### Running:

* To scan the budgets and send the alerts:

        python main.py check

* If you'd like to scan another dates too use "--searching-date":

        python main.py check --searching-date 2020-01-20

* To list the budgets:

        python main.py list-budgets

* To list the shops:

        python main.py list-shops

* Any Doubts?

        python main.py --help


## Docker

### Prerequisites:
* Docker

### Setting up
    docker build -t budgets_shop .

### Running:

* To scan the budgets and send the alerts:

        docker run budgets_shop check

* If you'd like to scan another dates too use "--searching-date":

        docker run budgets_shop check --searching-date 2020-06-20

* To list the budgets:

        docker run budgets_shop list-budgets

* To list the shops:

        docker run budgets_shop list-shops

* Any Doubts?

        docker run budgets_shop --help

### Testing:

    pytest app/tests.py 

## Technologies:

I've used SQLite as database. But, there's no need to import the sql.
All the database setup is been doing at the application.

I've chosen an ORM to deal with it. Peewee ORM is simple and minimalist to work with smaller context.

I'm using also a lib to make the CLI. Typer.

If you want to add data, you can write in app/migrations/data.py file, or in the database itself.

I've add two more commands to visualize the data in the command line. The list of budgets and shops. That way, you can see what has changed in the database.

Challenge resolution time: 8 hours.

You can run th application using python console or docker.

* Does your solution avoid sending duplicate notifications?

Yes, i'm checking if the shop is between 50 and 100 percent to make one notification and 100 percent or more to trigger the other one.

* How does your solution handle a budget change after a notification has already been sent?

It checks all the stores, not only the online ones.