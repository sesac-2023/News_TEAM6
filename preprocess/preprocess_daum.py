## pickle 파일 통합
def load_pickle():
    import pickle

    # 파일들이 연속적으로 저장되어 있는 기본 경로
    base_path = './daum_news_data_pkl/total_news_data_0{}.pkl'

    # 모든 데이터를 저장할 빈 리스트를 생성
    merged_data = []

    # 파일들을 순차적으로 읽어와서 데이터를 병합
    for i in range(10):
        file_path = base_path.format(i)
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            merged_data.extend(data)

    # 모든 데이터를 하나의 pickle 파일에 저장
    with open('./daum_news_data_pkl/merged_data.pkl', 'wb') as output_file:
        pickle.dump(merged_data, output_file)

## DatdFrame 재구조화
def making_df():
    import pandas as pd
    import pickle
    from datetime import datetime

    with open('./daum_news_data_pkl/merged_data.pkl', 'rb') as f:
        df_daum = pd.DataFrame(pickle.load(f))

    df_columns = ['cat1_name', 'cat2_name', 'platform_name', 'title', 'press', 'writer', 'date_upload', 'date_fix', 'content', 'sticker', 'url']
    classified = {1411: '아시아/대양주', 1412: '미국/아메리카', 1413: '유럽', 1414: '중동/아프리카', 1415: '국제일반', 1416: '영어뉴스', 1417: '해외화제', 1418: '일본', 1419: '중국'}

    df_daum[11] = '국제'
    df_daum = df_daum[[11,6,8,2,0,1,3,4,9,10,7]]
    df_daum[6] = df_daum[6].apply(lambda x: classified.get(int(x)))
    df_daum[1] = df_daum[1].apply(lambda x: None if str(x).find('입력 <span')==0 else x)
    df_daum[3] = [datetime(int(__[0]), int(__[1]), int(__[2]), int(__[3].split(':')[0]), int(__[3].split(':')[1])).strftime('%Y-%m-%d %H:%M:%S') for __ in [_.split('. ') for _ in df_daum[3]]]
    df_daum[4] = None
    df_daum.columns = df_columns

    return df_daum

## 불용어 처리
def stopword(df_daum):
    # 불용어 불러오기
    f = open('./stopwords.txt', 'r')
    stopwords = f.read().split("\n")

    # 불용어 부분을 공백의 문자열로 처리
    content_list = df_daum['content'].astype(str).tolist()

    for i in range(len(content_list)):
        for stopword in stopwords:
            content_list[i] = content_list[i].replace(stopword, '')

    df_daum['content'] = content_list

    return df_daum

## 본문에서 이메일 제거
def rm_email(df_daum):
    import re

    content_list = df_daum['content'].astype(str).tolist()

    content_list = [re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', '', content) for content in content_list]
    df_daum['content'] = content_list

    return df_daum

## 영어뉴스 제거
def rm_eng_news(df_daum):
    import re
    
    # 소주제가 영어뉴스인 경우
    df_daum = df_daum[df_daum['cat2_name'] != '영어뉴스']

    # 본문 내용의 70% 이상이 영어인 경우
    df_daum = df_daum[df_daum.content.apply(lambda x: (len(re.sub('[a-zA-Z]', '', x))+1)/(len(x)+1))>0.3]

    return df_daum

## 비어있는 본문의 값을 제목으로 대체
def fill_content(df_daum):
    # 인덱스값 초기화
    df_daum.reset_index(drop=True, inplace=True)

    # 본문이 비어있을 경우 제목으로 대체
    df_daum.loc[(df_daum['content'] == ''), 'content'] = df_daum['title']

    return df_daum