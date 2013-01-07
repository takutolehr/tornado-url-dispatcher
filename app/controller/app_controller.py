import tornado.web
import base64
class AppController:
    """"""
    dispatcher = None
    request = None

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.request = self.dispatcher.request

    def set_flash(self, message):
        self.set_cookie('__flash',base64.b64encode(message))
        return

    """ OVERRIDE REQUEST HANDLER FUNCTIONS """
    
    def clear_cookie(self, key):
        return self.dispatcher.clear_cookie(key)
    
    def get_argument(self, key, val):
        return self.dispatcher.get_argument(key, val)

    def get_arguments(self, key, val):
        return self.dispatcher.get_arguments(key, val)

    def get_cookie(self, key):
        return self.dispatcher.get_cookie(key)
    
    def redirect(self, url):
        self.dispatcher.redirect(url)
        return 'exit'
    
    def set_cookie(self, key, val):
        return self.dispatcher.set_cookie(key, val)
    
    def set_header(self, key, val):
        self.dispatcher.set_header(key, val)
    
    def set_secure_cookie(self, key, val):
        return self.dispatcher.set_secure_cookie(key, val)
    
    def write(self, val):
        self.dispatcher.write(val)
