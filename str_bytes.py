# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 下午6:55
# @Author  : wonderstone
# @FileName: str_bytes.py
# @Software: PyCharm
# @Ref00   :https://docs.python.org/3/library/stdtypes.html?highlight=str#str
# @Ref01   :https://docs.python.org/3/library/stdtypes.html?highlight=bytes#bytes


# website = 'http://www.gpxtrade.net/'
website = '我是超人'
print(type(website))
# Bytes Objects
website_bytes_utf8 = website.encode(encoding="utf-8")
print(website_bytes_utf8.hex())
website_bytes_gbk = website.encode(encoding="gbk")
print(website_bytes_gbk.hex())

pass
# 解码回string
print(website_bytes_utf8.decode())
print(website_bytes_gbk.decode("gbk"))