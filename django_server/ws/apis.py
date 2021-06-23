from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio


class TestWS(AsyncWebsocketConsumer):
    groups = ["broadcast"]

    async def ws_timeout(self):
        await asyncio.sleep(30)
        print("closing connection after timeout")
        await self.close()           

    async def auto_send(self):
        i=0
        while i<10:
            await self.send(text_data=f"count {str(i)}")
            await asyncio.sleep(2)
            i+=1

    async def connect(self):
        await self.accept()
        # await self.accept("subprotocol")
        asyncio.ensure_future(self.auto_send())
        asyncio.ensure_future(self.ws_timeout())

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Received, "+text_data)
        # await self.send(bytes_data="Hello world!")
        # await self.close(code=4123)

    async def disconnect(self, close_code):
        print("disconnected")

