class AppModel(object):
    
    connection = None

    def _connect(self, host='localhost', db='my_database'):
        """ Set self.connection to your database connection object. """
        self.connection = None
        return
