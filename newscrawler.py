# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
import requests
import json
import re
from bs4 import BeautifulSoup
from newsdao import NewsDAO


class NaverNewsCrawler(object):

    def __init__(self, newsdao, url):
        self.newsdao = newsdao
        self.url = url

    def get_topics(self):

        res = requests.get(self.url)
        content = res.content
        soup = BeautifulSoup(content)

        soup_1 = soup.find('div', attrs={'id': "lnb"})
        soup_2 = soup_1.find_all('a', href=True)

        topic_list = []
        for topic_link in soup_2:
            #print topic_link['href']
            topic_list.append(home + topic_link['href'])

        #print topic_list
        self.get_article_links(topic_list)


    def get_article_links(self, urls):

        for url in urls:
            res = requests.get(url)
            content = res.content
            soup = BeautifulSoup(content)

            try:
                soup_1 = soup.find('div', attrs={'id': "main_content"})
                soup_2 = soup_1.find_all('a', href=True)

                for k in soup_2:
                    #print k['href']
                    link = k['href']
                    self.crawl_title_content(link)

            except Exception as e:
                print '1', e

    def crawl_title_content(self, link):

        res = requests.get(link)
        content = res.content
        soup = BeautifulSoup(content)

        try:
            title = soup.find('h3', attrs={"id": "articleTitle"}).get_text().strip()
            content = soup.find('div', attrs={"id": "articleBodyContents"}).get_text().strip()
            content_re = re.sub(r'//.+\n.+{}', '', content)
            content = content_re.strip()
            written_time = soup.find('span', attrs={"class": "t11"}).get_text()

            print link
            print str(title)
            print str(content)
            print str(written_time)
            print '-' * 80

            self.newsdao.save_news(link, str(title.encode('utf-8')), str(content.encode('utf-8')), str(written_time.encode('utf-8')))

        except Exception as e:
            print '2', e


home = 'http://news.naver.com'

if __name__ == '__main__':
    #memcache = MemCache()
    newsdao = NewsDAO()

    crawler = NaverNewsCrawler(newsdao, home)
    crawler.get_topics()
