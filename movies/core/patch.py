"""MonkeyPatch to fix flask-restplus error handler issues"""

from flask_restplus import Api

def patched_error_router(self, original_handler, e):
    """

    :param self:
    :param original_handler:
    :param e:
    :return:
    Fixed version of Flask-restplus api.handle_error()
    issues (see:
    https://github.com/noirbizarre/flask-restplus/issues/340)
    Logic: Currently Flask-restplus only recognizes
    exceptions on exact matches. Instead of handling inherited
    exceptions correctly It is returning 'Internal Server Error'
    When an error handler is defined for the parent exception..
    Thus, if you define an errorhandler for SQLAlchemyException,
    it will not be applied, when any would descendant (DataError, DBAPIError, CompileError, etc.)
    would occure. Which behavior is the exact opposite against
    python's error handling policy.
    Therefore, we do here is the following:
    We "don't trust" if an 'Internal Server Error' was returned
    from Flask-restplus... But in this case, we still call
    Flask's error handler (that is handling inhertiance
    The original function code is very similar to our
    implementation.
    """
    if self._has_fr_route():
        try:
            resp = self.handle_error(e)
            if resp.status_code != 500:
                return resp
        except Exception:
            pass
        return original_handler


Api.error_router = patched_error_router