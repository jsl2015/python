# -*- coding:utf-8 -*-

import sys
import requests
reload(sys)
sys.setdefaultencoding('utf8')

url_1 = "http://www.tngou.net/tnfs/api/list"
# url_2 = "http://www.tngou.net/tnfs/api/classify"
src_header = "http://tnfs.tngou.net/image"
headers = {'apikey':'c242b402d39b2bdea96c372b1dd7d87b'}
params_1 = {
    'page': 3,
    'rows': 20,
    'id': 6      # 需根据classify结果才能知道
}
r = requests.get(url_1)
r = r.json()
# 保存图片到本地路径


def saveImage(imgUrl, imgName='default.jpg'):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    dst = "e:\test"
    path = dst+imgName
    print 'save the file:'+path+'\n'
    with open(path, 'wb') as img:
        img.write(image)
    img.close()
# 开始


def run():
    for line in r['tngou']:
        title = line['title']
        img = line['img']
        src_path = src_header+img
        saveImage(src_path, title+'.jpg')
run()
