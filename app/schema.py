import typing as t

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as base
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(settings.DB_DSN, echo=settings.APP_DEBUG)
SessionFactory = sessionmaker(bind=engine)


def declarative_base() -> t.Callable[[object], object]:
    return lambda cls: base(cls=cls)


@declarative_base()
class Base(object):
    @property
    def columns(self) -> t.List[str]:
        return [c.name for c in self.__table__.columns]  # type: ignore

    @property
    def column_items(self) -> t.Dict[str, str]:
        return dict([(c, getattr(self, c)) for c in self.columns])

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.column_items})'

    def to_json(self) -> t.Dict[str, str]:
        return self.column_items


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    photo_link = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    group = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    fav_colour = Column(String, nullable=False)


students_table = Student.__table__  # type: ignore
