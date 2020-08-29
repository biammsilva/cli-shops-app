import unittest

from typer.testing import CliRunner
from peewee import SqliteDatabase

from main import application
from .models import Budgets, Shops

app = application
runner = CliRunner()
MODELS = [Budgets, Shops]


class CliTestCase(unittest.TestCase):

    def setUp(self):
        self.test_db = SqliteDatabase(':memory:')
        self.test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        self.test_db.connect()
        self.test_db.create_tables(MODELS)
        shop1 = Shops.create(**{
            'id': 1,
            'name': "Test Shop 1",
            'online': True
        })
        shop2 = Shops.create(**{
            'id': 2,
            'name': "Test Shop 2",
            'online': True
        })
        Budgets.create(**{
            'shop_id': shop1,
            'month': '2020-09-01',
            'budget_amount': 500,
            'amount_spent': 300
        })
        Budgets.create(**{
            'shop_id': shop2,
            'month': '2020-09-01',
            'budget_amount': 500,
            'amount_spent': 600
        })

    def test_check_no_entries_month(self):
        result = runner.invoke(app, [
            "check",
            "--searching-date",
            "2020-01-01"
            ]
        )
        assert result.exit_code == 0
        assert "No entries for this month" in result.output

    def test_list_budgets(self):
        result = runner.invoke(app, ["list-budgets", ])
        assert result.exit_code == 0
        assert '1 - Test Shop 1\nMonth: 2020-09-01\n'\
               'Budget amount: 500\nAmount spent: 300\n'\
               'Average spent (%): 60\n------------------\n'\
               '2 - Test Shop 2\nMonth: 2020-09-01\n'\
               'Budget amount: 500\nAmount spent: 600\n'\
               'Average spent (%): 120\n------------------\n'\
            in result.output

    def test_list_shops(self):
        result = runner.invoke(app, ["list-shops", ])
        assert result.exit_code == 0
        assert '1 - Test Shop 1\n'\
               'Online? yes\n'\
               '------------------\n'\
               '2 - Test Shop 2\n'\
               'Online? yes\n'\
               '------------------\n'\
            in result.output

    def test_check_september_one_block(self):
        result = runner.invoke(app, [
            "check",
            "--searching-date",
            "2020-09-01"
            ]
        )
        shop2 = Shops.get(id=2)
        assert result.exit_code == 0
        assert shop2.online is False
        assert 'You reached 50% of the current months budget\n'\
               '1 - Test Shop 1\n'\
               'Date: 2020-09-01\n'\
               "Month's Budget: 500\n"\
               'Expenditure: 300\n'\
               'Remaining budget: 200\n'\
               '------------------\n'\
               "you reached 100% of your budget, you've been blocked\n"\
               '2 - Test Shop 2\n'\
               'Date: 2020-09-01\n'\
               "Month's Budget: 500\n"\
               'Expenditure: 600\n'\
               'Remaining budget: -100\n'\
               '------------------\n'\
            in result.output

    def test_check_september_notification_changed(self):
        shop2 = Shops.get(id=2)
        budget2 = Budgets.get(shop_id=shop2)
        budget2.amount_spent = 200
        budget2.save()
        result = runner.invoke(app, [
            "check",
            "--searching-date",
            "2020-09-01"
            ]
        )
        assert result.exit_code == 0
        assert shop2.online is True
        assert 'You reached 50% of the current months budget\n'\
               '1 - Test Shop 1\n'\
               'Date: 2020-09-01\n'\
               "Month's Budget: 500\n"\
               'Expenditure: 300\n'\
               'Remaining budget: 200\n'\
               '------------------\n'\
               '2 - Test Shop 2\n'\
               'Date: 2020-09-01\n'\
               "Month's Budget: 500\n"\
               'Expenditure: 200\n'\
               'Remaining budget: 300\n'\
               '------------------\n'\
            in result.output

    def tearDown(self):
        self.test_db.drop_tables(MODELS)
        self.test_db.close()
