#！python3
# -*- coding: utf-8 -*-

import urllib.request
import re

import os

# 保存文件，保存二进制文件时不用指定文件编码
def saveFile(data, file = './h.txt'):
    save_path = file
    f_obj = open(save_path, 'w', encoding="UTF-8")
    # f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()


# 分析网页文件，获取网页标题
def getTitle(data):
    pattern = re.compile('<title>(.*?)</title>')
    for x in pattern.findall(data):
        saveFile(x)
        break


# 抓取网页
def catchUrl(url):
    mUrl = url
    # data 是使用 utf-8 解码后的字符串
    data = urllib.request.urlopen(mUrl, timeout = 2).read().decode('utf-8')
    # data 是网页的二进制源码，如果要保持最大的灵活性，这里可以选择保存二进制文件
    # data = urllib.request.urlopen(mUrl, timeout = 2).read()
    return data


# 程序主体
if __name__ == '__main__':
    data = catchUrl("http://www.baidu.com/")
    saveFile(data, './hehe.txt')
    getTitle(data)
