import unittest
import os
from flask import Flask
import flask_restful as restful
from flask_restful import Api
from main import initApp
from plugin_routines import getPluginList


class TestGt1417(unittest.TestCase):

    def testGt1417(self):
        app = Flask(__name__)
        api = Api(app)
        initApp(api)
        resources = api.endpoints
        self.assertTrue('resource_gt_1416' in resources)
        self.assertTrue('resource_gt_1417' in resources)
