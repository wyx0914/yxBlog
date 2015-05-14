# -*- coding: utf-8 -*-
from pymongo import MongoClient

__author__ = 'wuyongxing'


def get_connection():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    return client['yxBlog']