# -*- coding: utf-8 -*-
from os import path
from tornado.web import RequestHandler
from service import friend as friend_service
from service import article as article_service
__author__ = 'wuyongxing'

class BaseHandler(RequestHandler):

    def initialize(self):
        self.error_uri = '/error/404'

    def get(self, *args, **kwargs):
        self.redirect(self.error_uri)

    def post(self, *args, **kwargs):
        self.redirect(self.error_uri)

    def render(self, template_name, **kwargs):
        kwargs['links'] = friend_service.get_all_friend_link()
        kwargs['types'] = article_service.get_all_article_type()
        kwargs['latest_articles'] = article_service.get_latest_article()
        RequestHandler.render(self, path.join(self.get_template_path(), '%s.html' % template_name), **kwargs)

