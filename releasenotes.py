#!/usr/bin/env python

import polish
from releases import get_releases


def main():
    releases_html = ''
    releases = get_releases(polish.config.release_info_dir)

    configdict = {}
    for attr in (a for a in dir(polish.config) if not a.startswith('_')):
        configdict[attr] = getattr(polish.config, attr)

    for release in releases:
        infodict = {}
        for attr in ('version', 'date', 'size', 'signature', 'filename'):
            infodict[attr] = getattr(release, attr)

        sections_html = ''
        for (section, changes) in release.changelog.items():
            changes_html = ''
            for change in changes:
                changes_html += '<li>%s</li>\n' % change
            sections_html = polish.template('releasenotes_section', configdict, infodict, section=section.capitalize(), changes=changes_html})
        releases_html += polish.template('releasenotes_release', configdict, infodict, sections=sections_html)

    configdict['releases'] = releases_html
    html = polish.templates('releasenotes', configdict, releases=releases_html)

    print html.encode('utf-8')

if __name__ == '__main__':
    main()
