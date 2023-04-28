import threading
import logging
from collections.abc import Callable
from typing import List

from .imap.session import Session

USERNAME = "imaptest.fluent@outlook.com"
PASSWORD = "ClarifyMyTest200"
HOST = "outlook.office365.com"

class MailClient(threading.Thread):
    # Logging
    _logger = logging.getLogger("client.MailClient")
    # Event
    stop_ev: threading.Event
    load_complete: Callable[[], None]
    sessions: List[Session]

    def __init__(self, load_complete: Callable[[], None]):
        threading.Thread.__init__(self)
        self.stop_ev = threading.Event()
        self.load_complete = load_complete
        self.sessions = []

    def __setup(self):
        self._logger.info("SETTING UP (FAKE)")
        # await asyncio.sleep(5)
        new_client = Session(USERNAME, PASSWORD, HOST)
        new_client.connect()
        new_client.login()
        new_client.check()
        new_client.search()
        new_client.fetch()
        self.sessions.append(new_client)
        session_index = len(self.sessions)
        self.load_complete()
        self._logger.info("LOADING COMPLETE")
        return session_index

    def setup(self):
        session_index = self.__setup()
        return session_index


    def run(self):
        """This methods starts/runs the thread."""
        self.__setup()
        self.stop_ev.wait()

    def close_connections(self):
        for session_to_close in self.sessions:
            session_to_close.logout()

    def stop(self):
        # When stop method is run, stop the asyncio loop
        self.close_connections()
        self.stop_ev.set()
        self._logger.info("STOPPED")
