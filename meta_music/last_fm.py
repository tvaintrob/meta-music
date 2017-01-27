import requests
from errors import LastFMError

LAST_FM_API_KEY = '666e49df4b20c4c71bcdda54207b46e2'
LAST_FM_API_URL = 'http://ws.audioscrobbler.com/2.0/'


def get_track_info(track_name, artist):
    last_fm_request = requests.get(LAST_FM_API_URL, params={
        'method': 'track.getInfo',
        'api_key': LAST_FM_API_KEY,
        'artist': artist,
        'track': track_name,
        'format': 'json'
    })

    if last_fm_request.status_code == 200:
        return last_fm_request.json()['track']
    else:
        raise LastFMError()


def get_album_name(track_info):
    if 'album' in track_info:
        return track_info['album']['title']
    else:
        return ''


def get_album_artwork(track_info):
    if 'album' in track_info:
        art_url = [x['#text'] for x in track_info['album']['image']
                   if x['size'] == 'extralarge'][0]
        art_req = requests.get(art_url)

        if art_req.status_code == 200:
            return art_req.content
    else:
        return ''
