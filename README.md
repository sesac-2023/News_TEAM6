# 📰뉴스 추천 시스템

## 📢 프로젝트 개요
     뉴스 기사 및 댓글 데이터를 크롤링하고 이를 바탕으로 추천 시스템을 구축하여 
    사용자의 관심사와 비슷한 뉴스를 추천합니다. 

## 🗓️ 프로젝트 기간 
2023년 9월 13일(수) ~ 2023년 9월 22일(금)

## 📝 프로젝트 파이프라인 
<img src="https://github.com/sesac-2023/News_TEAM_6/assets/138412359/89f03c46-0a10-492b-a745-d1d2ddf68b0a" width="600" height="350"/>

## 🗂️폴더별 설명
- crawler : scrapy를 이용해 네이버와 다음의 뉴스 기사를 크롤링
- django_api : 개발 모델을 이용한 기사 추천 시스템 django_api 배포
- modelling : doc2vec 모델을 이용한 컨텐츠 기반 필터링
- preprocess : 크롤링한 기사들 전처리

## 📄기능명세서
- 뉴스 추천 홈페이지 => 임의의 뉴스 20개 리스트 노출
- 상세 뉴스 페이지 => 선택 뉴스의 본문 노출
- 추천 뉴스 페이지 => 콘텐츠 기반 필터링 추천 뉴스 20개 리스트 노출

## 📄api 명세서
- 뉴스 추천 홈페이지 => URL: news / DATA: {cat2: int, title: string}
- 상세 뉴스 페이지 => URL: news/<int:pk> / DATA: {cat2: int, title: string, content: string}
- 추천 뉴스 페이지 => URL: news/int:pk/recommend / DATA: {title: string}

<img src="https://github.com/sesac-2023/News_TEAM_6/assets/138412359/d97aa14c-d2ef-463d-9dff-dfda9629da8c" width="300" height="400"/>
<img src="https://github.com/sesac-2023/News_TEAM_6/assets/138412359/f5c5eaa7-5c62-4ee3-86eb-783acf061c97" width="300" height="400"/>




## <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> 팀주소
- https://malachite-sugar-318.notion.site/81803ba363b94a5297050016e3a85880?pvs=4

## 🤼‍♂️ 팀명 : World_News_TEAM
- **정준화** = **email**: behappy_jh@naver.com / **github**: https://github.com/JunHwa1
- **이종혁** = **email**: xhxhfh333@hanmail.net / **github**: https://github.com/wonder1ng
- **서지은** = **email**: wldms7258@gmail.com / **github**: https://github.com/jinny0203
- **장우진** = **email**: jwj1206@gmail.com / **github**: https://github.com/jwj1206

## 참고자료
- **블로그**
    - https://colinch4.github.io/2023-09-06/15-42-26-331788/ - [COLIN’S BLOG] Gensim Doc2Vec 모델 생성 및 학습
    - https://sosoeasy.tistory.com/325 - [씩씩한 IT블로그] gensim라이브러리로 학습한 doc2vec모델의 함수들





## 컨벤션
### Code Convention

- 클래스: `PascalCase`
- 변수명: `snake_case`
- 함수명: `snake_case`
- 상수: `SNAKE_CASE`

### folder and files Convention
가능하면 영문 소문자로만 구성한다.  
가능하면 짧게 구성한다(축약어 사용).  
특수문자와 빈 공백sᴘᴀᴄᴇ은 사용하지 않는다.  
단어와 단어의 구분은 ‘_’(ᴜɴᴅᴇʀʙᴀʀ) 로 구성한다.  

### Git Convention

기본 브랜치: `main`

<aside>
💡 `COMMIT_TYPE: COMMIT_SUMMARY`

</aside>

- **COMMIT_TYPE**
    - feat : 새로운 기능 추가
    - fix : 버그 수정
    - docs : 문서 추가 및 수정
    - style : 코드 포맷팅, 세미콜론 누락, 오타 수정 등
    - test : 테스트코드
    - refactor : 코드 리팩토링
    - chore : 빌드 업무 수정, 패키지 매니저 수정
- **COMMIT_SUMMARY**
    - 영어로 작성
    - 마침표를 붙이지 않음
    - 50자를 넘기지 않음

- **BRANCH_NAME**  
crawler, preprocess, modeling, api  
  
### etc
subject: 과거형은 쓰지 않는다. fixed -> fix  
type: 대문자는 쓰지 않는다.  
body: 부연설명이 필요할 시 작성  
footer: 선택사항. issue tracker id를 작성할때 사용.  

### References
https://jjam89.tistory.com/284  
https://devsosin.notion.site/1a4f6e2b5d0c44719acdacae79028244
