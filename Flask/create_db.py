from Flask.models.models import User
from Flask.backend.db import engine, Base


def create_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
