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
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins Config
PLUGIN_PATHS = ["plugins", "plugins/pelican-plugins"]
PLUGINS = ["gallery", "thumbnailer"]

#Gallery Plugin
GALLERY_PATH = "images/gallery"

#Thumbnailer Plugin
IMAGE_PATH = "images/gallery"
THUMBNAIL_DIR = "images/thumbnails"
#THUMBNAIL_SIZES = [("200x?")]
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True
