import peewee

from ..models import Shops, Budgets


def create_tables():
    try:
        Shops.create_table()
        print("Table 'Shops' successfully created!")
    except peewee.OperationalError:
        print("Table 'Shops' already exists!")

    try:
        Budgets.create_table()
        print("Table 'Budgets' successfully created!")
    except peewee.OperationalError:
        print("Table 'Budgets' already exists!")
