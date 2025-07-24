# 🫐 과일 & 모종 e-commerce 🫐

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)

## 🌟 프로젝트 소개

과일과 모종을 판매하는 e-commerce 플랫폼입니다. Django Framework를 사용하였으며, 고객의 요청에 의해 제작되었습니다.

### 🎯 주요 목표
- 사용자 친화적인 인터페이스 제공
- 효율적인 주문 관리 시스템 구축
- 관리자를 위한 포괄적인 관리 도구 제공

## 📸 스크린샷
| **메인 화면** | **로그인 화면** | **상품 목록** |
|:---:|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/f40acc87-255a-42a2-8db5-1156e8f6a962" width=270> | <img src="https://github.com/user-attachments/assets/a6094f4b-0a1e-4952-8e17-58c51303b3f8" width=270> | <img src="https://github.com/user-attachments/assets/ba161292-126d-40a2-80ee-73f6c1ea50c7" width=270> |
| **주문서 작성** | **관리자 대시보드** | **주문서 관리** |
| <img src= "https://github.com/user-attachments/assets/21b8bb58-3048-4ab1-8bd3-00b86e0f5312" width=270> | <img src="https://github.com/user-attachments/assets/8fa83d22-346c-4eb5-a535-3e4e916d0cc5" width=270> | <img src="https://github.com/user-attachments/assets/f8f067ad-446a-42a2-9d1c-e6a02eee85dd" width=270> |



## 🚀 주요 기능

### 🛍️ E-commerce 기능
- **상품 관리**: 상품 등록, 수정, 삭제 및 카테고리 관리
- **주문 시스템**: 
  - 주문 생성 및 관리
  - 주문 상태 추적 (입금확인중 → 배송준비중 → 배송중 → 배송완료)
  - 고유 주문번호 생성 (날짜 정보 + 랜덤숫자)

### 👥 사용자 관리
- 회원가입 및 로그인/로그아웃

### 📝 리뷰 시스템
- 배송완료 후 상품 리뷰 작성

### 🛠️ 관리자 기능
- **관리자 대시보드**
- **상품 관리**: 등록/수정/삭제
- **주문 관리**: 상태 업데이트 및 추적
- **통계 대시보드**: 
  - 총 주문 수
  - 취소 요청 현황
  - 배송 상태별 현황
- **필터링**: 주문 필터링 및 정렬

## 🛠 기술 스택

### Backend
* Python 3.x
* Django 4.2.13
* Django REST Framework 3.14.0

### Database
* SQLite3 (개발용)

### 배포 및 서버
* Gunicorn (WSGI 서버)
* Nginx (Reverse Proxy)
* GitHub Actions (CI/CD)
* AWS EC2 (배포 환경)

### 📂 프로젝트 구조
```
blueberry/
├── config/              # Django 설정 파일
├── accounts/            # 사용자 관련 앱
├── items/               # 상품 관련 앱
├── orders/              # 주문 관련 앱
├── reviews/             # 리뷰 관련 앱
├── custom_admin/        # 관리자 대시보드 커스터마이징
├── staticfiles/         # 수집된 정적 파일
└── manage.py
```

## 🚀 향후 개선 계획

* 결제 시스템 통합: 실제 결제 게이트웨이 연동
* 사용자 경험 개선: SNS 로그인 및 자동로그인 구현
* PostgreSQL 등 외부 DB 마이그레이션
