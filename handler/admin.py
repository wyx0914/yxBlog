# -*- coding: utf-8 -*-
import time
from os import path
from tornado.web import authenticated, RequestHandler
from config import constants
from bussiness import admin as admin_service
from bussiness import friend as friend_service
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
        if self.get_current_user():
            self.redirect('/system/article')
            return

        self.render('login')

    def post(self, *args, **kwargs):
        account = self.get_argument('account', '')
        password = self.get_argument('password', '')

        flag = admin_service.login(account, password)
        if flag:
            self.set_secure_cookie('user', account, expires=time.time() + constants.cookies_expires)
            self.redirect('/system/article')
        else:
            self.redirect('/system/login')


class LogoutHandler(SystemHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.set_secure_cookie('user', '', expires=10)
        self.redirect('/system/login')


class ArticleHandler(SystemHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.render('system-base')


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

