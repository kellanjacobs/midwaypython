from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship

from .meta import Base

class Horse(Base):
    """ The SQLAlchemy declarative model class for a Horse object. """
    __tablename__ = 'horses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    str = Column(Integer, nullable=False, default=0)
    active = Column(Integer, nullable=False, default=1)
    races = relationship('Race', back_populates="horse")

    def __repr__(self):
        return self.name
