# -*- coding: utf-8 -*-
from handler.base import BaseHandler
from service import article as article_service

__author__ = 'wuyongxing'


class ArticleDetailHandler(BaseHandler):

    def get(self, title):
        if not article_service.exist_article_by_title(title):
            self.redirect('/article/all/page/1')
            return

        model = article_service.get_article(title)
        article_service.increase_visit_count(model._id)

        self.render('article-detail', model=model)

class ArticleListHandler(BaseHandler):

    def get(self, type, index):
        article_list, page = article_service.get_article_list(index, type)
        self.render('article-list', article_list=article_list, page=page, type=type)