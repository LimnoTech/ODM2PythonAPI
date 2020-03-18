from __future__ import (absolute_import, division, print_function)

import uuid

from odm2api.base import ServiceBase
from odm2api.base import ODM2Models

class CreateODM2(ServiceBase):
    
    def create_obj(self, obj):
        """
        Accepts one of the ODM2Models and submits it to the database
        
        obj : python class from ODM2Models
        """
        
        #validatation? Object not mapped
        
        self._session.add(obj)
        self._session.commit()
        self._session.close()
        #TODO - I'd like to see a response obj passed back with status, stack info if applicable, etc
        return obj
    
    def create_dataframe(self, obj, dataframe):
        """
        Accepts a obj which represent the data structure of the table, and a pandas DataFrame, then bulk 
        inserts the DataFrame into the database.
        
        obj : python class from ODM2Models - note this can be empty
        dataframe : pandas DataFrame with the data you intend to import
        """
        #TODO - consider need for validation
        #validation - I wonder what the database will do with extra columns?
        #probably need to drop those? Return error?
        
        df.to_sql(
            name=obj.__tablename__,
            con=self._session,
            schema=obj.__schema__,
            index=False,
            if_exists='append'
        )