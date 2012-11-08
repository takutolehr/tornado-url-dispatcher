import tornado.web
from app.controller.app_controller import AppController

class Test(AppController):

    def func_one(self):
        return

    def func_two(self):
        print self.get_argument('test', '')
        return
