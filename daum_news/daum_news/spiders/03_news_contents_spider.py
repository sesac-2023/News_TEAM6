from pathlib import Path
import datetime as dt
import pandas as pd
import re
import pickle
import requests
import json

import scrapy

## 각 기사 데이터 크롤링
classified_k = {'아시아/대양주': 1141, '미국/아메리카': 1142, '유럽': 1143, '중동/아프리카': 1144, '국제일반': 1145, '영어뉴스': 1146, '해외화제': 1147, '일본': 1148, '중국': 1149}
classified_e = {'asia': 1141, 'america': 1142, 'europe': 1143, 'africa': 1144, 'others': 1145, 'englishnews': 1146, 'topic': 1147, 'japan': 1148, 'china': 1149}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTY5NDczODQyNSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiYjk3NjUyYWEtMzc1Mi00NDk4LWI0NzktOGE2NjQ2ZjIyNjVkIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.Dm81YMRQjcIxaKL-3SSVOmSvgn9XB_WVA4pF0O_wRak'
}
base_sticker = 'https://action.daum.net/apis/v1/reactions/home?itemKey='
to_wirte = []

class QuotesSpider(scrapy.Spider):
    name = "03_news_contents_spider"

    def start_requests(self):
        
        with open('total_news_url.txt', encoding='utf_8') as f:
            urls_classes = [_.split('\t') for _ in f.read().split('\n')[:-1]]
        # idx = int(__file__[-5:-3])
        # idx_list = [i for i in range(0,len(urls_classes), int(len(urls_classes)/10))][:-1]+[len(urls_classes)]
        # urls_classes = urls_classes[idx_list[idx]+idx_list[idx]]

        # scrapy가 마지막 작업은 실패해도 완료하여 해당 개수만큼 뒷부분 url 추가
        for url_class in urls_classes+urls_classes[-33:]:
            url, class__, agency = url_class
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, cb_kwargs={'class__': class__, 'agency': agency})

        # pickle로 바이너리 저장
        # with open(f'total_news_data_{idx}.pkl', 'wb') as f:
        with open(f'total_news_data.pkl', 'wb') as f:
            pickle.dump(to_wirte, f)

    def parse(self, response, class__, agency):
        d = str(response.css('article.box_view').getall())
        제목 = d.split('<h3 class="tit_view" data-translation=')[1].split('</h3>')[0].split('>')[1]
        기자 = d.split('<span class="txt_info">')[1].split('</span>')[0]
        입력일시 = d.split('<span class="num_date">')[1].split('</span>')[0]
        수정일시 = 'null'
        소주제_id = str(classified_e.get(class__))
        기사_url = response.url
        사이트 = 'Daum' if classified_e.get(class__) else 'Naver'
        본문 = ''.join(response.css('div.news_view.fs_type1 div.article_view section p::text').getall()).strip()
        언론사 = agency
        소주제 = class__
        스티커 = json.loads(requests.get(base_sticker+기사_url[21:], headers=headers).text)['item']['stats']

        to_wirte.append([언론사, 기자, 제목, 입력일시, 수정일시, 소주제, 소주제_id, 기사_url, 사이트, 본문, 스티커])
