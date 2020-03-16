from __future__ import (absolute_import, division, print_function)

import uuid

from odm2api import ServiceBase
from odm2api import ODM2Models

class CreateODM2(ServiceBase):
    
    def create_obj(self, obj):
        """
        Accepts one of the ODM2Models and submits it to the database
        
        obj = python class from ODM2Models
        
        """
        
        #validatation? Object not mapped
        
        self._session.add(obj)
        self._session.commit()
        self._session.close()
        return obj
    
    def create_dataframe(self, obj, dataframe):
        """
        Accepts a obj which represent the data structure of the table, and a pandas DataFrame, then bulk 
        inserts the DataFrame into the database.
        
        obj = python class from ODM2Models - note this can be empty
        dataframe = pandas dataframe
        """
        
        #validation - I wonder what the database will do with extra columns?
        #probably need to drop those? Return error?
        
        df.to_sql(
            name=obj.__tablename__,
            con=self._session
            schema=obj.__schema__
            index=False,
            if_exists='append'
        )
        
"""
#TODO - talk with Anthony about reducing this. He'll probably be ok with me axing it 
#why are we doing this to ourselves!!!!
class CreateODM2(ServiceBase):
    # Annotations

    #TODO - talk to Anthony about the need for some many create methods
    #At a minimum we should use private method to reduce the redundate code
    def __create__(self, value):
        self._session.add(value)
        self._session.commit()
        self._session.close()
        return value
        
    def create(self, value):
        return self.__create__(value)
    
    def createAll(self, values):
        return self.__create__(value)

    def createVariable(self, var):
        return self.__create__(value)

    def createMethod(self, method):
        return self.__create__(value)

    def createProcessingLevel(self, proclevel):
        return self.__create__(proclevel)
    
    def createSamplingFeature(self, samplingfeature):
        if samplingfeature.SamplingFeatureUUID is None:
            samplingfeature.SamplingFeatureUUID = str(uuid.uuid1())
        return self.__create__(samplingfeature)

    def createUnit(self, unit):
        return self.__create__(unit)

    def createOrganization(self, org):
        return self.__create__(ogr)
    
    def createPerson(self, person):
        return self.__create__(person)

    def createAffiliation(self, affiliation):
        return self.__create__(affiliation)

    def createDataset(self, dataset):
        return self.__create__(dataset)

    def createDatasetResults(self, datasetresult):
        return self.__create__(datasetresult)

    def createAction(self, action):
        return self.__create__(action)

    def createActionby(self, actionby):
        return self.__create__(actionby)
    
    def createFeatureAction(self, action):
        return self.__create__(action)
        
    def createAnnotations(self, anno):
        return self.__create__(anno)
        
    def createRelatedAction(self, relatedaction):
        return self.__create__(relatedaction)
    
    def createResult(self, result):
        if result.ResultUUID is None:
            result.ResultUUID = str(uuid.uuid1())
        return self.__create__(result)
    
    def createResultValue(self, value):
        return self.__create__(value)

    def createSpatialReference(self, spatialref):
        return self.__create__(spatialref)

    def createModel(self, model):
        return self.__create__(model)
    
    def createRelatedModel(self, relatedmodel):
        return self.__create__(relatedmodel)
    
    def createSimulation(self, simulation):
        return self.__create__(simulation)

    #This is pandas - but why not implement a general dataframe insert method
    def createTimeSeriesResultValues(self, datavalues):
        try:
            # TODO: PRT - need to look into this further - might need to revise method
            # FXIME: F841 local variable 'tablename' is assigned to but never used.
            # tablename = TimeSeriesResultValues.__tablename__
            datavalues.to_sql(
                name='TimeSeriesResultValues',
                schema=TimeSeriesResultValues.__table_args__['schema'],
                if_exists='append',
                chunksize=1000,
                con=self._session_factory.engine,
                index=False
            )
            self._session.commit()

            return datavalues
        except Exception as e:
            print(e)
            return None
            """