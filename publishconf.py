#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://gtia.com'
SITENAME = 'Atari 8-bits forever'
RELATIVE_URLS = False

AUTHOR = 'gozar'
DEFAULT_DATE = 'fs'
THEME = 'theme/pelican-bootstrap3'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = [
            'extra/CNAME',
                ]
EXTRA_PATH_METADATA = {
            'extra/CNAME': {'path': 'CNAME'},
                }

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
