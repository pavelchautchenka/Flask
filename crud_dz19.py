from sqlalchemy import select
from models_19 import Note, session


def get_all_notes():
    return session.execute(select(Note)).scalars().all()


def get_notes(uuid: str):
    query = select(Note).where(Note.uuid == uuid)

    return session.execute(query).scalar_one()


def create_notes(title: str, content: str):
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


def add_notes():
    session.add(Note(title='title1',content='content 1'))
    session.add(Note(title='title2', content='content 2'))
    session.commit()
