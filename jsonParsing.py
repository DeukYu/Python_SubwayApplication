import urllib.request, json, urllib.parse, pprint, http.client

#서울시 지하철 역사 정보 조회
def FindStation(stationName):
    base_url = 'http://swopenAPI.seoul.go.kr/api/subway/49556d7755726c6137384e5475776f/json/stationInfo/0/100/'
    path = urllib.parse.quote(stationName)
    with urllib.request.urlopen(base_url + path) as url:
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data

def FindRoute(start, end):
    base_url = 'https://api.odsay.com/v1/api/subwayPath?lang=1&CID=1000&SID=201&EID=222&Sopt=1&'
    path = urllib.parse.quote('apiKey=kVDgXCUs3Kdt7zL9KhbKog')
    with urllib.request.urlopen(base_url + path) as url:
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data

def FindStationFirstLast(stationName):
    base_url = 'http://swopenAPI.seoul.go.kr/api/subway/75524f4e69726c6136386263747374/json/firstLastTimetable/0/100/'
    path = urllib.parse.quote(stationName)
    with urllib.request.urlopen(base_url + path) as url:
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data

def FindStationUseRate(stationName):
    base_url = 'http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayTime/1/100/201501//'
    path = urllib.parse.quote(stationName)
    with urllib.request.urlopen(base_url + path) as url:
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data

# 서울시 대중교통 보관 분실물 검색
# 습득물분류: 지갑, 쇼핑백, 서류봉투, 가방, 배낭, 핸드폰, 옷, 책, 파일, 기타
# 습득물코드: s1(1~4호선), s2(5~8호선), s3(코레일), s4(9호선)
# Article, station
def Lost_Article():
    key = '4c566371676c64793334654f5a6a7a/'
    Article = urllib.parse.quote('핸드폰')
    SubwayCode = urllib.parse.quote('s1')
    base_url = 'http://openAPI.seoul.go.kr:8088/4c566371676c64793334654f5a6a7a/xml/SearchLostArticleService/1/5/'
    #path = urllib.parse.quote_plus('')
    print(base_url)
    with urllib.request.urlopen(base_url + Article + '/' + SubwayCode) as url:
        #print(url)
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data

#FindStationFirstLast('정왕')
Lost_Article()