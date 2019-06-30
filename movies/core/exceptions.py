
class MoviesError(Exception):

    status_code = 500

    def __init__(self, message, status_code=status_code, details=[]):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.details = details
