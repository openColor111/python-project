#/usr/bin/env python
import requests
from lxml import etree
def get_borad(page=10):
    x=[]
    for p in range(1,page+1):
        url = "http://www.kuaidaili.com/free/outha/%s/"%(p)
        f = requests.get(url)
        htm = f.text
        f.close
        html = etree.HTML(htm)
        tbody = html.xpath('//tbody')[0]
        for i in tbody.getchildren():
            x.append((i.getchildren()[0].text,i.getchildren()[1].text))
    return x

if __name__ == '__main__':
    print(get_borad())



    
