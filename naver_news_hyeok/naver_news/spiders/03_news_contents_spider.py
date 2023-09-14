from pathlib import Path
import datetime as dt
import pandas as pd
import re
import pickle

import scrapy

## 각 기사 데이터 크롤링
classified = {231: '아시아/호주', 232: '미국/중남미', 233: '유럽', 234: '중동/아프리카', 322: '세계 일반'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
to_wirte = []
class QuotesSpider(scrapy.Spider):
    name = "03_news_contents_spider"

    def start_requests(self):
        with open('total_news_url.txt', encoding='utf_8') as f:
            urls_classes = [_.split('\t') for _ in f.read().split('\n')[:-1]]

        for url_class in urls_classes[:300]:
            url, class__ = url_class
            # url = 'https://n.news.naver.com/mnews/article/020/0003520400?sid=104'
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, cb_kwargs={'class__': int(class__)})
        
        # pickle로 바이너리 저장
        with open('total_news_data.pkl', 'wb') as f:
            pickle.dump(to_wirte, f)

    def parse(self, response, class__):
        d = str(response.css('div.newsct_wrapper').getall())
        기자, 언론사 = d.split('Copyright ⓒ ')
        언론사 = 언론사.split('. All rights reserved. ')[0]
        기자 = 기자.split('<span class="byline_s">')[1].split('</span>')[0]
        제목 = d.split('media_end_head_title')[1].split('span>')[1][:-2]
        입력일시 = d.split('"media_end_head_info_datestamp_time _ARTICLE_DATE_TIME" data-date-time="')[1]
        수정일시 = 입력일시.split('data-modify-date-time="')[1][:19] if '_ARTICLE_MODIFY_DATE_TIME' in 입력일시 else 'null'
        입력일시 = 입력일시[:19]
        소주제 = classified.get(class__)
        소주제_id = class__
        기사_url = response.url
        사이트 = 'Naver' if classified.get(class__) else 'Daum'
        # 본문은 아직 만들지 않음.
        to_wirte.append([언론사, 기자, 제목, 입력일시, 수정일시, 소주제, 소주제_id, 기사_url, 사이트])
        