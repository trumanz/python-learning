#!/usr/bin/env python
import os
import logging
import sys
from paste import deploy
from wsgiref.simple_server import make_server

LOG = logging.getLogger(__name__)

module_dir = os.getcwd()
print module_dir

def server(app_name, conf_file):

    LOG.debug("loading");
    app = deploy.loadapp("config:" + conf_file , name=app_name)
    serve = make_server("0.0.0.0",8080,app)
    serve.serve_forever()
    
if __name__ == '__main__':
    app_name = "myapp"
    conf_file = os.path.abspath("config.ini")
    server(app_name,conf_file)
