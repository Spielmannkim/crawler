# crawler

[1]지마켓 슈퍼딜상품들의 순위,상품명,판매수,링크,가격 데이터들을 매 5분간격으로 크롤링하여 엑셀에 정리

[2]정리된 엑셀파일의 각 상품명을 키값으로 매5분마다 순위,판매수를 추출하여 하나의 엑셀파일에 정리(그래프로 보기 위함)

지마켓 - https://corners.gmarket.co.kr/superdeals

# 크롤러 실행 전 다운 받아야 할 것들

[1] 파이썬 다운받기

[2] 파이썬 라이브러리와 모듈 다운받기

1.requests: HTTP 요청을 보내기 위한 모듈입니다.

설치 방법: pip install requests

2.pandas: 데이터프레임을 다루기 위한 라이브러리입니다.

설치 방법: pip install pandas

3.lxml: HTML을 파싱하기 위한 라이브러리입니다.

설치 방법: pip install lxml


# 크롤러 실행순서

[1] start.py를 실행하여 매5분마다 엑셀파일 생성

[2] 엑셀파일이 충분히 생성되면 sales.py를 실행하여 가격 데이터들을 나열한 엑셀파일 생성

[3] ranks.py를 실행하여 순위 데이터들을 나열한 엑셀파일 생성
