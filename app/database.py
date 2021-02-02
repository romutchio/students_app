from .models import Student
from .schema import students_table
from contextlib import contextmanager
import logging
import typing as t

from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.sql import Update

from .schema import SessionFactory


logger = logging.getLogger(__name__)


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session: Session = SessionFactory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def insert(student: Student) -> None:
    with session_scope() as session:
        query = students_table.insert().values(**student.dict())
        session.execute(query)


def get_by_id(student_id: int) -> t.Optional[Student]:
    query = students_table.select().where(students_table.c.id == student_id)
    with session_scope() as session:
        result = session.execute(query).fetchone()
        if not result:
            return None
        else:
            return Student.from_orm(result)


def get_by_full_name(full_name: str) -> t.Optional[Student]:
    query = students_table.select().where(students_table.c.full_name == full_name)
    with session_scope() as session:
        result = session.execute(query).fetchone()
        if not result:
            return None
        else:
            return Student.from_orm(result)


def get_all() -> t.List[Student]:
    query = students_table.select().order_by(students_table.c.id)
    with session_scope() as session:
        result = session.execute(query)
        students: t.List[Student] = []
        for row in result:
            try:
                students.append(Student.from_orm(row))
            except ValidationError as e:
                logger.exception(e)
        return students


def delete(id: int) -> None:
    with session_scope() as session:
        query: Update = students_table.delete(students_table.c.id == id)
        session.execute(query)
