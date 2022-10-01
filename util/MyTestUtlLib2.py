import urllib.request

# urlopen()向URL发请求,返回响应对象
response = urllib.request.urlopen('http://www.baidu.com/')
# 提取响应内容
html = response.read().decode('utf-8')
# 打印响应内容
print(html)
