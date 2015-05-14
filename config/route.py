# -*- coding: utf-8 -*-
from tornado.web import StaticFileHandler
from config.constants import settings
from handler import home, admin, about, guestbook

__author__ = 'wuyongxing'


mapper = [
    (r'/', home.IndexHandler),
    (r'/guestbook', guestbook.GuestBookHandler),
    (r'/about', about.AboutHandler),
    (r'/system/login', admin.LoginHandler),
    (r'/system/logout', admin.LogoutHandler),
    (r'/system/article', admin.ArticleHandler),
    (r'/system/friend', admin.FriendLinkHandler),
    (r'/system/friend/(delete|add|update)', admin.FriendLinkHandler),
#    (r'.*', ErrorHandler),
    (r'/static/(.*)', StaticFileHandler, dict(path=settings['static_path'])),
    (r'/favicon.ico', StaticFileHandler, dict(path=settings['static_path'])),
]