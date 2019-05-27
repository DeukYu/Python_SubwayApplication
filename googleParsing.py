import urllib.request, json, urllib.parse, pprint
from kakaoParsing import FindAddress2, Translation

def FindStation(origin, dest):
    originPos = FindAddress2(origin + "역")
    destPos = FindAddress2(dest + "역")
    originUrl = str(originPos[0]) + ',' + str(originPos[1])
    destUrl = str(destPos[0]) + ',' + str(destPos[1])
    base_url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+ originUrl +'&destination='+ destUrl +'&mode=transit&key=AIzaSyCg0fDlbw8XRm5A29-ETy_Ic2O7fHppdIo'
    with urllib.request.urlopen(base_url) as url:
        data = json.loads(url.read().decode('utf-8'))
        pprint.pprint(data)
        return data


#data = FindStation("병점", "여수")
#print(data['routes'][0]['legs'])
#print(data['routes'][0]['legs'][0]['departure_time']['text'])
#print(data['routes'][0]['legs'][0]['arrival_time']['text'])
#print(data['routes'][0]['legs'][0]['distance']['text'])
#print(data['routes'][0]['legs'][0]['duration']['text'])
#pprint.pprint(data['routes'][0]['legs'][0]['steps'])
#
#print()
#print("출발 시간 : " + data['routes'][0]['legs'][0]['departure_time']['text'])
#print("도착 시간 : " + data['routes'][0]['legs'][0]['arrival_time']['text'])
#print("이동 거리 : " +data['routes'][0]['legs'][0]['distance']['text'])
#print("이동 시간 : " +data['routes'][0]['legs'][0]['duration']['text'])
#print()
#print("이동 경로")
#if(data['routes'][0]['legs'][0]['steps'][0]['travel_mode'] == 'TRANSIT'):
#    print("시작역에서 " + Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_stop']['name']) + "까지 " + data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name'] + " " + Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign']) + "행 열차 " + data['routes'][0]['legs'][0]['steps'][0]['transit_details']['departure_time']['text'] + " ~ " + data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_time']['text'] +", 지하철" + str(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['num_stops']) + " 정거장")
#
#data2 = data['routes'][0]['legs'][0]['steps'][1:]
##print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
##pprint.pprint(data2)
#
#
#for i in data2:
#    if i['travel_mode'] == 'TRANSIT':
#        print(Translation(i['transit_details']['departure_stop']['name']) + "에서 " + Translation(i['transit_details']['arrival_stop']['name']) + "까지 " + i['transit_details']['line']['short_name'] + " " + Translation(i['transit_details']['headsign']) + "행 열차 " + i['transit_details']['departure_time']['text'] + " ~ " + i['transit_details']['arrival_time']['text'] + ", 지하철" + str(i['transit_details']['num_stops']) + " 정거장")
#    elif i['travel_mode'] == 'WALKING':
#        print("환승")