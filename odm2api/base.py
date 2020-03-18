from __future__ import (absolute_import, division, print_function)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.engine import reflection
from sqlalchemy import MetaData, Table
from sqlalchemy import exc
import warnings

### Mapped after initialized ###
ODM2Models = None
ODM2Metadata = None
initialized = False 

### Services ###
class ServiceBase(object):
    def __init__(self,  session_maker, debug=False):
        """Must send in either a session_factory."""
        self._session_maker = session_maker
        self._session = self._session_maker()
        self._debug = debug

    def getSession(self):
        if self._session is None:
            self._session = self._session_maker()

        return self._session

    def reset_session(self):
        self._session = self._session_maker()   
        
from odm2api.services import CreateODM2,ReadODM2,UpdateODM2,DeleteODM2    
class ODM2Services(object):
    """
    Base object which provides access to ODM2 CRUD 
    (Create, Read, Update, Delete) services. 
    
    session_maker: sqlalchemy sessionmaker object
    debug: legacy parameter from version 1 of ODM2 api, not currently implementing
    """  

    def __init__(self, session_maker, debug=False):
        from odm2api.services import createService, readService, updateService, deleteService     
        self.create = createService.CreateODM2(session_maker)
        self.read = readService.ReadODM2(session_maker)
        self.update = updateService.UpdateODM2(session_maker)
        self.delete = deleteService.DeleteODM2(session_maker)
        
### Models ###
class Base(object):
    from sqlalchemy.ext.declarative import declared_attr

    @declared_attr
    def __tablename__(self):
        return self.__name__

    def __init__(self, *args, **kwargs):
        for name, value in self.classes.items():
            setattr(self, name, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    @declared_attr
    def __table__(self):
        global ODM2Metadata
        
        if ODM2Metadata is None:
            #not initialized
            return None
        else:
            table = None
            for key in ODM2Meta.tables.keys():
                if '.' + obj.__tablename__ in key:
                    table = ODM2Meta.tables[key]
            return table
        
    @declared_attr
    def __schema__(self):
        table = self.__table__
        if table is not None: return table.schema
        else: return None

### Init ###
ModelBase = automap_base(cls=Base)
def init_api(engine):
    global ModelBase, ODM2Models, ODM2Metadata, initialized 
    
    tables = {}
    if not initialized:
    #TODO - I removed the try catch here for development because it was preventing my from setting stack trace. Need to reimplement
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=exc.SAWarning)
            insp = reflection.Inspector.from_engine(engine)
            metadata = MetaData(bind=engine)
            for schema in insp.get_schema_names():
                if 'ODM2' in schema:
                    metadata.reflect(schema=schema)
                    for table_name in insp.get_table_names(schema=schema):
                        #we don't pass tables back, but by binding engine to their metadata to engine
                        #we'll get only the proper tables
                        tables[table_name] = Table(table_name, MetaData(bind=engine, schema=schema))
            ModelBase.metadata = metadata
            ModelBase.prepare(reflect=True)
            ODM2Models = ModelBase.classes
            initialized = True

            #TODO raise appropreate error
            #pass
