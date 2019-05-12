import re
import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html(html):
    bs4 = BeautifulSoup(html, 'html.parser')
    items = bs4.find_all("a", class_="nm nm-icn f-thide s-fc0")
    for item in items:
        out.write(item.text + "\n")


if __name__ == '__main__':
    # 歌手分类id
    list1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    # initial的值
    list2 = [0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
             90]
    out = open("wangyi_singer.tsv", "w", encoding="utf8")
    for i in list1:
        for j in list2:
            url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
            print('start spider {}'.format(url))
            html = get_html(url)
            parse_html(html)
