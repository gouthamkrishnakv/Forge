# Forge: IMAP Session

import imapclient
import logging

IMAP4_SSL_PORT = 993


class Session:
    __logger = logging.getLogger("Imap.Session")

    host: str
    port: int | None
    username: str
    password: str
    # TODO: Add OAuth2 Token also
    connection: imapclient.IMAP4_TLS | None

    def __init__(
        self, username: str, password: str, host: str, port: int | None = None
    ) -> None:
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        # Set as none, change later
        self.connection = None

    def connect(self):
        """This connects to a client session and then sends back a success/failure"""
        if self.port is not None:
            self.connection = imapclient.IMAP4_TLS(
                self.host,
                self.port,
                ssl_context=imapclient.ssl.create_default_context(),
            )
        else:
            self.connection = imapclient.IMAP4_TLS(
                self.host, IMAP4_SSL_PORT, ssl_context=imapclient.ssl.create_default_context()
            )
        self.__logger.info("Connection initialized")
        return self

    def login(self):
        if self.connection is not None:
            self.connection.login(self.username, self.password)
        self.__logger.info("Logged in with ({}, {})".format(self.username, "****"))
        return self

    def search(self):
        if self.connection is not None:
            result, data = self.connection.search(None, "ALL")
            self.__logger.info(f"{result} , {data}")
            return result, data
        return None

    def fetch(self, folder: str | None = None):
        if self.connection is not None:
            if folder is None:
                folder = "INBOX"
            self.connection.select(folder)
            self.connection.fetch("1", "(RFC822)")

    def check(self, folder: str | None = None) -> tuple[str, list[bytes | None]] | None:
        if self.connection is not None:
            if folder is None:
                folder = "INBOX"
            status, data = self.connection.select(folder)
            if status == "OK":
                self.__logger.info(f"{status} , {data}")
            else:
                self.__logger.error(f"ERR: {status} , {data}")
            return status, data
        return None

    def logout(self):
        if self.connection is not None:
            self.connection.logout()
        return self

