from unittest import TestCase
from db_model import getServiceList, getDbObject
SERVICES = 'services'
NAME = 'name'


class GetServiceListTest(TestCase):

    def testGetServiceListTest(self):
        db = getDbObject()
        FIRST_OBJ = list(db[SERVICES].find().sort(NAME, 1).skip(0).limit(1))[0]
        COUNT = db[SERVICES].find().count()
        if COUNT > 1:
            LAST_OBJ = list(
                db[SERVICES].find().sort(
                    NAME, -1).skip(0).limit(1))[0]
            list(db[SERVICES].find())
            RESULT = getServiceList(COUNT, 0)
            self.assertEqual(RESULT[0], FIRST_OBJ)
            self.assertEqual(RESULT[COUNT - 1], LAST_OBJ)
            RESULT = getServiceList(None, None)
            self.assertEqual(RESULT[0], FIRST_OBJ)
            self.assertEqual(RESULT[COUNT - 1], LAST_OBJ)
