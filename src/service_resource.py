from flask import request
from flask.ext.restful import Resource

class ServiceResource(Resource):
    def get(self, serviceName):
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        return {serviceName: 'Service removed'}  

