import os
import tornado.ioloop
import tornado.web
from app.lib.dispatcher import Dispatcher


settings = {
    "debug":True,
    "static_path": os.path.join(os.path.dirname(__file__), "app/webroot"),
    "cookie_secret": "9Dh193LadDfjOfLL024Foa582nNCmd",
    "xsrf_cookies": True,
}

Dispatcher.home = '/test/func_one'

application = tornado.web.Application([
    (r'/favicon\.ico', tornado.web.StaticFileHandler, {'path': ''}),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': ''}),
    (r"/.*", Dispatcher),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
