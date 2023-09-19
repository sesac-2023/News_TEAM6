from pathlib import Path
import datetime as dt
import pandas as pd

import scrapy

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

## 날짜별 소주제별 기사 페이지 url 크롤링
class QuotesSpider(scrapy.Spider):
    name = "01_get_page_urls_spider"

    def start_requests(self):
        # 'https://news.daum.net/breakingnews/foreign/{}?page=99999&regDate={}'
        # 소주제 확인용 딕셔너리
        classified_k = {'아시아/대양주': 1411, '미국/아메리카': 1412, '유럽': 1413, '중동/아프리카': 1414, '국제일반': 1415, '영어뉴스': 1416, '해외화제': 1417, '일본': 1418, '중국': 1419}
        classified_e = {'asia': 1411, 'america': 1412, 'europe': 1413, 'africa': 1414, 'others': 1415, 'englishnews': 1416, 'topic': 1417, 'japan': 1418, 'china': 1419}
        base = 'https://news.daum.net/breakingnews/foreign/{}?page=99999&regDate={}'
        
        # 크롤링 날짜 지정 및 리스트 생성
        first_day = '2023-05-01'
        END_DAY = '2023-09-13'
        date_list = pd.date_range(first_day, END_DAY, freq='d')[::-1]
        date_list = [t_day.strftime('%Y%m%d') for t_day in date_list]

        # url 리스트 생성
        urls = [base.format(target_class, target_day) for target_day in date_list for target_class in classified_e.keys()]
        
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        last_page = int(response.css('div.paging_news em.num_page::text').getall()[-1])
        url_1, url_2 = response.url.split('?page=')
        new_urls = [url_1+'?page='+str(_)+url_2[5:] for _ in range(last_page,0,-1)]
        with open('total_url.txt', 'a', encoding='utf_8') as f:
	        for url in new_urls:
                    f.write(url+'\n')