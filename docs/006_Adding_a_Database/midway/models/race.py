from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Race(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    race_number = Column(Integer, nullable=False)
    place = Column(Integer, default=99)
    horse_id = Column(ForeignKey('horses.id'), nullable=False)
    horse = relationship('Horse', back_populates="races")
