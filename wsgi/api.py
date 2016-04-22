import httplib
import json
import webob.dec

from webob import Response

class VersionAPI(object):
    def __init__(self):
        self.version = "0.1"

    def index(self,req):
        response = Response(request=req,
                                  status=httplib.MULTIPLE_CHOICES,
                                  content_type='application/json')
        response.body = json.dumps(dict(versions=self.version))
        return response
            
    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)

