#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Dobryden'
SITENAME = u'leedobryden.com'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/lndobryden'),
            ('linkedin', 'https://www.linkedin.com/in/lee-dobryden-6aa62994'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins Config
PLUGIN_PATHS = ["plugins", "plugins/pelican-plugins"]
PLUGINS = ["photos"]

#Photos Plugin
PHOTO_LIBRARY = "images"
PHOTO_GALLERY = (1024, 768, 100)
PHOTO_ARTICLE = ( 760, 506, 80)
PHOTO_THUMB = (600, 1200, 80)
PHOTO_RESIZE_JOBS = 4
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = 'Lee Dobryden'
#PHOTO_WATERMARK_IMG = ''

#Theme Vars
USE_LESS = True

GOOGLE_ANALYTICS = "UA-103198821-1"

STATIC_PATHS = ['images',
    'static/keybase.txt',
    'static/.well-known'
    ]
EXTRA_PATH_METADATA = {
    'static/keybase.txt': {'path': 'keybase.txt'},
    'static/.well-known/*': {'path': '.well-known/*'},
    }
