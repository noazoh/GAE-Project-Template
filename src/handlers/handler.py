#　-*- coding: utf-8 -*-
import os
import webapp2
from src import main
from google.appengine.ext.webapp import template
from google.appengine.api import users

from logging import getLogger,StreamHandler,DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

class MainHandler(webapp2.RequestHandler):
    """
    /handler
    """
    def __init__(self, *args, **kwargs):
        #基底クラスの__init__()を呼ぶ
        super(MainHandler, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        logger.debug("query_string=" + self.request.query_string)
        logger.debug(kwargs)
        logger.debug(args)

        params = {
                  "param1": "param1",
                  "param2": "param2",
                  }
        fpath = os.path.join(main.TEMPLATEPATH, "index.html")
        html = template.render(fpath, params)
        self.response.out.write(html)
