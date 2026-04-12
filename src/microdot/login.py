from time import time
from microdot import redirect
from microdot.microdot import urlencode, invoke_handler


class Login:
    """User login support for Microdot.

    :param login_url: the URL to redirect to when a login is required. The
                      default is '/login'.
    """
    def __init__(self, login_url='/login'):
        self.login_url = login_url
        self.user_loader_callback = None

    def user_loader(self, f):
        """Decorator to configure the user callback.

        The decorated function receives the user ID as an argument and must
        return the corresponding user object, or ``None`` if the user ID is
        invalid.
        """
        pass





    async def login_user(self, request, user, remember=False,
                         redirect_url='/'):
        """Log a user in.

        :param request: the request object
        :param user: the user object
        :param remember: if the user's logged in state should be remembered
                         with a cookie after the session ends. Set to the
                         number of days the remember cookie should last, or to
                         ``True`` to use a default duration of 30 days.
        :param redirect_url: the URL to redirect to after login

        This call marks the user as logged in by storing their user ID in the
        user session. The application must call this method to log a user in
        after their credentials have been validated.

        The method returns a redirect response, either to the URL the user
        originally intended to visit, or if there is no original URL to the URL
        specified by the `redirect_url`.
        """
        pass

    async def logout_user(self, request):
        """Log a user out.

        :param request: the request object

        This call removes information about the user's log in from the user
        session. If a remember cookie exists, it is removed as well.
        """
        pass

    async def get_current_user(self, request):
        """Return the currently logged in user."""
        pass

    def __call__(self, f):
        """Decorator to protect a route with authentication.

        If the user is not logged in, Microdot will redirect to the login page
        first. The decorated route will only run after successful login by the
        user. If the user is already logged in, the route will run immediately.
        Example::

            login = Login()

            @app.route('/secret')
            @login
            async def secret(request):
                # only accessible to authenticated users

        """

        return wrapper

    def fresh(self, f):
        """Decorator to protect a route with "fresh" authentication.

        This decorator prevents the route from running when the login session
        is not fresh. A fresh session is a session that has been created from
        direct user interaction with the login page, while a non-fresh session
        occurs when a login is restored from a "remember me" cookie. Example::

            login = Login()

            @app.route('/secret')
            @auth.fresh
            async def secret(request):
                # only accessible to authenticated users
                # users logged in via remember me cookie will need to
                # re-authenticate
        """
        pass
