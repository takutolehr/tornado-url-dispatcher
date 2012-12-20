import tornado.web
class AppController:
    """"""
    dispatcher = None
    request = None

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.request = self.dispatcher.request

    """ OVERRIDE REQUEST HANDLER FUNCTIONS """
    
    def get_argument(self, key, val):
        return self.dispatcher.get_argument(key, val)

    def get_arguments(self, key, val):
        return self.dispatcher.get_arguments(key, val)

    def get_cookie(self, key):
        return self.dispatcher.get_cookie(key)
    
    def redirect(self, url):
        return self.dispatcher.redirect(url)
    
    def set_cookie(self, key, val):
        return self.dispatcher.set_cookie(key, val)
    
    def set_header(self, key, val):
        self.dispatcher.set_header(key, val)
    
    def write(self, val):
        self.dispatcher.write(val)
