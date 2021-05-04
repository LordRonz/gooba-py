import argparse
from utils.earrapist import earrapist

def get_args():
    earrapist_help = '\n'.join(f'{i + 1}: {s}' for i, s in enumerate(earrapist))

    parser = argparse.ArgumentParser(description='Earrape spam', formatter_class=argparse.RawTextHelpFormatter)

    parg = parser.add_argument
    parg('-r', action='store_true', help='Rythm')
    parg('-g', action='store_true', help='Groovy')
    parg('-f', action='store_true', help='Fredboat')
    parg('-o', action='store_true', help='Octave')
    parg('-y', action='store_true', help='Hydra')
    parg('-v', action='store_true', help='Vexera')
    parg('-t', action='store_true', help='24/7')
    parg('-s', default=1, type=int, choices=range(1, len(earrapist) + 1),help=earrapist_help
    )

    parsed = vars(parser.parse_args())
    parsed['s'] = earrapist[parsed['s'] - 1]
    
    return parsed
