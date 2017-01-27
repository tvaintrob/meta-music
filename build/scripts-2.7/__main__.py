#!/Users/talvintrob/Projects/meta_music/bin/python

import os
from cli import parser
from __init__ import MusicFile

ACOUSTID_API_KEY = 'cSpUJKpD'


if __name__ == '__main__':
    args = parser.parse_args()

    if args.current_dir:
        files = [x for x in os.listdir(os.getcwd()) if x.endswith('.mp3')]
    else:
        files = args.files

    for file in files:
        print "[META] Proccesing file: %s..." % file
        mf = MusicFile(file)
        mf.lookup(ACOUSTID_API_KEY)

        print "[META] Found details: %s - %s" % (mf.artist, mf.song_name)
        if not mf.album:
            print "[META] Could not find album for the song"

        print "[META] Copying to: %s" % args.out_dir
        mf.copy_to(args.out_dir)

        print "[META] Tagging mp3"
        mf.tag()

        print "[META] Done."
