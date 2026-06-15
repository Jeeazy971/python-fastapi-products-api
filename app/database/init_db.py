from pathlib import Path

from app.database.session import Base, engine
from app.models.goal import Goal


def create_db_and_tables():
    Path("data").mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_db_and_tables()
    print("Database initialized")
