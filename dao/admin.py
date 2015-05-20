# -*- coding: utf-8 -*-
from dao import db

__author__ = 'wuyongxing'

table_admin = db.get_connection().admin


def get_password_md5(account):
    return table_admin.find_one({
        'account': account,
    })