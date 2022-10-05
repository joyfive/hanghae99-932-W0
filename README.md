# 사전프로젝트 : 2022년 9월 OTT 콘텐츠 추천
### # 크롤링, [GET] [POST] 연습 

목차

## 팀원 및 역할

오기쁨(팀장) : 몽고 DB to 서브페이지 [GET] method 활용 UI 노출 연동 및 디자인 전반 css 수정 <br>
유도원 : 코멘트 CRUD [GET] [POST] method 활용<br>
원민재 : 메인페이지 크롤링 데이터 몽고DB 활용 [GET] method 로 UI 노출 연동

## 프로젝트 소개

<p align="justify">

## <a href="https://www.notion.so/joyfive/32-d9ad428c46a84647b6289da3801ae337">SA</a>

<br>

## 기술 스택

HTML / CSS / JavaScript / Python / Flask / mongoDB

<br>

## 구현 기능

### 기능 1 : 회원가입 및 로그인


### 기능 2 : 메인페이지
#### 1) 리스팅 기능 [GET]method


#### 2) 상세페이지 이동링크


### 기능 3 : 게시글 입력 및 확인<br>
#### 1) 크롤링 모듈 동작 : <br>
- JS) 사용자 input 값을 파라미터로 치환하여 POST 요청 <br>
- Python) bs4 크롤링 및 데이터 가공 후 프론트로 response 전달 <br>
- JS) 가공데이터로 temp_html 사용자 노출<br>

#### 2) write.html 
- Jinja2 템플릿 엔진을 이용한 서버사이드 렌더링으로 게시판 기능 구현 <br>
- 사용자가 지니뮤직의 파라미터값 입력 시 크롤링 모듈 동작<br>
- 가공데이터로 전달받은 response 값은 사용자 노출 및 게시글 데이터 저장 시 같이 저장 <br>
- 글제목+내용+별점 입력 후 함께 mongoDB에 데이터 저장 <br>
- 게시글 작성 <br>
- 메인페이지 정상 리스팅 확인<br>

#### 3) view.html <br>
- 매개변수 keyworld [jinja] 상세 페이지 url 분기 [GET]:jinja를 활용한 서버사이드렌더링 방식<br>
- write에서 POST한 크롤링데이터 및 사용자 데이터 find<br>
- json으로 프론트에서 상세<br>

<br>

## 배운 점 & 아쉬운 점

(기쁨)<br>
<b> 배운 점</b>


<b>아쉬운 점</b>


(도원)<br>
*배운점 <br>
  * API 요청에 대한 Method 활용
  * 데이터 삭제 기능
*아쉬운점 <br>
  * JWT을 활용한 로그인 기능
  * 데이터 수정기능
(민재)<br>
배운 점 <br>


아쉬운 점 <br>


<p align="justify">

</p>

<br>

## 라이센스

Copyright 2022. hang-hae99 9th W0 team 32. all rights reserved.
