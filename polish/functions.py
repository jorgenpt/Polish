#!/usr/bin/env python

import os
import config

def template(file, *args, **kwargs):
    if len(args) == 1:
        vars = args[0]
    else:
        vars = {}
        for arg in args:
            vars.update(arg)
    vars.update(kwargs)
    return open('%s.tpl' % os.path.join(config.template_dir, file), 'r').read() % vars
