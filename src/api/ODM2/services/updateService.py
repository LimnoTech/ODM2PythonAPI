from .. import serviceBase
from src.api.ODM2.models import *

from datetime import datetime

__author__ = 'jmeline'
# ################################################################################
# Annotations
# ################################################################################

class UpdateODM2(serviceBase):
    def test(self):
        return None


# ################################################################################
# CV
# ################################################################################




# ################################################################################
# Core
# ################################################################################
    def updateResultValidDateTime(self, resultId, dateTime):
        q = self._session.query(Results).filter(Results.ResultID==int(resultId)).update({'ValidDateTime':dateTime.to_datetime()})
        self._session.commit()


# ################################################################################
# Data Quality
# ################################################################################




# ################################################################################
# Equipment
# ################################################################################





# ################################################################################
# Extension Properties
# ################################################################################




# ################################################################################
# External Identifiers
# ################################################################################




# ################################################################################
# Lab Analyses
# ################################################################################




# ################################################################################
# Provenance
# ################################################################################




# ################################################################################
# Results
# ################################################################################




# ################################################################################
# Sampling Features
# ################################################################################




# ################################################################################
# Sensors
# ################################################################################



# ################################################################################
# ODM2
# ################################################################################

