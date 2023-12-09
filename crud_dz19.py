from sqlalchemy import select
from models_19 import User, session


def get_user(username: str) -> User:
    with session() as conn:
        query = select(User).where(User.username == username)

        return conn.execute(query).scalar_one()


def create_user(username: str, password: str, email: str) -> User:
    with session() as conn:
        user = User(username=username, password=password, email=email)
        conn.add(user)
        conn.commit()
        conn.refresh(user)
    return user


def get_all_users() -> list[User]:
    with session() as conn:
        return conn.execute(select(User)).scalars().all()


def add_users():
    with session() as connection:
        user = User(username="igor", password="PASSWORD", email="igor@mail.com")


        connection.add(user)
        connection.add(
            User(username="user123", password="PASSWORD", email="user123@mail.com")
        )
        connection.add(
            User(username="user111", password="PASSWORD", email="user111@mail.com")
        )
        connection.add(
            User(username="user999", password="PASSWORD", email="user999@mail.com")
        )

        connection.commit()
