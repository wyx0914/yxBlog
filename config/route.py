# -*- coding: utf-8 -*-
from tornado.web import StaticFileHandler
from config.constants import settings
from handler import home, admin, about, guestbook, \
    attach, error, article

__author__ = 'wuyongxing'

handler_mapper = [
    (r'/', home.IndexHandler),
    (r'/guestbook', guestbook.GuestBookHandler),
    (r'/about', about.AboutHandler),
    (r'/system/login', admin.LoginHandler),
    (r'/system/logout', admin.LogoutHandler),
    (r'/system/friend', admin.FriendLinkHandler),
    (r'/system/friend/(delete|add|update)', admin.FriendLinkHandler),
    (r'/system/article/type', admin.ArticleTypeHandler),
    (r'/system/article/type/(delete|add|update)', admin.ArticleTypeHandler),
    (r'/system/article/list/([1-9][0-9]*)', admin.ArticleListHandler),
    (r'/system/article/delete', admin.ArticleListHandler),
    (r'/system/article/add', admin.ArticleHandler),
    (r'/system/article/(.+)/update', admin.ArticleHandler),
    (r'/system/article/check', admin.ArticleCheckHandler),

    (r'/attach/upload', attach.AttachUploadHandler),
    (r'/attachments', attach.AttachManageHandler),

    (r'/article/(.+)/page/([1-9][0-9]*)', article.ArticleListHandler),
    (r'/article/detail/(.+)', article.ArticleDetailHandler),

    (r'(.*)', error.ErrorHandler),
    (r'/static/(.+)', StaticFileHandler, dict(path=settings['static_path'])),
    (r'/favicon.ico', StaticFileHandler, dict(path=settings['static_path'])),
]