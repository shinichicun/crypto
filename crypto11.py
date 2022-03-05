# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: ans.py
# Compiled at: 2018-08-09 11:29:44
import base64

def encode1(ans):
    s = ''
    for i in ans:
        x = ord(i)- 25
        x = x ^ 36
        s += chr(x)

    return s


def encode2(ans):
    s = ''
    for i in ans:
        x = ord(i)^ 36
        x = x  - 36
        s += chr(x)

    return s


def encode3(ans):
    return base64.b32decode(ans)

flag=''
final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='
flag= encode1(encode2(encode3(final).decode('ISO 8859-1')))
print('flag=',format(flag))
