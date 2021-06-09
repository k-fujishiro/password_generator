import base64
import hashlib
import pyperclip
head = 'gSat7mO+hEi'
tail = '9tEn3n'
mid = input('Input string!')
str = head + mid + tail
pwd = base64.b64encode(hashlib.sha256(str.encode('utf-8')).digest())
print(pwd)
pyperclip.copy(pwd.decode(encoding='utf-8'))
