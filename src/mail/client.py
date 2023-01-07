import threading
# import imapclient
import logging
import asyncio
from typing import List

from .imap.session import Session

USERNAME = "imaptest.fluent@outlook.com"
PASSWORD = "ClarifyMyTest200"
HOST = "outlook.office365.com"

class MailClient(threading.Thread):
    # Logging
    _logger = logging.getLogger("client.MailClient")
    # Event
    loop: asyncio.AbstractEventLoop
    sessions: List[Session]

    def __init__(self, load_complete):
        threading.Thread.__init__(self)
        self.load_complete = load_complete
        self.loop = asyncio.get_event_loop()
        self.sessions: List[Session] = []

    async def __setup(self):
        self._logger.info("SETTING UP (FAKE)")
        # await asyncio.sleep(5)
        new_client = Session(USERNAME, PASSWORD, HOST)
        new_client.connect()
        new_client.login()
        self.sessions.append(new_client)
        self.load_complete()
        self._logger.info("LOADING COMPLETE")

    def run(self):
        self.loop.create_task(self.__setup())
        self.loop.run_forever()

    async def logout_all_sessions(self):
        async for session in self.sessions:
            session.connection.logout()


    def stop(self):
        # When stop method is run, stop the asyncio loop
        self.loop.call_soon_threadsafe(self.logout_all_sessions)
        self.loop.call_soon_threadsafe(self.loop.stop)
        self._logger.info("STOPPED")
