# -*- coding: utf-8 -*-
from bson import ObjectId
from dao import db

__author__ = 'wuyongxing'

table_friend_link = db.get_connection().friend_link


def get_all():
    return table_friend_link.find()


def add(text, link):
    table_friend_link.insert({
        'text': text,
        'link': link
    })


def update(_id, text, link):
    try:
        table_friend_link.update({'_id': ObjectId(_id)}, {
            '$set': {
                'text': text,
                'link': link
            }
        })
    except:
        pass


def delete(_id):
    try:
        table_friend_link.remove({'_id': ObjectId(_id)})
    except:
        pass