#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 3:16 下午
# @Author  : zhiqi.chen
# @File    : jump7.py
# @Software: PyCharm

num = 0
while num < 100:
    num = num + 1
    if num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
        continue
    print(num)