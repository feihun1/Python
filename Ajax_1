import requests
from urllib.parse import urlencode
import os
import time
from hashlib import md5
from multiprocessing.pool import Pool
import re
from urllib import request

keyword = '风景图'
timestamp = int(time.time())
keyword = keyword.encode("utf-8").decode("latin1")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
cookie = 'ttcid=29f0413def8a432e911f5a8f0622c3e938; csrftoken=12c91af6803ee5219ca2f8eb09a2f9d2; SLARDAR_WEB_ID=1b418c99-ae08-4284-aa13-5220bb44121a; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6842093343468553742; s_v_web_id=verify_kbu495tl_il4XjJEE_YjYj_4BHi_BXAN_WUQw8uhE8sP5; tt_webid=6842093343468553742; __tasessionId=v632jba0a1593049020314; tt_scid=LZrB2fy4ZVkIWqA4clnAFMYCOpzBBb5c.pJoxnanif8eiMHBvwDeBmE0X-Gh.qAt1035'
headers = {
    'Host':'www.toutiao.com',
    'Referer':'https://www.toutiao.com/search/?keyword=' + keyword,
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    'cookie':cookie
}

def get_page(offset):
    params = {
        'aid':'24',
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'风景图',
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':timestamp,
        '_signature':'S.3WlAAgEBCNqm8ZbVhwnUv8l4AABULWpnDsH9iOdkmYDzTXvj6Ba3K1AAna2lebFVsbNzxOk1-1M91ct3XBPxs8qtt71.3wH2PwJHprF2FmttxNpkYHd.FyshtAqt3Zn.v'
    }
    url = "https://www.toutiao.com/api/search/content/?" + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
        
   def main(offset):
    json = get_page(offset)
    datas = json['data']
    for data in datas:
        try:
            #替换标题中的特殊符号和去掉空格
            title = re.sub(r'[\\/\:\*?<>\|]*','',data['title']).strip()
        except:
            continue
        #创建图片标题名对应的文件夹
        dir_path = os.path.join('这里写要保存的路径',title)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        try:
            for i,image in enumerate(data['image_list']):
                url = re.sub(r'list/190x124|list','origin',image['url'])
                try:
                    request.urlretrieve(url, os.path.join(dir_path, '%d.jpg'%(i+1)))
                except:
                    print("error")
        except:
            pass
def main(offset):
    json = get_page(offset)
    datas = json['data']
    for data in datas:
        try:
            #替换标题中的特殊符号和去掉空格
            title = re.sub(r'[\\/\:\*?<>\|]*','',data['title']).strip()
        except:
            continue
        #创建图片标题名对应的文件夹
        dir_path = os.path.join('这里写要保存的路径',title)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        try:
            for i,image in enumerate(data['image_list']):
                url = re.sub(r'list/190x124|list','origin',image['url'])
                try:
                    request.urlretrieve(url, os.path.join(dir_path, '%d.jpg'%(i+1)))
                except:
                    print("error")
        except:
            pass

GROUP_START = 1
GROUP_END = 5
if __name__ == '__main__':
    for i in range(GROUP_START, GROUP_END+1):
        main(offset = i*20)
