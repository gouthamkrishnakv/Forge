#!/usr/bin/env python3

# Forge: Main
#
# Copyright (C) 2022 Goutham Krishna K V

import logging
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
        self.create_action("preferences", self._preferences, ["<primary>p"])

    def _quit(self, **kwargs):
        self.quit()

    def _preferences(self, **kwargs):
        print("Preferences clicked")

    def create_action(self, name: str, callback, shortcuts=None, parent="app"):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"{parent}.{name}", shortcuts)

    def do_activate(self):
        win: Gtk.Window = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()


def main(version):
    """Application entry point."""
    logging.basicConfig(format="%(levelname)s: %(name)s\t:%(message)s",level=logging.DEBUG)
    app = ForgeApplication()
    return app.run(sys.argv)
