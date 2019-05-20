import urllib.request, json, urllib.parse

#서울시 지하철 역사 정보 조회
def FindStation(stationName):
    base_url = 'http://swopenAPI.seoul.go.kr/api/subway/49556d7755726c6137384e5475776f/json/stationInfo/0/10/'
    path = urllib.parse.quote(stationName)
    with urllib.request.urlopen(base_url + path) as url:
        data = json.loads(url.read().decode('utf-8'))
        print(data)
        return data