from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
from konlpy.tag import Mecab
import pandas as pd
import pickle 

# df_news 불러오기 
with open('../dataset/fin_df.pkl', 'rb') as f:    # 경로주의
    df_news = pickle.load(f)

# 형태소 분석
mecab = Mecab()
tokenized_df = [mecab.morphs(content) for content in df_news['content']]

# TaggedDocument 객체 생성
tagged_df = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokenized_df)]

# Doc2Vec 모델 생성
model = Doc2Vec(vector_size=300, min_count=2, epochs=40)

# 모델 학습
model.build_vocab(tagged_df)
model.train(tagged_df, total_examples=model.corpus_count, epochs=model.epochs)

# 학습된 모델 저장
model.save('doc2vec_fin_model.model')