from datetime import datetime

import typer

from app.models import Budgets, Shops

application = typer.Typer()


@application.command()
def list_budgets():
    ''' Command list the budgets and calculate the average spent '''
    budgets = Budgets.select()
    for budget in budgets:
        average_spent = (budget.amount_spent * 100) / budget.budget_amount
        typer.echo(str(budget.shop_id) + ' - ' + budget.shop_id.name)
        typer.echo('Month: ' + str(budget.month))
        typer.echo('Budget amount: ' + str(budget.budget_amount))
        typer.echo('Amount spent: ' + str(budget.amount_spent))
        typer.echo('Average spent (%): ' + str(average_spent))
        typer.echo('------------------')


@application.command()
def list_shops():
    ''' Command list the shops and check if it is online '''
    shops = Shops.select()
    for shop in shops:
        typer.echo(str(shop.id) + ' - ' + shop.name)
        typer.echo('Online? ' + ('yes' if shop.online else 'no'))
        typer.echo('------------------')


@application.command()
def check(searching_date: str = str(datetime.today().date())):
    ''' Command to scan the budgets and send the alerts...
        If you'd like to scan another dates too use "--searching-date":

        Ex. python main.py check --searching-date 2020-01-20'''
    date = datetime.strptime(searching_date, '%Y-%m-%d')

    budgets = Budgets.select().join(Shops, on=(Budgets.shop_id == Shops.id))\
        .where(
            (Budgets.month == date.replace(day=1).date())
        )
    if not budgets:
        typer.echo("No entries for this month")
    for budget in budgets:
        average_spent = (budget.amount_spent * 100) / budget.budget_amount
        shop = budget.shop_id
        if average_spent >= 100 and budget.shop_id.online:
            shop.online = False
            shop.save()
            typer.echo("you reached 100% of your budget, you've been blocked")
        elif 50 <= average_spent < 100:
            shop.online = True
            shop.save()
            typer.echo('You reached 50% of the current months budget')
        elif average_spent < 50:
            shop.online = True
            shop.save()
        else:
            continue
        remaining_budget = budget.budget_amount - budget.amount_spent
        typer.echo(str(budget.shop_id) + ' - ' + budget.shop_id.name)
        typer.echo('Date: ' + str(date.date()))
        typer.echo("Month's Budget: " + str(budget.budget_amount))
        typer.echo('Expenditure: ' + str(budget.amount_spent))
        typer.echo('Remaining budget: ' + str(remaining_budget))
        typer.echo('------------------')


if __name__ == "__main__":
    application()
