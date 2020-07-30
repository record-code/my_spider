# coding: utf-8
# @Project_Name :   LibraTest
# @File         :   main.py
# @Author       :   'yangcai'
# @Time         :   2020/7/23 9:43

from scrapy.cmdline import execute

import sys
import os

# 用来设置工程目录，有了它才可以让命令行生效
# os.path.abspath(__file__)  用来获取当前py文件的路径
# os.path.dirname()    用来获取文件的父亲的路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 调用execute()函数执行scarpy的命令 scary crawl 爬虫文件名字
execute(['scarpy','crawl','jobbole'])