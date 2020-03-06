from __future__ import (absolute_import, division, print_function)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine import reflection
from sqlalchemy import MetaData
from sqlalchemy import exc
import warnings

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

    #def __repr__(self):
    #    valuedict = self.__dict__.copy()
    #    for v in valuedict.keys():
    #        if 'obj' in v.lower():
    #            del valuedict[v]
    #
    #        if v == '_sa_instance_state':
    #            del valuedict['_sa_instance_state']
    #    return '<%s(%s)>' % (self.__class__.__name__, str(valuedict))

ModelBase = automap_base(cls=Base)
ODM2Models = None
initialized = False 
def init_api(engine):
    global ModelBase, ODM2Models, initialized 
    
    if not initialized:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=exc.SAWarning)
            try:
                insp = reflection.Inspector.from_engine(engine)
                metadata = MetaData(bind=engine)
                for schema in insp.get_schema_names():
                    if 'ODM2' in schema:
                        metadata.reflect(schema=schema)
                ModelBase.metadata = metadata
                ModelBase.prepare(reflect=True)
                initialized = True
                ODM2Models = ModelBase.classes
            except: #TODO we should figure out now to surpress these warning - this isn't it though
                #TODO raise appropreate error
                pass
            