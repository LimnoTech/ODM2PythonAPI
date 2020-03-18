from __future__ import (absolute_import, division, print_function)

__author__ = 'jmeline'

from datetime import datetime

from odm2api.base import ServiceBase
from odm2api.base import ODM2Models

class UpdateODM2(ServiceBase):
    
    def update(self, obj):
        self._session.add(obj)
        self._session.commit()
        self._session.close()
        return obj

    #TODO - review and decide what bit of this should be kept.    
    # ################################################################################
    # Core
    # ################################################################################
    def updateResultValidDateTime(self, resultId, dateTime):

        # check type of "validdatetime'
        # if not datetime do this:
        # dt = dateTime.to_datetime()
        # else dt = dateTime
        if (type(dateTime) != datetime):
            dt = dateTime.to_datetime()
        else:
            dt = dateTime
            q = self._session.query(Results).filter(Results.ResultID == int(resultId))
            q.update({'ValidDateTime': dt})

            self._session.commit()

    def updateResult(self, resultID=None, valuecount=None, result=None):
        if resultID:
            q = self._session.query(Results).filter(Results.ResultID == int(resultID))
            if valuecount:
                q.update({'ValueCount': valuecount})
        if result:
            self._session.add(result)
        self._session.commit()

    def updateAction(self, actionID=None, begin=None, end=None, action=None):
        if actionID:
            q = self._session.query(Actions).filter(Actions.ActionID == int(actionID))
            # if (type(begin) != datetime):
            #     begin = begin.to_datetime()
            # if (type(end) != datetime):
            #     end = end.to_datetime()

            if begin:
                q.update({'BeginDateTime': begin})
            if end:
                q.update({'EndDateTime': end})
        elif action:
            self._session.add(action)
        self._session.commit()
