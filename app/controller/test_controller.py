import tornado.web
from app.controller.app_controller import AppController
from app.model.test import Test

class TestController(AppController):

    def func_one(self):
        return

    def func_two(self):
        name = self.get_argument('name', '')
        return {'name':name} # Set the variables to render in the view file.
    
    def func_three(self):

        if 'POST' == self.request.method:
            """ Process post value. """
            self.set_flash('Submission successful.')
            return self.redirect('/test/func_one') # Redirect to func_one.
        return
