# -*- coding: utf-8 -*-

from tornado.web import authenticated
from handler.admin import SystemHandler
from handler.base import BaseHandler
from service import attach as attach_service

__author__ = 'wuyongxing'


class AttachUploadHandler(SystemHandler):
    @authenticated
    def post(self, *args, **kwargs):
        type = self.get_argument('dir', '')
        files = self.request.files

        json_str = attach_service.upload_image(type, files)

        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json_str)


class AttachManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        type = self.get_argument('dir', '')
        path = self.get_argument('path', '')
        order = self.get_argument('order', '')  # 排序

        json_str = attach_service.image_list(type, path, order)

        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json_str)

