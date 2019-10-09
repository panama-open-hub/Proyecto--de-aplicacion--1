import os
import time
import logging
import asyncio
import json
import tornado.ioloop
import tornado.web
from tornado import gen,ioloop, web
from tornado.gen import multi
from tornado.options import define, options

_dummyData = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@admin.com",
        "password": 1234
    }]

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomeHandler),
            (r'/home', HomeHandler),
            #(r"/postdata",PostData),
            (r"/stop", StopServer),
            #(r"/api/user", Hello),
            #(r"/api/sensors", Hello),
            #(r"/version", VersionHandler),
            (r"/hello", Hello),
            #(r"/user/", User),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,

            cookie_secret=str(os.urandom(45)),
            #xsrf_cookies=True,
            autoreload=True,
            gzip=True,
            login_url="/login",
            autoescape=None   
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class Hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        data_json = json.dumps(_dummyData)
        if data_json:
            exp = json.loads(data_json)
        else:
            exp = None
        self.render("index.html", data=exp)

class StopServer(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado server stopped")
        tornado.ioloop.IOLoop.instance().stop()