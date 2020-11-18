#API 키 사용 없이 데이터 가져오기
import requests
import json
import time

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
print(r.text)

json_to_dict = json.loads(r.text)
print(type(json_to_dict))

# 웹API 응답 결과를 바로 딕셔너리 타입으로 변환하도록 코드 단순화
json_to_dict2 = requests.get(url).json()
print(type(json_to_dict2))

# JSON->딕셔너리 변환 후에는 [] 안에 키 지정해 단계별 접근 가능.(원하는 데이터 추출)
print(json_to_dict2["iss_position"])
print(json_to_dict2["iss_position"]["latitude"])
print(json_to_dict2["iss_position"]["longitude"])
print(json_to_dict2["message"])
print(json_to_dict2["timestamp"])
''''
def ISS_Position(iss_position_api_url):
    json_to_dict2 = requests.get(iss_position_api_url).json()
    return json_to_dict2["iss_position"]

# 우주정거장 위치를 10초마다 갱신
for k in range(5):
    print(ISS_Position(url))
    time.sleep(10)
'''

# 국가 정보 가져오기(REST Countries의 국가 관련 정보 이용)
url_temp = "https://restcountries.eu/rest/v1/name/"
country = "South Korea"
url2 = url_temp + country
r2 = requests.get(url2)
print(r2.text)

json_to_list = requests.get(url2).json()
print(json_to_list)

