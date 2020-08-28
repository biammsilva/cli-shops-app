import typer

from app.models import Shops

application = typer.Typer()


@application.command()
def main():
    shop = Shops.get(id=2)
    typer.echo(shop.name)


if __name__ == "__main__":
    application()
