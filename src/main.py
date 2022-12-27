import sys
import gi
import json

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from .main_window import MainWindow

from gi.repository import Gtk, Gio, Adw

class TempestApplication(Adw.Application):
    def __init__(self) -> None:
        super().__init__(
            application_id="com.crosine.Forge",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )

    def do_activate(self):
        win: Gtk.Window = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()


def main(version):
    """Application entry point."""
    app = TempestApplication()
    return app.run(sys.argv)
