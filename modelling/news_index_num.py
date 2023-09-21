from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
from konlpy.tag import Mecab
import pandas as pd
import pickle


class doc2vec_news:
    def __init__(self):
        # 저장된 모델 불러오기 
        self.model = Doc2Vec.load('../dataset/save_model/doc2vec_fin_model.model')   # 경로주의

    def news_index(self, index_num):
    
        a = index_num  # a번째 뉴스
        b = 20    # 추천 뉴스 개수

        news = []
        for i in self.model.docvecs.most_similar(a, topn=b):
            news.append(i[0])
            print(i)
            
        return news         
        
        