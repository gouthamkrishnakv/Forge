# Forge: IMAP Session

import imaplib
import imapclient
import logging

IMAP4_SSL_PORT = 993


class Session:
    __logger = logging.getLogger("Imap.Session")

    host: str
    port: str | None
    username: str
    password: str
    # TODO: Add OAuth2 Token also
    connection: imapclient.IMAP4_TLS

    def __init__(
        self, username: str, password, host: str, port: int | None = None
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
        self.connection.login(self.username, self.password)
        self.__logger.info("Logged in with ({}, {})".format(self.username, "****"))
        return self
