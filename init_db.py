from app.schema import Base
from app.schema import engine


def database(db_engine) -> None:
    Base.metadata.drop_all(db_engine)  # type: ignore
    Base.metadata.create_all(db_engine)  # type: ignore

database(engine)
