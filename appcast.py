#!/usr/bin/env python

import polish_config
from releases import get_releases


def main():
    releases_xml = ''
    releases = get_releases(polish_config.release_info_dir)

    config_dict = {}
    for attr in (a for a in dir(polish_config) if not a.startswith('_')):
        config_dict[attr] = getattr(polish_config, attr)

    for release in releases:
        infodict = {}
        for attr in ('version', 'date', 'size', 'signature', 'filename'):
            infodict[attr] = getattr(release, attr)
        infodict.update(config_dict)
        releases_xml += release_xml % infodict

    config_dict['releases'] = releases_xml
    xml = appcast_xml % config_dict

    print xml.encode('utf-8')

appcast_xml = '''<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle"  xmlns:dc="http://purl.org/dc/elements/1.1/">
    <channel>
        <title>%(appcast_title)s</title>
        <link>%(appcast_url)s</link>
        <description>%(appcast_description)s</description>
        <language>%(language)s</language>

        %(releases)s
    </channel>
</rss>'''

release_xml = '''
        <item>
            <title>Version %(version)s</title>
            <sparkle:releaseNotesLink>%(release_notes)s?version=%(version)s</sparkle:releaseNotesLink>
            <pubDate>%(date)s</pubDate>
            <enclosure
                url="%(release_url)s/%(filename)s"
                sparkle:version="%(version)s"
                type="application/octet-stream"
                length="%(size)s"
                sparkle:dsaSignature="%(signature)s"
                />
        </item>'''

if __name__ == '__main__':
    main()
