# -*- coding: utf-8 -*-

# This file is part of 'hamster-gtk'.
#
# 'hamster-gtk' is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# 'hamster-gtk' is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 'hamster-gtk'.  If not, see <http://www.gnu.org/licenses/>.

"""This module provides file chooser widget."""

# [FIXME]
# Adding 'unicode_literals' raises encoding issues. This is a major sign we
# have a unicode issue!
from __future__ import absolute_import

from gettext import gettext as _

from gi.repository import Gtk
from six import text_type

from .config_widget import ConfigWidget


class EditableFileChooser(Gtk.Grid, ConfigWidget):
    """A file chooser that also has an entry for changing the path."""

    # Required else you would need to specify the full module
    # name in ui file
    __gtype_name__ = 'EditableFileChooser'

    def __init__(self):
        """Initialize widget."""
        super(Gtk.Grid, self).__init__()

        self.entry = Gtk.Entry()
        self.entry.set_hexpand(True)

        self.button = Gtk.Button(_("Choose"))
        self.button.connect('clicked', self.on_choose_clicked)

        self.attach(self.entry, 0, 0, 1, 1)
        self.attach(self.button, 1, 0, 1, 1)
        self.connect('mnemonic-activate', self.on_mnemonic_activate)

    def get_config_value(self):
        """Return value of the entry."""
        return self.entry.get_text()

    def set_config_value(self, value):
        """Set value of the entry."""
        self.entry.set_text(text_type(value))

    def on_choose_clicked(self, widget):
        """Open a dialog to select path and update entry widget with it."""
        # Reliably determine parent window
        # https://developer.gnome.org/gtk3/unstable/GtkWidget.html#gtk-widget-get-toplevel
        toplevel = self.get_toplevel()
        if not toplevel.is_toplevel():
            toplevel = None

        dialog = Gtk.FileChooserDialog(_("Please choose a directory"), toplevel,
            Gtk.FileChooserAction.SAVE, (_("_Cancel"), Gtk.ResponseType.CANCEL,
                                         _("_Save"), Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.entry.set_text(text_type(dialog.get_filename()))

        dialog.destroy()

    def on_mnemonic_activate(self, widget, group_cycling):
        """Mnemonic associated with this widget was activated."""
        return self.entry.do_mnemonic_activate(self.entry, group_cycling)
