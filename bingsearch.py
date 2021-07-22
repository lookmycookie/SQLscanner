# coding:utf-8
# /usr/env/python3
import requests
from lxml import etree

bing = 'https://cn.bing.com/search?q='

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
i = 0

print('''______ _               _       _           _   _                           _       _    ______       _       _       _____                     _     
| ___ (_)             (_)     (_)         | | (_)                         (_)     | |   | ___ \     | |     | |     /  ___|                   | |    
| |_/ /_ _ __   __ _   _ _ __  _  ___  ___| |_ _  ___  _ __    _ __   ___  _ _ __ | |_  | |_/ / __ _| |_ ___| |__   \ `--.  ___  __ _ _ __ ___| |__  
| ___ \ | '_ \ / _` | | | '_ \| |/ _ \/ __| __| |/ _ \| '_ \  | '_ \ / _ \| | '_ \| __| | ___ \/ _` | __/ __| '_ \   `--. \/ _ \/ _` | '__/ __| '_ \ 
| |_/ / | | | | (_| | | | | | | |  __/ (__| |_| | (_) | | | | | |_) | (_) | | | | | |_  | |_/ / (_| | || (__| | | | /\__/ /  __/ (_| | | | (__| | | |
\____/|_|_| |_|\__, | |_|_| |_| |\___|\___|\__|_|\___/|_| |_| | .__/ \___/|_|_| |_|\__| \____/ \__,_|\__\___|_| |_| \____/ \___|\__,_|_|  \___|_| |_|
                __/ |        _/ |                             | |                                                                                    
               |___/        |__/                              |_|                                                                                    

''')
print('搜索语法：')
print('inurl:asp?id=')
print('inurl:php?id=')
i = 0
print('输入关键字')
keyword = input()


def get_pages(keyword, pages):
    pages = pages * 10 + 1
    pages = str(pages)
    url = bing + keyword + '&first=' + pages
    print(url)
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    res = tree.xpath('//div[@class="b_caption"]/div/cite/text()')
    print(res)
    return res


while i < 1000:
    urls = get_pages(keyword, i)
    for url in urls:
        print(url)
        result_file = open('beingurls.txt', 'a+', encoding='utf-8')
        result_file.write(url + '\r')
    i = i + 1
