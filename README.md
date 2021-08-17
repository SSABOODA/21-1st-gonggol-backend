# '캉골' 웹사이트 구현 프로젝트

## 프로젝트 설명
- '캉골' 커머스 사이트를 모티브로 하여 기능 구현 하였습니다.
- 프로젝트 초기 단계부터 팀원과 협의하여 기획하였습니다.
- 모든 기능은 직접 구현하였습니다.

## 구현한 기능
- **User 회원가입, 로그인**
    - 회원가입 : Bcrpyt 암호화 하여 회원가입, 정규표현식을 활용한 유효성 체크
    - 로그인 : JWT를 사용하여 기능 구현
    - Decorator를 활용한 회원 인가 구현

- **메인 페이지, 상품목록 페이지, 상품상세 페이지**
    - 메인 페이지 :신상품, 베스트 상품 리스트 패스 파라미터로 value 받고 response ( 신상품, 베스트 임의 결정 )
    - 상품 목록 페이지 : 쿼리파라미터를 이용해 상품의 이름,가격,재고태그,이미지등의 데이터를 response 하는 API 구현
    - 패스 파라미터로 product_id 값으로 데이터 response, 각 상품들의 size 재고, 가격, discount, image, image body response

- **장바구니**
    - 기본적인 장바구니 CRUD API 구현
      Login Decorator를 통한 회원정보 확인 구현

## 프로젝트 환경
- python 3.8
- Django 3.2
- MySQL

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


