#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Dobryden'
SITENAME = u'My Attempt at the Internet'
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
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins Config
PLUGIN_PATHS = ["plugins", "plugins/pelican-plugins"]
PLUGINS = ["photos"]

#Photos Plugin
PHOTO_LIBRARY = "images/gallery"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = ( 760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_RESIZE_JOBS = 4
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = 'Lee Dobryden'
#PHOTO_WATERMARK_IMG = ''

#Theme Vars
USE_LESS = True
