#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 20:59
# @Author  : lingxiangxiang
# @File    : main.py
import re

import web
from web.template import render
import requests
import test

urls = (
    '/', 'index',
    '/search', 'search',
)


class index():
    def GET(self):
        render = web.template.render("templates")
        return render.index()

class search():
    def GET(self):
        # render = web.template.render("templates")
        data = web.input()
        wd = data.get('wd')
        result = test.noextension(wd)
        return result


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
