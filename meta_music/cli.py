import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files',
                    metavar='FILE',
                    type=str,
                    nargs='*',
                    help='files to query')
parser.add_argument('--current-dir',
                    dest='current_dir',
                    action='store_true',
                    help='Query all .mp3 files in the current directory')
parser.add_argument('-o',
                    dest='out_dir',
                    type=str,
                    help='output directory',
                    default='./tagged')
