import eyed3


def tag(filename, info):
    audio_file = eyed3.load(filename)
    audio_file.tag.artist = info['artist']

    if 'album' in info:
        audio_file.tag.album = info['album']

    audio_file.tag.album_artist = info['artist']
    audio_file.tag.title = info['track']

    if 'image' in info:
        audio_file.tag.images.set(3, info['image'], 'image/png', u'image')
    audio_file.tag.save()
