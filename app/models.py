from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class KeyStore(Base):
    __tablename__ = "key_store"

    id = Column(
        Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )

    owner_id = Column(
        Integer,
        nullable=False
    )

    mail_id = Column(
        Integer,
        unique=True,
        nullable=False,
    )

    key = Column(
        String(64),
        nullable=False
    )

    iv = Column(
        String(32),
        nullable=False
    )

    creation_date = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )

    def __repr__(self):
        return f"<KeyStore id={self.id}>"
