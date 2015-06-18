#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
sys.path.append('../')
from db_model import addChannel
from config_reader import getHost, getPort

TEST_SERVICE = 'testservice'
NAME = 'test_name'
JSON = 'test_json'
OWNER_ID = 'test_owner_id'
OWNER_GROUP = 'STUB'
SERVICE_NAME = 'testservice'
ACl = 777

db = MongoClient(getHost(), getPort())[SERVICE_NAME]

class TestAddChannel(unittest.TestCase):
    def testAddChannel(self):
    	result = addChannel(NAME, JSON, OWNER_ID, SERVICE_NAME)
    	self.assertNotEqual(result, None)
    	self.assertNotEquals(list(db['channels'].find({'_id': result})), [])
