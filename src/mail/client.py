import threading
import imaplib
import logging

USERNAME = "imaptest.fluent@outlook.com"
PASSWORD = "ClarifyMyTest200"


class MailClient(threading.Thread):
    # Logging
    _logger = logging.getLogger("client.MailClient")
    # Event
    stop_ev: threading.Event

    def __init__(self, load_complete):
        threading.Thread.__init__(self)
        self.stop_ev = threading.Event()
        self.load_complete = load_complete

    def run(self):
        self._logger.info("Thread started")
        clnt = imaplib.IMAP4_SSL("outlook.office365.com")
        self._logger.info(clnt.login(USERNAME, PASSWORD))
        self._logger.info("LOGGED IN")
        self._logger.info(clnt.noop())
        self._logger.info(clnt.select(mailbox="INBOX", readonly=True))
        # self._logger.info(clnt.list(directory="INBOX/", pattern="*"))
        self._logger.info(clnt.status("INBOX", "MESSAGES"))
        # self._logger.info(clnt.search(None, "ALL", "HEADER", "SUBJECT", '"Microsoft"'))
        self._logger.info(clnt.fetch("Inbox (MESSAGES 1)", "HEADER SUBJECT BODY"))
        self.load_complete()
        while not self.stop_ev.wait(timeout=0.05):
            pass
        self._logger.info(clnt.logout())
        self._logger.info("LOGGED OUT")
        self._logger.info("Thread stopped")
