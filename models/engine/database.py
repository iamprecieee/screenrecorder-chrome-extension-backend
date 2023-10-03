from models.model import Video, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from typing import Union


classes = {"Video": Video}


class DBStorage:
    """ 
    These are class-level attributes with double underscores as name mangling. 
    They are used to store the SQLAlchemy database engine and session. 
    By using name mangling, you make these attributes private and only accessible within the class.
    """

    __engine = None
    __session = None

    def __init__(self):
        """ 
        The purpose of this __init__ method is to set up the initial configuration for database connectivity when an instance of the DBStorage class is created. 
        However, it doesn't establish a database connection or create a session at this point; it merely prepares the engine.
        """
        from resources.config import Config

        self.__engine = create_engine(Config.BASE_URI)

    def load(self):
        """
        This uses SQLAlchemy's create_all method to create database tables based on the defined models and their associated metadata.
        The create_all method uses this engine to establish a connection to the database and create tables if they don't already exist. 
        """

        Base.metadata.create_all(self.__engine)

        """ 
        A session factory is a callable that produces new SQLAlchemy session objects when called.
        """

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)

        """
        A scoped session is a special type of session that is intended for use in multi-threaded applications. 
        It manages sessions within a thread-local context.
        """

        Session = scoped_session(session_factory)

        """
        This establishes a database session used to interact with the database throughout the lifespan of the DBStorage instance.
        """

        self.__session = Session

    def new(self, obj: Video):
        """
        Adds a new object (e.g., a new video) to session and stages it for insertion into the database.
        """

        self.__session.add(obj)
        self.save()

    def save(self):
        """
        This method is used to commit changes made within the current database session.
        self.__session.commit() commits any pending changes (inserts, updates, deletes) to the database. 
        After committing, the changes become permanent in the database.
        """

        self.__session.commit()

    def all(self, cls_instance: Union[Video, str] = None):
        """ 
        This returns a list of all instances in the session.
        """

        if type(cls_instance) is str:
            cls_instance = classes.get(cls_instance)
        videos = []
        if cls_instance and cls_instance in classes.values():
            for cls_instance in classes.values():
                videos.extend(self.__session.query(cls_instance).all())
        return videos

    def get(self, cls_instance: Union[Video, str], id: str):
        """
        This returns a specific instance in the session by its id.
        """

        if type(cls_instance) is str:
            cls_instance = classes.get(cls_instance)
        if cls_instance is not None and cls_instance in classes.values():
            return self.__session.query(cls_instance).filter_by(id=id).first()

    def getFilename(self, cls_instance: Union[Video, str], filename: str):
        """
        This returns a specific instance in the session by its filename.
        """

        if type(cls_instance) is str:
            cls_instance = classes.get(cls_instance)
        if cls_instance is not None and cls_instance in classes.values():
            return self.__session.query(cls_instance).filter_by(filename=filename).first()

    def delete(self, cls_instance: Union[Video, str], id: str):
        """
        Deletes an instance of the model from the database using id
        """

        if type(cls_instance) is str:
            cls_instance = classes.get(cls_instance)
        if cls_instance is not None and cls_instance in classes.values():
            inst = self.__session.query(cls_instance).filter_by(id=id).first()
            self.__session.delete(inst)

    def close(self):
        """
        This deletes an instance of the model from the database.
        """

        self.__session.remove()
