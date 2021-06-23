from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import time


class TestWS(AsyncWebsocketConsumer):
    groups = ["broadcast"]

    async def ws_timeout(self):
        # await asyncio.sleep(30)
        # print("closing connection after timeout")
        # await self.close() 
        max_wait=10
        while (diff:=time.time()-self.last_client_interact)<=max_wait:
            await self.send(text_data="closing connection in {0:.2f}".format(max_wait-diff))
            await asyncio.sleep(2)
        await self.send(text_data="closing connection after timeout")
        await self.close() 


    async def connect(self):
        await self.accept()

        self.last_client_interact=time.time()

        # await self.accept("subprotocol")
        asyncio.ensure_future(self.ws_timeout())

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Received, "+text_data)
        self.last_client_interact=time.time()
        # await self.send(bytes_data="Hello world!")
        # await self.close(code=4123)

    async def disconnect(self, close_code):
        print("disconnected")

