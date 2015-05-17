# -*- coding: utf-8 -*-

import sys
from tornado.ioloop import IOLoop
from tornado.web import Application
from config.constants import settings
from config.route import handler_mapper

__author__ = 'wuyongxing'

reload(sys)
sys.setdefaultencoding('utf-8')

application = Application(handler_mapper, **settings)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            settings['listen_port'] = int(sys.argv[1])
        except ValueError:
            pass

    application.listen(settings['listen_port'])
    IOLoop.instance().start()