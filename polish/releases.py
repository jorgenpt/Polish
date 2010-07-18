from copy import deepcopy
import re
from operator import attrgetter
import os
import yaml
import polish_config

class Version(object):
    def __init__(self, version):
        if isinstance(version, basestring):
            self._array = [int(v) for v in version.split('.')]
        else:
            self._array = [int(v) for v in version]
        self._string = '.'.join([str(v) for v in self._array])

    def __lt__(self, other):
        return self._array <  other._array
    def __le__(self, other):
        return self._array <= other._array
    def __gt__(self, other):
        return self._array >  other._array
    def __ge__(self, other):
        return self._array >= other._array
    def __eq__(self, other):
        return self._array == other._array
    def __ne__(self, other):
        return self._array != other._array

    def __str__(self):
        return self._string
    def __repr__(self):
        return 'Version(%r)' % self._string

class Release(object):
    def __init__(self, file_or_obj):
        if isinstance(file_or_obj, basestring):
            fh = file(file_or_obj)
            filename = file_or_obj
        else:
            fh = file_or_obj
            filename = fh.name

        _, tail = os.path.split(filename)
        version, _ = os.path.splitext(tail)
        self._version = Version(version)
        self._info = yaml.load(fh)

    @property
    def version(self):
        return self._version

    @property
    def date(self):
        return self._info.get('date', '')

    @property
    def signature(self):
        return self._info['signature']

    @property
    def changelog(self):
        return deepcopy(self._info.get('changelog', {}))

    @property
    def filename(self):
        if 'filename' in self._info:
            return self._info['filename']
        return polish_config.release_name % self._version

    @property
    def path(self):
        if 'directory' in self._info:
            directory = self._info.get('directory', '')
        else:
            directory = polish_config.release_dir

        return os.path.join(directory, self.filename)

    @property
    def size(self):
        return os.path.getsize(self.path)

    @property
    def changelog(self):
        return self._info.get('changelog', {})

    def __repr__(self):
        return '<Release object, version = %r, info = %r>' % (self._version, self._info)

def get_releases(from_path):
    release_regex = re.compile(r'(\d+\.)+yaml$', re.I)
    releases = [Release(os.path.join(from_path, r)) for r in os.listdir(from_path) if release_regex.match(r)]
    releases.sort(key=attrgetter('version'), reverse=True)
    return releases
