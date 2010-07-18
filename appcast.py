#!/usr/bin/env python

import polish
from releases import get_releases


def main():
    configdict = {}
    for attr in (a for a in dir(polish.config) if not a.startswith('_')):
        configdict[attr] = getattr(polish.config, attr)

    items = ''
    releases = get_releases(polish.config.release_info_dir)
    for release in releases:
        infodict = {}
        for attr in ('version', 'date', 'size', 'signature', 'filename'):
            infodict[attr] = getattr(release, attr)
        items += polish.template('appcast_item', configdict, infodict)
    print polish.template('appcast', configdict, items=items).encode('utf-8')


if __name__ == '__main__':
    main()
