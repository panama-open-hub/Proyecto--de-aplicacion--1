import sys
import os
from datetime import datetime, date,timedelta
from time import gmtime, strftime,sleep
import logging
import asyncio
import json
import sqlite3
import tornado.ioloop
import tornado.web
from tornado import gen,ioloop, web
from tornado.gen import multi
from tornado.options import define, options
from modules import pohLcd, pohLed


print("The Python version is %s.%s.%s" % sys.version_info[:3])
define("port", default=8888, help="run on the given port", type=int)

_data = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@admin.com",
        "password": 1234
    }]

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        data_json = json.dumps(_data)
        if data_json:
            exp = json.loads(data_json)
        else:
            exp = None
        self.render("index.html", data=exp)

class Application(tornado.web.Application):
    def __init__(self):
        #self.device = Device()

        handlers = [
            (r'/', HomeHandler),
            #(r"/postdata",PostData),
            #(r"/stop", StopServer),
            #(r"/api/user", Hello),
            #(r"/api/sensors", Hello),
            #(r"/version", VersionHandler),
            #(r"/hello", Hello),
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

def main():
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    port=int(os.environ.get("PORT",options.port))
    server.listen(port)
    print("Listening at port 8888")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()