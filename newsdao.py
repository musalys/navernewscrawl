# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
import numpy as np

from model import News
from connection import Session
from sqlalchemy import func, desc

from konlpy.tag import Kkma


class NewsDAO(object):

    def __init__(self):
        pass

    def save_news(self, link, title, content, written_time):
        saved = False
        session = Session()
        if not self.get_news_by_id(link):
            #print link
            news = News(link=link, title=title, content=content, written_time=written_time, crawl_time=datetime.datetime.now())
            session.add(news)
            session.commit()
            saved = True
        session.close()

        return saved

    def get_news_by_id(self, link):
        try:
            session = Session()
            result = session.query(News)\
                            .filter(News.link == link).first()
            return result

        except Exception as e:
            print '11', e

        finally:
            session.close()

    def get_news_content(self, news_id):

        try:
            session=Session()
            result = session.query(News)\
                            .filter(News.link == news_id).first()
            return result.content
        except Exception as e:
            print '21', e

        finally:
            session.close()

    def get_news_by_keyword_content(self, keyword):
        data = []
        session = Session()
        subquery = session.query(News)
        result = session.query(News)\
                        .filter(News.content.like('%' + keyword + '%'))\
                        .all()
        for row in result:
            news = {}
            news['link'] = row.link
            news['title'] = row.title
            news['content'] = row.content
            news['written_time'] = row.written_time
            news['crawl_time'] = row.crawl_time

            data.append(news)
        return data
