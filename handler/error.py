# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'wuyongxing'

class ErrorHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('error')