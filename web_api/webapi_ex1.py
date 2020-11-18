# 웹 API : 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
'''
REST API(이미 존재하는 데이터 공유, 데이터 요청 후 응답하면 연결 끊어짐) ->보통 이것
Streaming API(향후 발생 이벤트에 대해 등록, 이벤트 발생시 갱신 후 응답) ->가끔 이것까지 지원하기도 함.

최근에는 다 OAuth 인증 방식 채택. 보안 인증을 허용하는 개방형 인증 규약.
(앱 별로)API Key, API 비밀번호, 접속 토큰, 비밀번호를 이용.

웹 API로 요청해 응답받은 데이터 형식은 주로 JSON, XML.
    -> 데이터를 전달하기 위해 만든 구조화된 텍스트 형식
XML - 먼저 등장해 사용되어 왔음.
JSON - 구조 단순. XML보다 텍스트 크기 작아 전송 빠름. 데이터 추출 분석이 더 쉬움.
최근에는 JSON을 더 많이 쓰는 추세.
'''

# JSON(JavaScript Object Notation) 형식:
# {"이름": "값", ... "신체정보" : {" ":, " ":  } }
# 객체는 {}로 감싸고 각 쌍은 ,로 구분. 이름은 문자열. 값은 숫자, 문자열, 배열, 또다른 객체 다 가능.

# JSON 형식 검사 사이트 http://jsonlint.com
# JSON 뷰어 설치 또는 JSON 온라인 뷰어 http://jsonviewer.stack.hu 이용

import json
import xmltodict

python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}
type(python_dict)  # str

# JSON Data로 변환(Dict -> JSON)
json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(type(json_data))
print(json_data)

# JSON -> Dict 변환
json_dict = json.loads(json_data)
print(type(json_dict))  # dict

# json_dict['취미']로 취미 리스트 뽑아내기 가능.
# 그 중 첫 번째 추출하려면 json_dict['취미'][0]



# XML(eXtensible Markup Language): 데이터 저장 및 전달을 위해 만든 다목적 마크업 언어
# HTML과 달리 자신이 태그를 정의해 사용 가능.
# xml에서 dict 타입 변환은 xmltodict 라이브러리 이용

# xml data를 넣음: type class 'str'
xml_data = """<?xml version="1.0" encoding="UTF-8" ?>
    <사용자정보>
        <이름>홍길동</이름>
        <나이>25</나이>
        <거주지>서울</거주지>
        <신체정보>
            <키 unit="cm">175.4</키>
            <몸무게 unit="kg">71.2</몸무게>
        </신체정보>
        <취미>등산</취미>
        <취미>자전거타기</취미>
        <취미>독서</취미>
    </사용자정보>
"""
print(xml_data)
print(type(xml_data))

# xml -> dict로 변환
# 속성은 @속성이름, 속성 있는 태그 문자열은 #text로 표시
dict_data = xmltodict.parse(xml_data, xml_attribs=True)  # xml_attribs=False로 설정시 XML데이터 속성 무시

# 딕셔너리 타입 데이터이므로 앞에서와 똑같이 추출 가능
dict_data['사용자정보']['이름']

user_name = dict_data['사용자정보']['이름']
body_data = dict_data['사용자정보']['신체정보']

height = body_data['키']['#text']
height_unit = body_data['키']['@unit']

weight = body_data['몸무게']['#text']
weight_unit = body_data['몸무게']['@unit']

print("[사용자 {0}의 신체정보]".format(user_name))
print("*키: {0}{1}".format(height, height_unit))
print("*몸무게: {0}{1}".format(weight, weight_unit))

