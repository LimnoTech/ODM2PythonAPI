from __future__ import (absolute_import, division, print_function)

import uuid

from odm2api import ServiceBase

class CreateODM2(ServiceBase):
    # Annotations

    #TODO - talk to Anothony about the need for some many create methods
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
