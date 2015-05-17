# -*- coding: utf-8 -*-
import json
import math
from config import constants

from dao import article as article_dao
from model.article import Article
from model.page import Page

__author__ = 'wuyongxing'


def get_all_article_type():
    types = list(article_dao.get_all_article_type())
    for t in types:
        t['num'] = article_dao.get_article_count_by_type(str(t['_id']))
    return types


def handle_article_type(operate, _id, type):
    if operate == 'add':
        article_dao.add_article_type(str(type))
    elif operate == 'update':
        article_dao.update_article_type(str(_id), str(type))
    elif operate == 'delete':
        article_dao.delete_article_type(str(_id))


def check_article(_id, type, title):
    _id = str(_id)
    type = str(type)
    title = str(title)

    if len(_id) != 0 and not article_dao.exist_article_by_id(_id):
        return json.dumps({
            'error': 1,
            'message': '文章不存在'
        })

    if len(title) == 0:
        return json.dumps({
            'error': 1,
            'message': '标题不能为空'
        })

    if article_dao.exist_article_by_title(title) and title != article_dao.get_article_title(_id):
        return json.dumps({
            'error': 1,
            'message': '文章已经存在'
        })

    if not article_dao.exist_article_type(type):
        return json.dumps({
            'error': 1,
            'message': '文章类型不存在'
        })

    return json.dumps({
        'error': 0,
        'message': 'success'
    })


def add_or_update_article(model):
    check_result = json.loads(check_article(model._id, model.type, model.title))

    if check_result['error'] != 0:
        return

    model.change()

    if model.is_new():
        article_dao.add_article(model)
    else:
        article_dao.update_article(model)


def exist_article_by_title(title):
    if title == '':
        return True
    else:
        return article_dao.exist_article_by_title(title)


def get_article(title):
    model = Article()
    if title != '':
        art = article_dao.get_article_by_title(str(title))
        if art:
            model._id = art['_id']
            model.title = art['title']
            model.tag = art['tag']
            model.time = art['time']
            model.content = art['content']
            model.description = art['description']
            model.visit_count = art['visit_count']
            tt = article_dao.get_article_type_by_id(art['type'])
            if tt:
                model.type = tt['_id']
                model.type_name = tt['type']

    return model


def increase_visit_count(_id):
    article_dao.increase_visit_count(str(_id))


def get_article_title(_id):
    return article_dao.get_article_title(str(_id))


def get_latest_article():
    result = list(article_dao.get_latest_article(constants.item_limit))
    latest_articles = []
    for art in result:
        model = Article()
        model._id = art['_id']
        model.title = art['title']
        model.tag = art['tag']
        model.time = art['time']
        model.content = art['content']
        model.description = art['description']
        model.visit_count = art['visit_count']
        tt = article_dao.get_article_type_by_id(art['type'])
        if tt:
            model.type = tt['_id']
            model.type_name = tt['type']

        latest_articles.append(model)

    return latest_articles


def get_article_list(index, type=''):
    try:
        index = int(index)
    except ValueError:
        index = 1
    type = str(type)

    query = {}
    if type != '' and type != 'all':
        tt = article_dao.get_article_type_by_name(str(type))
        if tt:
            query = {'type': str(tt['_id'])}
        else:
            return [], Page()

    item_limit = constants.item_limit * constants.item_limit_rate
    total_count = article_dao.get_article_count(query)
    page_count = int(math.ceil(total_count * 1.0 / item_limit))

    if index > page_count or index < 1:
        offset = 0
        index = 1
    else:
        offset = (index - 1) * item_limit

    page = Page()
    page.index = index
    page.count = constants.page_count if page_count > constants.page_count else page_count

    if page.index <= page.count / 2:
        page.start = 1
    else:
        page.start = page.index - int(page.count / 2)
        if page.start > page_count - page.count:
            page.start = page_count - page.count + 1

    result = list(article_dao.get_article_list(offset, item_limit, query))

    article_list = []
    for art in result:
        model = Article()
        model._id = art['_id']
        model.title = art['title']
        model.tag = art['tag']
        model.time = art['time']
        model.content = art['content']
        model.description = art['description']
        model.visit_count = art['visit_count']
        tt = article_dao.get_article_type_by_id(art['type'])
        if tt:
            model.type = tt['_id']
            model.type_name = tt['type']

        article_list.append(model)
    return article_list, page

def delete_article(_id):
    article_dao.delete_article(str(_id))