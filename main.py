import sys
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
import gpiozero #BCM pin numbering

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/home", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()