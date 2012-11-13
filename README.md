tornado-url-dispatcher
======================

Tornado web URL dispatcher used to impose a MVC pattern.


Accessing http://127.0.0.1:8888/{{controller_name}}/{{function_name}} executes def {{function_name}}(self) in /app/controller/{{controller_name}}.py.

By default {{function_name}} will render the template file /app/view/{{controller_name}}/{{function_name}}.

If you want the controller function to render a different template file, return 'template_file_name' from the function.


###Naming Conventions:

1. The controller file name must match {{controller_name}}.
    * ex. "test.py"
2. The controller class name must be {{controller_name}} capitalized.
    * ex. "Test"

###See it work:

1. python __main__.py
2. Go to 127.0.0.1:8888/test/func_one
