import requests


r = requests.get('https://api.github.com/user', auth=('lechunxiaing@163.com', 'lcx106611'))

print(r.status_code, r.headers['content-type'], r.encoding)
print(r.text)
print(r.json())