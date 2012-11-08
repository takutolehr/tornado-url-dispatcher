import os
import tornado.web
    
class Dispatcher(tornado.web.RequestHandler):
    
    def get(self):
        self.__render()

    def post(self):
        self.__render()

    def __render(self):
        
        uri = self.request.uri.split('?', 1)[0].split('/')[1:]
        
        _class_name = uri[0].capitalize()
        _method_name = uri[1]
        _temp = __import__('app.controller.'+uri[0], globals(), locals(), [_class_name], -1)
        _class = getattr(_temp, _class_name)
        _class = _class(self.application, self.request)
        _method = getattr(_class, _method_name)
        temp_file = _method()
        if None == temp_file:
            temp_file = uri[1]

        template_dir = os.path.dirname(__file__)+'/../view/'+uri[0]+'/'
        
        self.render(template_dir+temp_file)
