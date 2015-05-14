# -*- coding: utf-8 -*-

from dao import friend as friend_dao

__author__ = 'wuyongxing'

def get_all_friend_link():
    return list(friend_dao.get_all())

def handle_friend(operate, _id, text, link):
    if operate == 'add':
        friend_dao.add(str(text), str(link))
    elif operate == 'update':
        friend_dao.update(str(_id), str(text), str(link))
    elif operate == 'delete':
        friend_dao.delete(str(_id))