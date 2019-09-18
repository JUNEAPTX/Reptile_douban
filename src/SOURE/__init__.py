from lxml import etree        
import requests               
import csv                    

fp = open('D:\Pyproject\douban.csv','wt',newline='',encoding='UTF-8')      
writer = csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))  

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]   

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

for url in urls:                     
    html = requests.get(url,headers = headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')
        url = info.xpath('td/div/a/@href')
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher =book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else ''
        writer.writerow((name,url,author,publisher,date,price,rate,comment))   
fp.close()                          