# -*- coding: utf-8 -*-
from bson import ObjectId
from config import constants
from dao import db

__author__ = 'wuyongxing'

table_article_type = db.get_connection().article_type
table_article = db.get_connection().article


def get_article_type_by_id(_id):
    try:
        return table_article_type.find_one({'_id': ObjectId(_id)})
    except:
        return None


def get_article_type_by_name(name):
    return table_article_type.find_one({'type': name})


def get_all_article_type():
    return table_article_type.find()


def add_article_type(type):
    table_article_type.insert({
        'type': type
    })


def update_article_type(_id, type):
    try:
        table_article_type.update({'_id': ObjectId(_id)}, {
            '$set': {
                'type': type
            }
        })
    except:
        pass


def delete_article_type(_id):
    try:
        table_article_type.remove({'_id': ObjectId(_id)})
    except:
        pass


def exist_article_type(_id):
    try:
        result = table_article_type.find({'_id': ObjectId(_id)}).count() > 0
    except:
        result = False
    return result


def exist_article_by_id(_id):
    try:
        result = table_article.find({'_id': ObjectId(_id)}).count() > 0
    except:
        result = False
    return result


def exist_article_by_title(title):
    return table_article.find({'title': title}).count() > 0


def add_article(model):
    table_article.insert({
        'title': model.title,
        'type': model.type,
        'tag': model.tag,
        'description': model.description,
        'content': model.content,
        'time': model.time,
        'visit_count': 0
    })


def update_article(model):
    try:
        table_article.update({'_id': ObjectId(model._id)}, {
            '$set': {
                'title': model.title,
                'type': model.type,
                'tag': model.tag,
                'description': model.description,
                'content': model.content
            }
        })
    except:
        pass


def get_article_by_title(title):
    return table_article.find_one({
        'title': title
    })


def get_article_title(_id):
    try:
        title = table_article.find_one({'_id': ObjectId(_id)})['title']
    except:
        title = None
    return title


def increase_visit_count(_id):
    try:
        table_article.update({'_id': ObjectId(_id)}, {
            '$inc': {
                'visit_count': 1
            }
        })
    except:
        pass


def get_article_count_by_type(type_id):
    return table_article.find({"type": type_id}).count()


def get_latest_article(item_limit):
    return table_article.find().sort('time', -1).limit(item_limit)


def get_article_count(query={}):
    return table_article.find(query).count()


def get_article_list(offset, item_limit, query={}):
    return table_article.find(query).sort('time', -1).skip(offset).limit(item_limit)


def delete_article(_id):
    try:
        table_article.remove({'_id': ObjectId(_id)})
    except:
        pass