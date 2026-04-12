from microdot import abort
from microdot.microdot import invoke_handler


class BaseAuth:
    def __init__(self):
        self.auth_callback = None
        self.error_callback = None

    def __call__(self, f):
        """Decorator to protect a route with authentication.

        An instance of this class must be used as a decorator on the routes
        that need to be protected. Example::

           auth = BasicAuth()  # or TokenAuth()

           @app.route('/protected')
           @auth
           def protected(request):
               # ...

        Routes that are decorated in this way will only be invoked if the
        authentication callback returned a valid user object, otherwise the
        error callback will be executed.
        """

        return wrapper

    def optional(self, f):
        """Decorator to protect a route with optional authentication.

        This decorator makes authentication for the decorated route optional,
        meaning that the route is allowed to run with or with
        authentication given in the request.
        """
        pass


class BasicAuth(BaseAuth):
    """Basic Authentication.

    :param realm: The realm that is displayed when the user is prompted to
                  authenticate in the browser.
    :param charset: The charset that is used to encode the realm.
    :param scheme: The authentication scheme. Defaults to 'Basic'.
    :param error_status: The error status code to return when authentication
                         fails. Defaults to 401.
    """
    def __init__(self, realm='Please login', charset='UTF-8', scheme='Basic',
                 error_status=401):
        super().__init__()
        self.realm = realm
        self.charset = charset
        self.scheme = scheme
        self.error_status = error_status
        self.error_callback = self.authentication_error



    def authenticate(self, f):
        """Decorator to configure the authentication callback.

        This decorator must be used with a function that accepts the request
        object, a username and a password and returns a user object if the
        credentials are valid, or ``None`` if they are not. Example::

           @auth.authenticate
           async def check_credentials(request, username, password):
               user = get_user(username)
               if user and user.check_password(password):
                   return get_user(username)
        """
        pass


class TokenAuth(BaseAuth):
    """Token based authentication.

    :param header: The name of the header that will contain the token. Defaults
                   to 'Authorization'.
    :param scheme: The authentication scheme. Defaults to 'Bearer'.
    :param error_status: The error status code to return when authentication
                         fails. Defaults to 401.
    """
    def __init__(self, header='Authorization', scheme='Bearer',
                 error_status=401):
        super().__init__()
        self.header = header
        self.scheme = scheme.lower()
        self.error_status = error_status
        self.error_callback = self.authentication_error


    def authenticate(self, f):
        """Decorator to configure the authentication callback.

        This decorator must be used with a function that accepts the request
        object, a username and a password and returns a user object if the
        credentials are valid, or ``None`` if they are not. Example::

           @auth.authenticate
           async def check_credentials(request, token):
               return get_user(token)
        """
        pass

    def errorhandler(self, f):
        """Decorator to configure the error callback.

        Microdot calls the error callback to allow the application to generate
        a custom error response. The default error response is to call
        ``abort(401)``.
        """
        pass

