import peewee
from ..models import Shops, Budgets


def insert_data():
    shops = [
        {
            'id': 1,
            'name': 'Steve McQueen',
            'online': 1
        },
        {
            'id': 2,
            'name': 'Fashion Quasar',
            'online': 0
        },
        {
            'id': 3,
            'name': 'As Seen On Sale',
            'online': 1
        },
        {
            'id': 4,
            'name': 'H&R',
            'online': 0
        },
        {
            'id': 5,
            'name': 'Meow Meow',
            'online': 1
        },
        {
            'id': 6,
            'name': 'Dole & Cabbage',
            'online': 0
        },
        {
            'id': 7,
            'name': 'George Manly',
            'online': 1
        },
        {
            'id': 8,
            'name': 'Harrison Ford',
            'online': 1
        }
    ]

    budgets = [
        {
            'shop_id': 1,
            'month': '2020-06-01',
            'budget_amount': 930.00,
            'amount_spent': 725.67
        },
        {
            'shop_id': 2,
            'month': '2020-06-01',
            'budget_amount': 990.00,
            'amount_spent': 886.63
        },
        {
            'shop_id': 3,
            'month': '2020-06-01',
            'budget_amount': 650.00,
            'amount_spent': 685.91
        },
        {
            'shop_id': 4,
            'month': '2020-06-01',
            'budget_amount': 740.00,
            'amount_spent': 746.92
        },
        {
            'shop_id': 5,
            'month': '2020-06-01',
            'budget_amount': 630.00,
            'amount_spent': 507.64
        },
        {
            'shop_id': 6,
            'month': '2020-06-01',
            'budget_amount': 640.00,
            'amount_spent': 946.32
        },
        {
            'shop_id': 7,
            'month': '2020-06-01',
            'budget_amount': 980.00,
            'amount_spent': 640.16
        },
        {
            'shop_id': 8,
            'month': '2020-06-01',
            'budget_amount': 790.00,
            'amount_spent': 965.64
        },
        {
            'shop_id': 1,
            'month': '2020-07-01',
            'budget_amount': 960.00,
            'amount_spent': 803.67
        },
        {
            'shop_id': 2,
            'month': '2020-07-01',
            'budget_amount': 670.00,
            'amount_spent': 715.64
        },
        {
            'shop_id': 3,
            'month': '2020-07-01',
            'budget_amount': 890.00,
            'amount_spent': 580.81
        },
        {
            'shop_id': 4,
            'month': '2020-07-01',
            'budget_amount': 590.00,
            'amount_spent': 754.93
        },
        {
            'shop_id': 5,
            'month': '2020-07-01',
            'budget_amount': 870.00,
            'amount_spent': 505.12
        },
        {
            'shop_id': 6,
            'month': '2020-07-01',
            'budget_amount': 700.00,
            'amount_spent': 912.30
        },
        {
            'shop_id': 7,
            'month': '2020-07-01',
            'budget_amount': 990.00,
            'amount_spent': 805.15
        },
        {
            'shop_id': 8,
            'month': '2020-07-01',
            'budget_amount': 720.00,
            'amount_spent': 504.25
        }
    ]

    try:
        Shops.insert_many(shops).execute()
        print('Shops data inserted')

        Budgets.insert_many(budgets).execute()
        print('Budgets data inserted')
    except peewee.IntegrityError:
        print('Data already inserted')
