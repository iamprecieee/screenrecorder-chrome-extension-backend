from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, LargeBinary
from uuid import uuid4
from datetime import datetime
import models


""" Creates a base class for all SQLAlchemy models """
Base = declarative_base()


class Video(Base):
    __tablename__ = "videos"

    """ 
    Defines class attributes for the BaseModel class
    """

    id = Column(String(60), primary_key=True, unique=True, default=str(uuid4))
    filename = Column(String(120))
    extension = Column(String)
    size = Column(String)
    resolution = Column(String)
    data = Column(LargeBinary)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    transcript = Column(String)

    def __init__(self, filename, extension, size, resolution, data, transcript):
        self.id = str(uuid4())
        self.filename = filename
        self.data = data
        self.extension = extension
        self.size = size
        self.resolution = resolution
        self.transcript = transcript
        models.storage.new(self)

    def save(self):
        models.storage.save()
