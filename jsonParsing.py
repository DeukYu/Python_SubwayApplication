import urllib.request, json, urllib.parse, pprint

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