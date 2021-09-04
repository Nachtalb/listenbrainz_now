Listenbrainz Now
============

A plugin for `Nicotine+`_.

Listenbrainz now playing integration


Installation
------------

Open Nicotine+ settings, go to *General > Plugins* and click *+ Add
Plugins*. After that download the latest `release`_ and extract it into
the plugins folder.

Remove the version from the folder name. The folder name must stay the
same across version upgrades otherwise you will loose any changed
settings.

Now you can enable the *Listenbrainz Now* plugin in the previously
opened plugin settings.


Commands
--------

- ``/lb`` Send currently playing song to chat
- ``/lb-update`` manually check for updates.
- ``/lb-reload`` reload the plugin.


Settings
--------

+-----------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Name                  | Function                                                                                | Default                                                              |
+=======================+=========================================================================================+======================================================================+
| Check for Updates     | Check for updates on start and periodically                                             | Enabled                                                              |
+-----------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Listenbrainz Username | Your Listenbrainz username                                                              | `''`                                                                 |
+-----------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Now playing message   | What to send to the chat when using ``/lb``                                             | `'/me is now Playing: {artist} - {title}'`                           |
|                       | Available placeholders: {artist}, {album} & {title}                                     |                                                                      |
+-----------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Append link           | Some listeners report the stream link to Listenbrainz. Show that link if available      | Enabled                                                              |
+-----------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+


Contributing
------------

Pull requests are welcome.


License
-------

`GNU GPL v3.0`_

.. _Nicotine+: https://nicotine-plus.github.io/nicotine-plus/
.. _release: https://github.com/Nachtalb/listenbrainz_now/releases
.. _GNU GPL v3.0: https://github.com/Nachtalb/listenbrainz_now/blob/master/LICENSE
