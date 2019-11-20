#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ricky White'
SITENAME = 'Ricky White — Developer'
SITEURL = ''

OUTPUT_PATH = 'output/'

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'theme/'
THEME_STATIC_DIR = 'static'

STATIC_PATHS = ['imgs', 'js', 'css', 'extra/robots.txt', 'blog/images']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Articles
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}/'

# Pages
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}/'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    "format": 'xml',
    'exclude': ['tag/', 'category/'],
}