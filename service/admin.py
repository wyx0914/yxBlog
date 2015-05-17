# -*- coding: utf-8 -*-

from dao import admin as admin_dao

__author__ = 'wuyongxing'


def login(account, password):
    return admin_dao.login(str(account), str(password).upper())

