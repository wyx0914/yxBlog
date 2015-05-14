# -*- coding: utf-8 -*-
from dao import db

__author__ = 'wuyongxing'

table_admin = db.get_connection().admin


def login(account, password):
    count = table_admin.find({
        'account': account,
        'password': password
    }).count()

    return count > 0