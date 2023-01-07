from logging import error
import logging
import gi

try:
    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")

    from gi.repository import Gtk, Adw
except ImportError or ValueError:
    error("Error: GObject dependencies not met.")

from .mail.client import MailClient


@Gtk.Template(resource_path="/com/crosine/Forge/UI/main_window.ui")
class MainWindow(Adw.ApplicationWindow):
    _logger = logging.getLogger("main.MainWindow")
    __gtype_name__ = "MainWindow"

    sidebar_toggle = Gtk.Template.Child()
    flap = Gtk.Template.Child()
    client_load_spinner = Gtk.Template.Child()

    # -- Constructors

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Sets up all default actions
        self._add_default_actions()
        # Sets up all default signals
        self._add_default_signals()
        # Sets up application
        self._setup()

    # Signal bound methods

    def on_close(self, *_args, **_kwargs):
        """
        This method is run when an application is closed.
        """
        self.clthread.stop()

    # Setup methods

    def _add_default_signals(self):
        """
        Adding default signals for the application
        """
        # self.sidebar_toggle.connect("toggled", lambda _: self.clthread.stop_ev.set())
        self.sidebar_toggle.connect("toggled", lambda _: print("Sidebar toggled"))
        self.connect("close-request", self.on_close)
        self._logger.info("Default signals set.")

    def _add_default_actions(self):
        """
        Add default actions for the window
        """
        self._logger.info("Default actions set")

    def load_complete(self):
        self.client_load_spinner.stop()

    def _setup(self):
        self.clthread = MailClient(self.load_complete)
        self.clthread.start()
