#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 16:21
# @Author  : lingxiangxiang
# @File    : test.py
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def noextension(wd):
    url = "https://www.baidu.com/s?wd={0}".format(wd)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # print(url)
    s = requests.session()
    result = s.get(url=url, headers=headers)
    result.encoding = "utf-8"
    html = result.text
    # print(html)
    # print(result.url)
    reg = re.compile(r'(<!-- new ppim --><div(.*)(\n)+)')
    result = re.findall(reg, html)
    print(result)
    # print(result[0][0])
    # print(result[1][0])
    print(len(result[0]))
    for i in result:
        text = html.replace(str(i[0]), '')
        html = text
    # print(text)

    reg1 = re.compile(r'(<script id="ecomScript">\s+.*\n}catch.*\s+</script>)')
    result1 = re.findall(reg1, text)
    print(result1)
    print(len(result1))
    if result1:
        html1 = text.replace(result1[0], '')
    else:
        html1 = text


    with open('1.html', 'wb') as f:
        f.write(html1.encode("utf-8"))

    return html1

def baidu(wd):
    url = "https://www.baidu.com/s?wd={0}".format(wd)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    s = requests.session()
    r = s.get(url=url, headers=headers)
    r.encoding = "utf-8"
    html = r.text
    return html
def tuiguang(context):
    reg = re.compile(r'(<!-- new ppim --><div(.*)(\n)+)')
    result = re.findall(reg, context)
    return result



if __name__ == "__main__":
    # noextension("python")
    context = baidu("python")
    result = tuiguang(context)
    print(result)
