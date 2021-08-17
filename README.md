# '캉골' 웹사이트 구현 프로젝트

## 프로젝트 설명
- '캉골' 커머스 사이트를 모티브로 하여 기능 구현 하였습니다.
- 프로젝트 초기 단계부터 팀원과 협의하여 기획하였습니다.
- 모든 기능은 직접 구현하였습니다.

## 구현한 기능
- **User 회원가입, 로그인**
    - 회원가입 : Bcrpyt 암호화 하여 회원가입, 정규표현식을 활용한 유효성 체크
    - 로그인 : JWT를 사용하여 기능 구현
    - Decorator를 활용한 회원 인증 여부 기능 구현

- **메인 페이지, 상품목록 페이지, 상품상세 페이지**
    - 메인 페이지 :신상품, 베스트 상품 리스트 패스 파라미터로 value 받고 response ( 신상품, 베스트 임의 결정 )
    - 상품 목록 페이지 : 쿼리파라미터를 이용해 상품의 이름,가격,재고태그,이미지등의 데이터를 response 하는 API 구현
    - 패스 파라미터로 product_id 값으로 데이터 response, 각 상품들의 size 재고, 가격, discount, image, image body response

- **장바구니**
    - 기본적인 장바구니 CRUD API 구현
      Login Decorator를 통한 회원정보 확인 구현

## 프로젝트 환경
- Python 3.8
- Django 3.2
- MySQL

## 백엔드 사용기술
- Python
- Django
- MySQL
- JWT
- Bcrypt

## 프로젝트 형상관리 tool
- Git(Github)

## 협업 tool
- trello
- slack
- gitbook

## 프로젝트 사용법
1. Git repository 에서 clone을 받습니다.
<a href="https://github.com/SSABOODA/21-1st-gonggol-backend">프로젝트 Github 링크</a>

```
$ git clone https://github.com/SSABOODA/21-1st-gonggol-backend.git
```

## 백엔드 API 명세
<a href="https://app.gitbook.com/@gonggol/s/gonggol/">백엔드 API 명세</a>

## ERD (modeling)
<img width="1514" alt="스크린샷 2021-08-17 오후 5 08 14" src="https://user-images.githubusercontent.com/69753846/129688685-9ca47003-77d4-484c-b206-dff18ad6e37a.png">

## 프로젝트 구조
```
├── gonggol
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── my_settings.py
├── orders
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── products 
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── utils.py
    └── views.py
```
- gonggol : 프로젝트 이름입니다.(최상위 폴더)
    - gonggol/settings.py : 프로젝트의 기반이 되는 파일들이 설정되어있습니다.
- my_settings.py : github에 push되면 안되는 내용들이 있습니다. (DATABASE 설정, SECERT_KEY, ALGORITHM)
- orders : 장바구니 API를 구현하기 위한 프로젝트 app폴더입니다.
    - models.py : 장바구니 관련 DB 테이블을 작성한 파일입니다.
    - urls.py : order app 으로 들어온 요청을 views.py의 로직으로 매핑시켜주는 경로를 설정하는 파일입니다.
    - views.py : 장바구니 관련 API를 작성하기 위해 실제 기능이 작동하는 로직이 담긴 파일입니다.
- products : 사이트 메인 페이지 상품 호출, 상품 상세, 상품목록 페이지 API를 구현하기 위한 프로젝트 app폴더입니다.
- users : User 회원가입, 로그인, 회원인증 관련 데이코레이터 API를 구현하기 위한 프로젝트 app 폴더입니다.
- requirements.txt : 프로젝트를 실행하기 위해 가상환경에 설치해줘야 할 프레임워크, 라이브러리 목록입니다. ex)django, mysqlclient...


