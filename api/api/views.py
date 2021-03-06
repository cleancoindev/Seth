""" Cornice services.
"""
from cornice.resource import resource, view
from db import get_all, get_single, insert
from json import loads

@resource(collection_path='/missions', path='/missions/{id}', cors_origins=('*',))
class Missions(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):
        return get_all(delim=['name','image','agency','description','date'])

    def collection_post(self):
        values = self.request.params
        insert(dict(values))
        return "Mission Created"

    def get(self):
        return get_single(str(self.request.matchdict['id']))

