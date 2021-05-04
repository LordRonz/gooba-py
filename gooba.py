def main():
    from time import sleep
    from utils.wowee import groovy, rythm, fredboat, octave, hydra, vexera, _247
    from utils.argparser import get_args

    parsed = get_args()
    s = parsed['s']

    executeee = {
        'g': groovy,
        'r': rythm,
        'f': fredboat,
        'o': octave,
        'y': hydra,
        'v': vexera,
        't': _247,
    }

    def gg():
        sleep(3)
        for c, func in executeee.items():
            if parsed[c]:
                func(s)
                sleep(0.3)

    gg()

if __name__ == '__main__':
    main()
