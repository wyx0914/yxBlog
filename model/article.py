# -*- coding: utf-8 -*-
import json
import time

__author__ = 'wuyongxing'


class Article(object):
    def __init__(self):
        self._id = ''
        self.title = ''
        self.type = ''
        self.tag = ''
        self.description = ''
        self.content = ''
        self.time = time.time()
        self.visit_count = 0

        self.type_name = ''

    def change(self):
        self._id = str(self._id)
        self.title = str(self.title)
        self.type = str(self.type)
        self.tag = str(self.tag)
        self.description = str(self.description)
        self.content = str(self.content)

    def is_new(self):
        return len(str(self._id)) == 0
