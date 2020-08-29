import typer

from app.migrations.tables import create_tables
from app.migrations.data import insert_data


application = typer.Typer()


@application.command()
def create():
    create_tables()
    insert_data()


if __name__ == "__main__":
    application()
