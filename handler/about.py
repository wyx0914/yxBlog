# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'wuyongxing'


class AboutHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('about')