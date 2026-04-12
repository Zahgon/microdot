import asyncio
import os
import signal
from microdot import *  # noqa: F401, F403
from microdot.microdot import Microdot as BaseMicrodot, Request, NoCaseDict, \
    MUTED_SOCKET_ERRORS
from microdot.websocket import WebSocket, websocket_upgrade, \
    with_websocket  # noqa: F401


class Microdot(BaseMicrodot):  # type: ignore[no-redef]
    """A subclass of the core :class:`Microdot <microdot.Microdot>` class that
    implements the WSGI protocol.

    This class must be used as the application instance when running under a
    WSGI web server.
    """
    def __init__(self):
        super().__init__()
        self.loop = asyncio.new_event_loop()
        self.embedded_server = False

    def wsgi_app(self, environ, start_response):
        """A WSGI application callable."""
        pass

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


    def run(self, host='0.0.0.0', port=5000, debug=False,
            **options):  # pragma: no cover
        """Normally you would not start the server by invoking this method.
        Instead, start your chosen WSGI web server and pass the ``Microdot``
        instance as the WSGI callable.
        """
        pass
