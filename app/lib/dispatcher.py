"""
Copyright (c) 2012 Takuto Lehr

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import tornado.web
    
class Dispatcher(tornado.web.RequestHandler):
    
    home = ''
    
    def get(self):
        self.__render()

    def post(self):
        self.__render()

    def __render(self):

        if '/' == self.request.uri:
            self.request.uri = self.home

        uri = self.request.uri.split('?', 1)[0].split('/')[1:]
        args = self.request.uri.split('?', 1)[0].split('/')[3:]
        _class_name = uri[0].capitalize()+'Controller'
        _method_name = uri[1]
        
        _temp = __import__('app.controller.'+uri[0]+'_controller', globals(), locals(), [_class_name], -1)
        _class = getattr(_temp, _class_name)
        _class = _class(self.application, self.request)
        _method = getattr(_class, _method_name)

        data = _method(*args)
        if not(isinstance(data, dict)):
            data = {}

        if '__redirect' in data:
            self.redirect(data['__redirect'])

        template_file = None
        if '__template_file' in data:
            template_file = data['__template_file']

        if None == template_file:
            template_file = _method_name

        template_dir = os.path.dirname(__file__)+'/../view/'
        data['__template_dir'] = template_dir
        data['__template_path'] = template_dir+uri[0]+'/'+template_file
        self.render(template_dir+'layout/default', data=data)

