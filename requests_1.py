import requests
import re
from requests.exceptions import RequestException
import csv

def get_one_page(url):
    headers = {'user-agent':'Mozilla/5.0'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    #院校名称、院校所在地、教育行政主管部门、院校类型
    pattern = re.compile('<tr>.*?js.*?a.*?>(.*?)</a>.*?/td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
    items = re.findall(pattern, html)
    at = []
    for i in items:
        a = [x.strip() for x in i if x.strip() != '']
        at.append(a)
    for item in at:
        yield{
            'Name':item[0],
            'Place':item[1],
            'Department':item[2],
            'Type':item[3],
        }

def write_to_csvField(fieldname):
    with open("school.csv",'a',encoding = 'utf-8', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()

def write_to_csvRows(content):
    with open("school.csv",'a',encoding = 'utf-8', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writerows(content)
        f.close()

def main(offset):
    url = 'https://gaokao.chsi.com.cn/sch/search.do?searchType=1&start={0}'.format(offset) 
    html = get_one_page(url)
    rows = []
    for item in parse_one_page(html):
        rows.append(item)
    write_to_csvRows(rows)

if __name__ == '__main__':
    fieldnames = ['Name','Place','Department','Type']
    write_to_csvField(fieldnames)
    for i in range(142):
        main(offset = i*20)
