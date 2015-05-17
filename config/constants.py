# -*- coding: utf-8 -*-
from os import path

__author__ = 'wuyongxing'


item_limit = 10

page_count = 10

item_limit_rate = 2

cookies_expires = 60 * 60 # 3600 s

home_dir = path.dirname(path.dirname(__file__))

upload_path = "static/attach/article/"

attach_path = path.join(home_dir, 'static/attach/')

settings = {
    'static_path': path.join(home_dir, 'static'),
    'template_path': path.join(home_dir, 'template'),
    'listen_port': 8080,
    "login_url": "/system/login",
    "xsrf_cookies": True,
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJBFuYh7EQnp2XdTP1o/Vo=",
}

