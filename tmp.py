# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午11:04
# @Author  : wonderstone
# @FileName: tmp.py
# @Software: PyCharm
# @Ref     : https://cryptography.io/en/latest/fernet/


from cryptography.fernet import Fernet, MultiFernet

key = Fernet.generate_key()
print("key: ",key)
F = Fernet(key)
info = "my deep dark secret"
# 加密信息
token = F.encrypt(info.encode())
print("token: ",token)
# 解密信息
de_info = F.decrypt(token)
print(de_info.decode())

key1 = Fernet.generate_key()
print("key1: ",key1)
F1 = Fernet(key1)
key2 = Fernet.generate_key()
print("key2: ",key2)
F2 = Fernet(key2)

# MultiFernet performs all encryption options using the first key in the list provided.
# MultiFernet attempts to decrypt tokens with each key in turn.
FM = MultiFernet([F1, F2])
tokenFM = FM.encrypt(info.encode())
print("tokenFM: ",tokenFM)
print("FM.decrypt: ",FM.decrypt(tokenFM))
key3 = Fernet.generate_key()
print("key3: ",key3)
F3 = Fernet(key3)
FM2 = MultiFernet([F3, F1, F2])
# rotate a token by decrypt and re-encrypting it under the MultiFernet instance’s primary key.
rotated = FM2.rotate(tokenFM)
print("rotated: ",rotated)
print(FM2.decrypt(rotated))
