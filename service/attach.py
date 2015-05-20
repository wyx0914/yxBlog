# -*- coding: utf-8 -*-
import os
import json
import tempfile
import time
from os import path
from PIL import Image
from config import constants

__author__ = 'wuyongxing'

image_only = json.dumps({
    "error": 1,
    "message": "只接受图片"
})

path_error = json.dumps({
    "error": 1,
    "message": "路径出错"
})

image_types = ('gif', 'jpg', 'jpeg', 'png', 'bmp')

if not path.exists(constants.attach_path):
    os.mkdir(constants.attach_path)

upload_path = path.join(constants.home_dir, constants.upload_path)
if not path.exists(constants.upload_path):
        os.mkdir(upload_path)

def upload_image(type, files):
    if len(type) == 0 or type != 'image':
        return image_only

    if files and len(files['imgFile']) > 0:
        f = files['imgFile'][0]
        filename = f['filename']

        uri = constants.upload_path + str(int(time.time())) + '.' + filename.split('.').pop()

        dstPath = path.join(constants.home_dir, uri)

        if len(f['body']) > (1 << 22):
            return image_only

        tmp = tempfile.NamedTemporaryFile(delete=True)
        tmp.write(f['body'])
        tmp.seek(0)

        try:
            img = Image.open(tmp.name)
        except IOError:
            tmp.close()
            return image_only
        if img:
            img.save(dstPath)
        tmp.close()

    url = "/" + uri

    return json.dumps({
        "error": 0,
        "url": url
    })


def image_list(type, _path, order):  # order 固定按时间排序，从新到旧
    if len(type) == 0 or type != 'image':
        return image_only

    cur_path = path.join(constants.attach_path, _path)
    cur_dir_path = _path
    move_up_dir_path = ''

    if _path != '':
        tmp = cur_dir_path[:(len(cur_dir_path) - 1)]
        move_up_dir_path = tmp[:tmp.rfind('/')] if tmp.find('/') >= 0 else ''

    if _path.find('..') >= 0:
        return path_error

    if _path != '' and not _path.endswith('/'):
        return path_error

    if not cur_path.startswith(constants.attach_path):
        return path_error

    if not path.exists(cur_path) or not path.isdir(cur_path):
        return path_error

    def compare(path_x, path_y):
        modify_time_x = path.getmtime(path.join(cur_path, path_x))
        modify_time_y = path.getmtime(path.join(cur_path, path_y))
        if modify_time_x < modify_time_y:
            return 1
        elif modify_time_x > modify_time_y:
            return -1
        else:
            return 0


    file_list = os.listdir(cur_path)
    file_list.sort(compare)

    items = []
    for file_name in file_list:
        item = {}
        file_path = path.join(cur_path, file_name)
        if path.isdir(file_path):
            item['is_dir'] = True
            item['has_file'] = len(os.listdir(file_path)) > 0
            item['filesize'] = 0L
            item['is_photo'] = False
            item['filetype'] = ''
        elif path.isfile(file_path):
            ext = file_name[(file_name.rfind('.') + 1):]
            item['is_dir'] = False
            item['has_file'] = False
            item['filesize'] = path.getsize(file_path)
            item['is_photo'] = ext in image_types
            item['filetype'] = ext

        item['filename'] = file_name
        item['datetime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(path.getmtime(file_path)))
        items.append(item)

    result = {}
    result['moveup_dir_path'] = move_up_dir_path
    result['current_dir_path'] = cur_dir_path
    result['current_url'] = path.join('/static/attach/', _path)
    result['total_count'] = len(items)
    result['file_list'] = items
    return result


