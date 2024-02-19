from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import argon2

import datetime
import os

from sqlalchemy import (BigInteger, DateTime, Identity, SmallInteger,
                        create_engine)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """ User model """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password: str):
        """ hash the password and set it to the password_hash attribute

        Args:
            password (str): the password to hash
        """
        self.password_hash = argon2.hash(password)

    def check_password(self, password : str):
        """ check if the password is correct

        Args:
            password (str): the password to check

        Returns:
            bool: True if the password is correct, False otherwise
        """
        return argon2.verify(password, self.password_hash)


class CommonMixin():
    """ Common columns for all tables """
    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(),
        primary_key=True
    )
    time_created: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

class Queries(CommonMixin, db.Model):
    __tablename__ = 'queries'

    query_text: Mapped[str] = mapped_column(
        db.Text,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        db.ForeignKey('users.id'),
        nullable=False
    )
    prompt_tokens: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True
    )
    completion_tokens: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True
    )
    total_tokens: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True
    )
    cost: Mapped[float] = mapped_column(
        db.Float,
        nullable=True
    )


class QueryResults(CommonMixin, db.Model):
    __tablename__ = 'query_results'

    query_id: Mapped[int] = mapped_column(
        db.ForeignKey('queries.id'),
        nullable=False
    )
    result: Mapped[str] = mapped_column(
        db.Text,
        nullable=False,
        default='Error occured'
    )
    execution_time: Mapped[float] = mapped_column(
        db.Float,
        nullable=False
    )
    intermediate_steps: Mapped[str] = mapped_column(
        db.Text,
        nullable=True
    )


class Contacts(CommonMixin, db.Model):
    __tablename__ = 'contacts'

    name: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False
    )
    subject: Mapped[str] = mapped_column(
        db.String(200),
        nullable=False
    )
    message: Mapped[str] = mapped_column(
        db.Text,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        db.ForeignKey('users.id'),
        nullable=True
    )