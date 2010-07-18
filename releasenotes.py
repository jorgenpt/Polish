#!/usr/bin/env python

import polish_config
from releases import get_releases


def main():
    releases_html = ''
    releases = get_releases(polish_config.release_info_dir)

    config_dict = {}
    for attr in (a for a in dir(polish_config) if not a.startswith('_')):
        config_dict[attr] = getattr(polish_config, attr)

    for release in releases:
        infodict = {}
        for attr in ('version', 'date', 'size', 'signature', 'filename'):
            infodict[attr] = getattr(release, attr)
        infodict.update(config_dict)

        sections_html = ''
        for (section, changes) in release.changelog.items():
            sectiondict = infodict.copy()
            sectiondict['section'] = section.capitalize()
            sectiondict['changes'] = ''
            for change in changes:
                sectiondict['changes'] += '<li>%s</li>\n' % change
            sections_html = section_html % sectiondict

        infodict['sections'] = sections_html
        releases_html += release_html % infodict

    config_dict['releases'] = releases_html
    html = releasenotes_html % config_dict

    print html.encode('utf-8')

releasenotes_html = '''<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <title>What's new in %(app_name)s?</title>
        <meta name="robots" content="anchors">
        <link href="updates.css" type="text/css" rel="stylesheet" media="all">
        <script src="updates.js" type="text/javascript"> </script>
    </head>

    <body>
%(releases)s
    </body>
</html>'''

release_html = '''<div class='version' id='%(version)s'>
        <h2>Changes in %(version)s</h2>
        %(sections)s
        </div>'''

section_html = '''<table class="dots" width="100%%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <td class="blue">
                    <h3>%(section)s</h3>
                </td>
            </tr>
            <tr>
                <td>
                    <ul>
%(changes)s                    </ul>
                </td>
            </tr>
        </table>
        <br />'''

if __name__ == '__main__':
    main()
