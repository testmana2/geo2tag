from pymongo import MongoClient
import sys
from basic_integration_test import BasicIntegrationTest
import requests
import json

plugins = MongoClient()['geomongo']['plugins']


class TestGeocodingJob(BasicIntegrationTest):
	def setUp(self):
		plugins.insert({'name': 'geocoder', 'enabled': True})

	def testGeocodingJob(self):
		r = requests.get(
			self.getUrl(
				'/instance/plugin/geocoder/service/testservice/job'
			)
		)
		print r.text
		self.assertEqual(type(json.loads(r.text)), type(list()))
		self.assertEqual(r.status_code, 200)
