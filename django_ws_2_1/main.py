import requests
import json

# 본인의 알라딘 TTBKey(API 키)를 입력하세요.
TTB_KEY = ""
BASE_URL = ""

# API 요청 파라미터 설정
params = {
    'ttbkey': TTB_KEY,
    'QueryType': 'ItemNewSpecial', # 주목할 만한 신간 리스트
    'MaxResults': 50,              # 최대 50개 데이터 요청
    'start': 1,
    'SearchTarget': 'Book',        # 조회 대상을 도서로 한정
    'output': 'js',                # 응답 데이터를 JSON으로 변경
    'Version': '20131101'
}


# API 요청 보내기
response = requests.get(BASE_URL, params=params)

# 응답받은 JSON 데이터 파싱
data = response.json()
print(data)
