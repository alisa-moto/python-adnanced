from sqlalchemy import Column, Integer, String, ForeignKey
from HW_site.library.data_base.sql_units.base_sqlalchemy import Base
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class UserCredentials(Base, UserMixin):
    __tablename__ = 'user_credentials'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)

    reader = relationship('Reader', backref='readers')

    def __init__(self, email: str, password: str, reader_id: int) -> None:
        self.email = email
        self.password = password
        self.reader_id = reader_id

    def __str__(self):
        return f'User with id {self.reader_id} has email {self.email} and password {self.password}'
