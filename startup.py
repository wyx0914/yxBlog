# -*- coding: utf-8 -*-

import sys
from tornado.ioloop import IOLoop
from tornado.web import Application
from config.constants import settings
from config.route import mapper

__author__ = 'wuyongxing'


application = Application(mapper, **settings)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            settings['listen_port'] = int(sys.argv[1])
        except ValueError:
            pass

    application.listen(settings['listen_port'])
    IOLoop.instance().start()