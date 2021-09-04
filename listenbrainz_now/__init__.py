from functools import partial
import json
from pynicotine.pluginsystem import returncode

from .base import BasePlugin
from .utils import command, get


class Plugin(BasePlugin):
    settings = {
        'username': '',
        'command': '/me is now Playing: {artist} - {title}'
    }
    metasettings = {
        'username': {
            'description': 'Listenbrainz Username',
            'type': 'string',
        },
        'command': {
            'description': '''Now playing message format
Placeholders: {artist}, {album}, {title}''',
            'type': 'string',
        },
    }

    @command
    def listen_now(self, initiator, public=True):
        username = self.settings['username']
        echo = self.echo_public if public else self.echo_private
        if not username:
            echo(initiator, 'No username defined', 'action')
            return returncode['zap']

        try:
            with get(f'https://api.listenbrainz.org/1/user/{username}/playing-now') as resp:
                data = resp.json['payload']
        except Exception as e:
            echo(initiator, f'Could not get now-playing data: {e}', 'action')
            return returncode['zap']

        if data['playing_now'] and (track := data['listens'][0]['track_metadata']):
            msg = self.settings['command'].format(artist=track['artist_name'],
                                                  album=track['release_name'],
                                                  title=track['track_name'])
            func = self.send_public if public else self.send_private
            func(initiator, msg)
        else:
            echo(initiator, 'Nothing is playing', 'action')
        return returncode['zap']

    __publiccommands__ = [('', partial(listen_now, public=True))]
    __privatecommands__ = [('', partial(listen_now, public=False))]
