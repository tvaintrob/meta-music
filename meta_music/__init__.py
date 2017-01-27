import last_fm
import acoustid
import shutil
import os
import tag_mp3


class MusicFile(object):
    def __init__(self, filename):
        self.filename = filename

    def lookup(self, acoustid_api_key):
        _, _, track, artist = \
            acoustid.match(acoustid_api_key, self.filename).next()
        self.song_name = track
        self.artist = artist.replace(';', ' ft.')

        t_info = last_fm.get_track_info(track, artist)
        self.album = last_fm.get_album_name(t_info)
        self.album_art = last_fm.get_album_artwork(t_info)

    def copy_to(self, dest_dir):
        new_path = os.path.join(dest_dir, '%s - %s.mp3' % (self.artist,
                                                           self.song_name))
        self.new_path = new_path

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        shutil.copyfile(self.filename, new_path)

    def tag(self):
        info = {
            'artist': self.artist,
            'track': self.song_name
        }

        if self.album:
            info['album'] = self.album
            info['image'] = self.album_art
        tag_mp3.tag(self.new_path, info)
