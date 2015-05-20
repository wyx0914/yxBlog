# -*- coding: utf-8 -*-

import hashlib
from random import Random
from dao import admin as admin_dao

__author__ = 'wuyongxing'


def create_random_str(random_length=6):
    random_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        random_str += chars[random.randint(0, length)]
    return random_str


def login(account, password, random_str):
    admin = admin_dao.get_password_md5(str(account))

    if admin is None:
        return False
    password_md5 = admin['password'].lower() + random_str

    password_md5 = hashlib.md5(password_md5.encode('utf-8')).hexdigest()

    return str(password) == str(password_md5)

