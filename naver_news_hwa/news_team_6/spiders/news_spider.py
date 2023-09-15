import scrapy 
from datetime import datetime, timedelta
from .. import items
import time 



class NavernewsSpider(scrapy.Spider):
    name = 'navernews'
    
#    BASE_URL = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2={}&sid1=104&date={}&page={}"

    def start_requests(self):
#        categories = {
#            '231' : '아시아/호주',
#            '232' : '미국/중남미',
#            '233' : '유럽',
#            '234' : '중동/아프리카',
#            '322' : '세계 일반'
#            }
#        for k, v in categories.items():
#            target_day = "2023-09-13"
#            URL = self.BASE_URL.format(k, date, page)

        start_urls = [
            "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=231&sid1=104&date={}&page={}",
            "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=232&sid1=104&date={}&page={}",
            "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=233&sid1=104&date={}&page={}",
            "https://news.naver.com/main/list.naver?mode=LS2D&sid2=234&mid=shm&sid1=104&date={}&page={}",
            "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=322&sid1=104&date={}&page={}"
                    ]

        for url in start_urls:
            date_today = datetime.now()
            for day in range(1, 11):  # 우선 10일치만 크롤링
                target_day = date_today - timedelta(days=day)
                for page in range(1, 11): # 우선 10 page만 
                    url = url.format(target_day.strftime('%Y%m%d'), page)  #위에 주석 쓰면 (k, date, page)순으로 넣어야 함.
                    # url = url.format(page, 1)
                    headers = {
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                    }

                    yield scrapy.Request(url=url, headers=headers, callback=self.parse, cb_kwargs={
                        'target_day' : target_day,
                        'page' : page
                    })

    time.sleep(2)

    def parse(self, response, target_day, page):
      
        news_li = response.css("li dl dt:first-child a::attr(href)").getall()
        print("-"*20)
        print(page, target_day.strftime('%Y%m%d'))
        print()
        for u in news_li:
            headers = {
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                    }
                    
            yield scrapy.Request(url=u, headers=headers, callback=self.parse_items)    
    time.sleep(2)
    #def news_details(self, response):
    #    title = response.css('#title_area > span.text::text').get().strip()
    #    context = response.css('#dic_area.text::text').get().strip()
    #    reporter = response.css('#contents > div.byline > p > span.text::text').get().strip()
#
    #    print(title)
    #    print(context)
    #    print(reporter)
    
    def parse_items(self, response):
        item = items.NewsTeam6Item()
        item['title'] = response.css('h2#title_area span::text').get()
        #item['context'] = response.css('#dic_area.text::text').get().strip()
        item['reporter'] = response.css('p.byline_p span::text').get()
        yield item

