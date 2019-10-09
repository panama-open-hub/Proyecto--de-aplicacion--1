import sys
import os
import pohTorServer
import tornado
from tornado.options import define, options

print("The Python version is %s.%s.%s" % sys.version_info[:3])
define("port", default=8888, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    app = pohTorServer.Application()
    server = tornado.httpserver.HTTPServer(app)
    port=int(os.environ.get("PORT",options.port))
    server.listen(port)
    print("Listening at port",str(port))
    tornado.ioloop.IOLoop.instance().start()

    #TODO ADDDD FINALLY

if __name__ == "__main__":
    main()