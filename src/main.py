import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Gio, Adw

from .main_window import MainWindow


class ForgeApplication(Adw.Application):
    def __init__(self) -> None:
        super().__init__(
            application_id="com.crosine.Forge", flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        self.add_default_actions()

    def add_default_actions(self):
        self.create_action("quit", self._quit, ["<primary>q"])

    def _quit(self, *__args):
        self.quit()

    def do_activate(self):
        win: Gtk.Window = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def create_action(self: str, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """Application entry point."""
    app = ForgeApplication()
    return app.run(sys.argv)
