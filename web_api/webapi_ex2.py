import requests

# 웹 사이트 주소에 경로 추가
# 웹 스크레이핑(Chapter 14)에 이용했던 requests 라이브러리를 그대로 이용
base_url = "https://api.github.com/"  # 맨 끝 /까지 붙여야 함 
sub_dirs = ["events", "user", "emails"]

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)
    
# 웹 사이트 주소에 매개변수 추가: ?를 이용해 매개변수 보낼 수 있음 ?key=value 뒤에 ?붙여 추가 가능

LAT = '37.57'
LON = '126.98'
API_KEY = 'b235c57pc357fb68acr1e81'
UNIT = 'metric'

site_url = "http://api.openweathermap.org/data/2.5/weather"
parameter = "?lat=%s&lon=%s&appid=%s&units=%s" % (LAT, LON, API_KEY, UNIT)
url_para = site_url + parameter
r = requests.get(url_para)

print(r.url)

# 앞에서 생성한 URL을 요청 주소(url)와 요청 매개변수(params)로 분리 후 URL 생성
req_url = "http://api.openweathermap.org/data/2.5/weather"
req_parameter = {"lat":LAT, "lon":LON, "appid": API_KEY, "units":UNIT}
r2 = requests.get(req_url,params=req_parameter)
print(r2.url)

# URL encoding: URL은 퍼센트 인코딩을 함. 어떤 문자는 인코딩 필요(16진수 값으로 변환)
# 보통 request.get(url, params=req_parameter) 이용시 기본적으로 URL 인코딩이 되므로 신경 쓸 일 없음.
# 단 URL 인코딩 결과가 API 키 문자열로 제공되는 경우 원래대로 되돌리는 과정 필요.
API_KEY2 = "et5piq3pfpqLEWPpCbvtSQ%2Bertertg%2Bx3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw%2B9rkvoewRV%2Fovmrk3dq%3D%3D"
API_KEY_decode = requests.utils.unquote(API_KEY2)

print("Encoded url:", API_KEY2)
print("Decoded url:", API_KEY_decode)

req_url2 = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList"
tm_x = 244148.546388
tm_y = 412423.75772

req_parameter = {"ServiceKey":API_KEY_decode, "tmX":tm_x, "tmY":tm_y}
r3 = requests.get(req_url2, params=req_parameter)
print(r3.url)


