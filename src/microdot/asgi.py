import asyncio
import os
import signal
from microdot import *  # noqa: F401, F403
from microdot.microdot import Microdot as BaseMicrodot, Request, Response, \
    NoCaseDict, abort
from microdot.websocket import WebSocket as BaseWebSocket, websocket_wrapper


class _BodyStream:  # pragma: no cover
    def __init__(self, receive):
        self.receive = receive
        self.data = b''
        self.more = True

    async def read_more(self):
        if self.more:
            packet = await self.receive()
            self.data += packet.get('body', b'')
            self.more = packet.get('more_body', False)

    async def read(self, n=-1):
        while self.more and len(self.data) < n:
            await self.read_more()
        if len(self.data) < n:
            data = self.data
            self.data = b''
            return data

        data = self.data[:n]
        self.data = self.data[n:]
        return data

    async def readline(self):
        return await self.readuntil()

    async def readexactly(self, n):
        return await self.read(n)

    async def readuntil(self, separator=b'\n'):
        if self.more and separator not in self.data:
            await self.read_more()
        data, self.data = self.data.split(separator, 1)
        return data


class Microdot(BaseMicrodot):  # type: ignore[no-redef]
    """A subclass of the core :class:`Microdot <microdot.Microdot>` class that
    implements the ASGI protocol.

    :param startup: An optional function to handle the `lifespan.startup` ASGI
                    signal.
    :param shutdown: An optional function to handle the `lifespan.shutdown`
                     ASGI signal.

    This class must be used as the application instance when running under an
    ASGI web server.
    """
    def __init__(self, lifespan_startup=None, lifespan_shutdown=None):
        super().__init__()
        self.lifespan_startup = lifespan_startup
        self.lifespan_shutdown = lifespan_shutdown
        self.embedded_server = False


    async def asgi_app(self, scope, receive, send):
        """An ASGI application."""
        pass

    async def __call__(self, scope, receive, send):
        return await self.asgi_app(scope, receive, send)


    def run(self, host='0.0.0.0', port=5000, debug=False,
            **options):  # pragma: no cover
        """Normally you would not start the server by invoking this method.
        Instead, start your chosen ASGI web server and pass the ``Microdot``
        instance as the ASGI application.
        """
        pass


class WebSocket(BaseWebSocket):  # pragma: no cover

    async def receive(self):
        message = await self.request.sock[0]()
        if message['type'] == 'websocket.disconnect':
            raise OSError(32, 'Websocket connection closed')
        elif message['type'] != 'websocket.receive':
            raise OSError(32, 'Websocket message type not supported')
        return message.get('bytes', message.get('text'))

    async def send(self, data):
        if isinstance(data, str):
            await self.request.sock[1](
                {'type': 'websocket.send', 'text': data})
        else:
            await self.request.sock[1](
                {'type': 'websocket.send', 'bytes': data})

    async def close(self):
        if not self.closed:
            self.closed = True
            try:
                await self.request.sock[1]({'type': 'websocket.close'})
            except:  # noqa E722
                pass


async def websocket_upgrade(request):  # pragma: no cover
    """Upgrade a request handler to a websocket connection.

    This function can be called directly inside a route function to process a
    WebSocket upgrade handshake, for example after the user's credentials are
    verified. The function returns the websocket object::

        @app.route('/echo')
        async def echo(request):
            if not (await authenticate_user(request)):
                abort(401)
            ws = await websocket_upgrade(request)
            while True:
                message = await ws.receive()
                await ws.send(message)
    """
    pass


def with_websocket(f):  # pragma: no cover
    """Decorator to make a route a WebSocket endpoint.

    This decorator is used to define a route that accepts websocket
    connections. The route then receives a websocket object as a second
    argument that it can use to send and receive messages::

        @app.route('/echo')
        @with_websocket
        async def echo(request, ws):
            while True:
                message = await ws.receive()
                await ws.send(message)
    """
    pass
