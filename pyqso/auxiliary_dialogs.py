#!/usr/bin/env python 

#    Copyright (C) 2013 Christian T. Jacobs.

#    This file is part of PyQSO.

#    PyQSO is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyQSO is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyQSO.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
import logging

def error(parent, message):
   """ Display an error message. """
   logging.error(message)
   _handle_gtk_dialog(parent, Gtk.MessageType.ERROR, message, "Error")

def info(parent, message):
   """ Display some information. """
   logging.debug(message)
   _handle_gtk_dialog(parent, Gtk.MessageType.INFO, message, "Information")
   
def question(parent, message):
   """ Ask the user a question. The dialog comes with 'Yes' and 'No' response buttons. """
   return _handle_gtk_dialog(parent, Gtk.MessageType.QUESTION, message, "Question")

def _handle_gtk_dialog(parent, msgtype, message, title):
   bt = Gtk.ButtonsType
   buttons = bt.YES_NO if msgtype == Gtk.MessageType.QUESTION else bt.OK
   dialog = Gtk.MessageDialog(parent, Gtk.DialogFlags.DESTROY_WITH_PARENT,
         msgtype, buttons, message, title=title)
   response = dialog.run()
   dialog.destroy()
   return response
