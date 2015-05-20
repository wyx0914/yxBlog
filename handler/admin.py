# -*- coding: utf-8 -*-
import time
from os import path
from tornado.web import authenticated, RequestHandler
from config import constants
from model.article import Article
from service import admin as admin_service
from service import friend as friend_service
from service import article as article_service
from config.constants import settings

__author__ = 'wuyongxing'


class SystemHandler(RequestHandler):
    def initialize(self):
        self.error_uri = '/error/404'

    def get(self, *args, **kwargs):
        self.redirect(self.error_uri)

    def post(self, *args, **kwargs):
        self.redirect(self.error_uri)

    def render(self, template_name, **kwargs):
        RequestHandler.render(self, path.join(settings['template_path'], '%s.html' % template_name), **kwargs)

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        if user is not None and user != '':
            self.set_secure_cookie('user', user, expires=time.time() + constants.cookies_expires)
        else:
            user = None
        return user

    def get_login_url(self):
        return constants.settings['login_url']


class LoginHandler(SystemHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument('next', '/system/article/list/1')
        if self.get_current_user():
            self.redirect(next)
            return

        random_str = admin_service.create_random_str()
        self.set_secure_cookie('random', random_str, expires=time.time() + constants.cookies_expires)

        self.render('login', next=next, random_str=random_str)

    def post(self, *args, **kwargs):
        next = self.get_argument('next', '/system/article/list/1')
        account = self.get_argument('account', '')
        password = self.get_argument('password', '')
        random_str = self.get_secure_cookie('random')

        flag = admin_service.login(account, password, random_str)
        if flag:
            self.set_secure_cookie('user', account, expires=time.time() + constants.cookies_expires)
            self.redirect(next)
        else:
            self.redirect('/system/login')


class LogoutHandler(SystemHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.set_secure_cookie('user', '', expires=10)
        self.redirect('/system/login')


class FriendLinkHandler(SystemHandler):
    @authenticated
    def get(self, *args, **kwargs):
        links = friend_service.get_all_friend_link()
        self.render('system-friend-link-list', links=links)

    @authenticated
    def post(self, operate):
        _id = self.get_argument('_id', '')
        text = self.get_argument('text', '')
        link = self.get_argument('link', '')

        friend_service.handle_friend(operate, _id, text, link)
        self.redirect('/system/friend')


class ArticleTypeHandler(SystemHandler):
    @authenticated
    def get(self, *args, **kwargs):
        types = article_service.get_all_article_type()
        self.render('system-article-type-list', types=types)

    @authenticated
    def post(self, operate):
        _id = self.get_argument('_id', '')
        type = self.get_argument('type', '')

        article_service.handle_article_type(operate, _id, type)
        self.redirect('/system/article/type')


class ArticleListHandler(SystemHandler):
    @authenticated
    def get(self, index):
        article_list, page = article_service.get_article_list(index)
        self.render('system-article-list', article_list=article_list, page=page)

    @authenticated
    def post(self):
        _id = self.get_argument('_id', '')

        article_service.delete_article(_id)

        self.redirect('/system/article/list/1')


class ArticleHandler(SystemHandler):
    @authenticated
    def get(self, title=''):
        types = article_service.get_all_article_type()

        if not article_service.exist_article_by_title(title):
            self.redirect('/system/article/list/1')
            return

        model = article_service.get_article(title)

        self.render('system-article-detail', types=types, model=model)

    @authenticated
    def post(self, title=''):
        art = Article()
        art._id = self.get_argument('_id', '')
        art.title = self.get_argument('title', '')
        art.type = self.get_argument('type', '')
        art.tag = self.get_argument('tag', '')
        art.description = self.get_argument('description', '')
        art.content = self.get_argument('content', '')

        article_service.add_or_update_article(art)

        self.redirect('/system/article/list/1')


class ArticleCheckHandler(SystemHandler):
    @authenticated
    def post(self, *args, **kwargs):
        _id = self.get_argument('_id', '')
        type = self.get_argument('type', '')
        title = self.get_argument('title', '')

        json_str = article_service.check_article(_id, type, title)

        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json_str)