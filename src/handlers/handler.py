#　-*- coding: utf-8 -*-
import logging
import os, webapp2
from src import main
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    """
    /handler
    """
    def __init__(self, *args, **kwargs):
        #基底クラスの__init__()を呼ぶ
        super(MainHandler, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        logging.debug("query_string=" + self.request.query_string)
        logging.debug(kwargs)
        logging.debug(args)

        params = {
                  "param1": "param1",
                  "param2": "param2",
                  }
        fpath = os.path.join(main.TEMPLATEPATH, "index.html")
        html = template.render(fpath, params)
        self.response.out.write(html)
