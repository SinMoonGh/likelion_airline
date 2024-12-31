# airline

### 항공편 예매 사이트
- 참여 인원 : 2명
- 프로젝트 기간 : 2024-12-24 ~ 2024-12-31
- 프로젝트 언어 : JavaScript, Python
- 프로젝트 프레임워크 : React, Django
- 데이터베이스 : MySQL

## 핵심기능

- 회원가입
- 로그인
- 사용자 삭제
- 사용자 티켓 조회
- 티켓 예매
- 티켓 환불
- 비밀번호 변경
- 항공편 목록 조회

## 요구사항

#### 유저 관련 API
1. 회원가입 (Signup)
- URL: POST /signup
- 설명: 새로운 사용자를 등록합니다.
- 요청 본문
```
{
 "firstName": "string",
 "lastName": "string",
 "email": "string",
 "password": "string"
}
```
- 응답 본문:
```
{
 "message": "회원가입 성공",
}
```

2. 로그인 (Login)
- URL: POST /login
- 설명: 사용자가 로그인하고 JWT 토큰을 발급받습니다.
- 요청 본문:
```
{
 "email": "string",
 "password": "string"
}
```
- 응답 본문:
```
{
 "message": "로그인 성공",
 "token": {JWT 토큰},
 "user": "string"
}
```

3. 사용자 삭제 (Delete User)
- URL: DELETE /users/:uid
- 설명: 사용자를 삭제합니다.
- 요청 헤더: Authorization: Bearer {JWT 토큰}
- 경로 매개변수: uid (삭제할 사용자 ID)
- 응답 본문:
```
{
 "message": "사용자 삭제 성공",
}
```

#### 항공편 관련 API

1. 항공편 목록 조회 (Get Tickets)
- URL: GET /tickets
- 설명: 모든 사용자의 티켓을 조회합니다.
- 요청 헤더: Authorization: Bearer {JWT 토큰}
- 요청 쿼리 파라미터:
  - page : 페이지 번호 (기본값: 1)
  - limit : 한 페이지에 표시할 티켓 수 (기본값: 10)
- 응답 본문:
```
{
  "totalItems": number,
  "totalPages": number,
  "currentPage": number,
  "tickets": [
    {
      "id": number,
      "departure": "대한민국",
      "departure_airport": "인천국제공항",
      "departure_airport_code": "ICN",
      "destination": "일본",
      "destination_airport": "도쿄 나리타 공항",
      "destination_airport_code": "NRT",
      "departure_date": "2024-05-01",
      "destination_date": "2024-05-01",
      "departure_time": "10:00",
      "destination_time": "14:00",
      "duration": "4시간",
      "airline": "대한항공",
      "flightClass": "이코노미",
      "price": 500000
    }
  ]
}
```

2. 티켓 구매 (Purchase Ticket)
- URL: POST /purchase/:ticket
- 설명: 사용자가 티켓을 구매합니다.
- 요청 헤더: Authorization: Bearer {JWT 토큰}
- 요청 본문:
```
{ 
 "flightId": string
 "userId": string
}
```
- 응답 본문:
```
{
  "message": "구매 완료",
  "ticket": {
    "id": number,
    "departure": "대한민국",
    "departure_airport": "인천국제공항",
    "departure_airport_code": "ICN",
    "destination": "일본",
    "destination_airport": "도쿄 나리타 공항",
    "destination_airport_code": "NRT",
    "departure_date": "2024-05-01",
    "destination_date": "2024-05-01",
    "departure_time": "10:00",
    "destination_time": "14:00",
    "duration": "4시간",
    "airline": "대한항공",
    "flightClass": "이코노미",
    "price": 500000
  }
}
```

3. 티켓 환불 (Refund Ticket)
- URL: POST /tickets/:ticketId/refund
- 설명: 사용자가 특정 티켓을 환불합니다.
- 요청 헤더: Authorization: Bearer {JWT 토큰}
- 경로 매개변수:
  - ticketId : 환불할 티켓 ID
- 응답 본문:
```
{
 "message": "티켓이 환불되었습니다."
}
```

#### 비밀번호 관련 API

1. 비밀번호 변경 (Change Password)
- URL: POST /change-password
- 설명: 사용자가 비밀번호를 변경합니다.
- 요청 헤더: Authorization: Bearer {JWT 토큰}
- 요청 본문:
```
{
 "oldPassword": "string",
 "newPassword": "string"
}
```
응답 본문:
```
{
 "message": "비밀번호가 변경되었습니다."
}
```

#### 항공편 관련 API

1. 항공편 조회 (Get Flights)
- URL: GET /flights
- 설명: 항공편 목록을 조회합니다.
- 요청 쿼리 파라미터:
  - departures : 출발지 (옵션)
  - arrivals : 도착지 (옵션)
  - departure_date : 출발 날짜 (YYYY-MM-DD)  (옵션)
  - arrival_date : 도착 날짜 (YYYY-MM-DD)  (옵션)
  - page : 페이지 번호 (기본값: 1) 
  - limit : 한 페이지에 표시할 항공편 수 (기본값: 5)
  - flightClass : 좌석 클래스 (옵션)
  - airline : 항공사 (옵션)
- 응답 본문:
```
{
    "totalItems": number,
    "totalPages": number,
    "currentPage": number,
    "flights": [
        {
            "id": number,
            "departure": "대한민국",
            "departure_airport": "인천국제공항",
            "departure_airport_code": "ICN",
            "destination": "일본",
            "destination_airport": "도쿄 나리타 공항",
            "destination_airport_code": "NRT",
            "departure_date": "2024-05-01",
            "destination_date": "2024-05-01",
            "departure_time": "10:00",
            "destination_time": "14:00",
            "duration": "4시간",
            "airline": "대한항공",
            "flightClass": "이코노미",
            "price": 500000
        }
    ]
}
```

#### 대륙과 국가 정보

1. 대륙과 국가 조회 (Get Continents and Countries)
- 설명: 대륙과 국가 정보를 조회합니다.
- 응답 본문:
```
{
    "continents": [
        {
            "continent": "아시아",
            "countries": ["대한민국", "일본", "중국"]
        },
        {
            "continent": "유럽",
            "countries": ["독일", "프랑스", "영국"]
        },
        {
            "continent": "북미",
            "countries": ["미국", "캐나다", "멕시코"]
        }
    ]
}
```

#### 항공사 목록 (Get Airlines)
- 설명: 항공사 목록을 조회합니다.
- 응답 본문:
```
["대한항공","아시아나항공","에어부산","제주항공","티웨이항공"]
``` 
