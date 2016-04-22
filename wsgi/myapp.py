import routes
import logging
import routes.middleware
import webob.dec
import webob.exc

import api

class Router(object):

    def __init__(self, mapper=None):
        self.map =  mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,self.map)

    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls()

    @webob.dec.wsgify
    def __call__(self,req):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        return app


class MyApp(Router):

    def __init__(self, mapper=None):
        if(mapper == None):
            mapper = routes.Mapper()
        
        mapper.connect("/",controller= api.VersionAPI(), action="index")
        super(MyApp,self).__init__(mapper) 
