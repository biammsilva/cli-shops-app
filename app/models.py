from peewee import SqliteDatabase, Model, CharField, AutoField, BooleanField,\
                   DateField, DecimalField, ForeignKeyField

db = SqliteDatabase('stylight.db')


class Shops(Model):
    """Shops model"""
    id = AutoField(column_name='a_id')
    name = CharField(max_length=255, column_name='a_name')
    online = BooleanField(column_name='a_online')

    class Meta:
        database = db
        table_name = 't_shops'


class Budgets(Model):
    """Budgets Model"""
    shop_id = ForeignKeyField(model=Shops, column_name='a_shop_id')
    month = DateField(column_name='a_month')
    budget_amount = DecimalField(max_digits=10, decimal_places=2,
                                 column_name='a_budget_amount')
    amount_spent = DecimalField(max_digits=10, decimal_places=2,
                                column_name='a_amount_spent')

    class Meta:
        database = db
        table_name = 't_budgets'
