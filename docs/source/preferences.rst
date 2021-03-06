Preferences
===========

PyQSO user preferences are stored in a configuration file located at
``~/.pyqso.ini``, where ``~`` denotes the user's home directory.

General
-------

Under the ``General`` tab, the user can choose to show the toolbox (see
the `Toolbox <toolbox.html>`_ section) when PyQSO is started.

View
----

Not all the available fields have to be displayed in the logbook. The
user can choose to hide a subset of them by unchecking them in the
``View`` tab. PyQSO must be restarted in order for any changes to take
effect.

Records
-------

The records tab allows users to choose if the UTC timezone is used when autocompleting the date and time fields, and whether the band should be automatically determined from the frequency field. Default values for the Power and Mode fields can also be specified here.

Callsign lookup
~~~~~~~~~~~~~~~

The user can enter their login details to access the `qrz.com <http://qrz.com/>`_
database and perform callsign lookups. Note that these details are currently stored in plain text
(unencrypted) format.

If the ``Ignore callsign prefixes and/or suffixes`` box is checked, then PyQSO will perform the callsign lookup whilst ignoring all prefixes (i.e. anything before a preceding "/" in the callsign) and the suffixes "P", "M", "A", "PM", "MM", "AM", and "QRP". For example, if the callsign to be looked up is EA3/MYCALL/P, only MYCALL will be looked up. If you get 'Callsign not found' errors, try enabling this option.

Hamlib support
--------------

PyQSO features rudimentary support for the Hamlib library. The name and
path of the radio device connected to the user's computer can be
specified in the ``Hamlib`` tab of the preferences dialog. Upon adding a
new record to the log, PyQSO will use Hamlib to retrieve the current
frequency that the radio device is set to and automatically fill in the
Frequency field.
