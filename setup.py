from app.migrations.tables import create_tables
from app.migrations.data import insert_data


if __name__ == "__main__":
    create_tables()
    insert_data()
