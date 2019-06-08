import urllib.request, json, urllib.parse, pprint, haversine
from kakaoParsing import FindAddress2, Translation
from stdafx import isKorean, getnum

def FindStation(origin, dest):
    originPos = FindAddress2(origin + "역")
    destPos = FindAddress2(dest + "역")
    originUrl = str(originPos[0]) + ',' + str(originPos[1])
    destUrl = str(destPos[0]) + ',' + str(destPos[1])
    base_url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+ originUrl +'&destination='+ destUrl +'&mode=transit&key=AIzaSyCg0fDlbw8XRm5A29-ETy_Ic2O7fHppdIo'
    with urllib.request.urlopen(base_url) as url:
        data = json.loads(url.read().decode('utf-8'))
        #pprint.pprint(data)
        return data

def _FindRoute(start, end):
    data = FindStation(start, end)
    pprint.pprint(data['routes'][0]['legs'])
    startTime = (data['routes'][0]['legs'][0]['departure_time']['text'])
    endTime = (data['routes'][0]['legs'][0]['arrival_time']['text'])
    totalLen = (data['routes'][0]['legs'][0]['distance']['text'])
    totalTime = (data['routes'][0]['legs'][0]['duration']['text'])
    Route = []

    if (data['routes'][0]['legs'][0]['steps'][0]['travel_mode'] == 'TRANSIT'):
        if isKorean(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign']):
            Route = [[start,
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_stop']['name'],
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name'],
                       "한글",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign'] + " 행 열차",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['departure_time']['text'] + " ~ " +
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_time']['text'],
                       str(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['num_stops']) + " 정거장",
                      data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['color']
                     ]]

        else:
            Route = [[start,
                      data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_stop']['name'],
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name'],
                       Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign']) + " 행 열차",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign'] + " 행 열차" ,
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['departure_time']['text'] + " ~ " + data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_time']['text'],
                       str(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['num_stops']) + " 정거장",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['color'],
                       getnum(data['routes'][0]['legs'][0]['steps'][0]['duration']['text'])
                     ]]
    data2 = data['routes'][0]['legs'][0]['steps'][1:]
    for i in data2:
        if i['travel_mode'] == 'TRANSIT':
            if not isKorean(i['transit_details']['departure_stop']['name']):
                i['transit_details']['departure_stop']['name'] = Translation(i['transit_details']['departure_stop']['name'])
            if not isKorean(i['transit_details']['arrival_stop']['name']):
                i['transit_details']['arrival_stop']['name'] = Translation(i['transit_details']['arrival_stop']['name'])
            if isKorean(i['transit_details']['headsign']):
                Route.append([i['transit_details']['departure_stop']['name'],
                               i['transit_details']['arrival_stop']['name'],
                               i['transit_details']['line']['short_name'],
                               "한글",
                               i['transit_details']['headsign'] + " 행 열차" ,
                               i['transit_details']['departure_time']['text'] + " ~ " + i['transit_details']['arrival_time']['text'],
                               str(i['transit_details']['num_stops']) + " 정거장",
                               i['transit_details']['line']['color'],
                               getnum(i['duration']['text'])
                              ])
            else:
                Route.append([i['transit_details']['departure_stop']['name'],
                               i['transit_details']['arrival_stop']['name'],
                               i['transit_details']['line']['short_name'],
                               Translation(i['transit_details']['headsign']) + " 행 열차",
                               i['transit_details']['headsign'] + " 행 열차" ,
                               i['transit_details']['departure_time']['text'] + " ~ " + i['transit_details']['arrival_time']['text'],
                               str(i['transit_details']['num_stops']) + " 정거장",
                               i['transit_details']['line']['color'],
                               getnum(i['duration']['text'])
                              ])



    returnData = {'startTime': startTime}
    returnData['endTime'] = endTime
    returnData['totalLen'] = totalLen
    returnData['totalTime'] = totalTime
    returnData['Route'] = Route
    returnData['Size'] = int(returnData['Route'].__len__())


    #print("returnData==========")
    #pprint.pprint(returnData)

    return returnData

def FindNearStation(addr):
    temp = FindAddress2(addr)
    y = str(temp[0])
    x = str(temp[1])

    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + y + "," + x +"&radius=5000&type=subway_station&key=AIzaSyCg0fDlbw8XRm5A29-ETy_Ic2O7fHppdIo"
    with urllib.request.urlopen(base_url) as url:
        data = json.loads(url.read().decode('utf-8'))
        #pprint.pprint(data)

    returndata = []
    for i in range(data['results'].__len__()):
        if not data['results'][i]['name'] in returndata[0:-1]:
            if(isKorean(data['results'][i]['name']) or data['results'][i]['name'] == 'Seoul Nat‘l Univ. (Gwanak-gu Office)'):
                returndata.append(["한글",
                                   data['results'][i]['name'],
                                   data['results'][i]['geometry']['location']['lat'],
                                   data['results'][i]['geometry']['location']['lng'],
                                   str(haversine.haversine((temp[0], temp[1]), (data['results'][i]['geometry']['location']['lat'],
                                                                data['results'][i]['geometry']['location']['lng'])) // 0.001),
                                   int(haversine.haversine((temp[0], temp[1]),
                                                       (data['results'][i]['geometry']['location']['lat'],
                                                        data['results'][i]['geometry']['location']['lng'])) / 6.5 * 60)
                                   ])
            else:
                returndata.append([Translation(data['results'][i]['name'] + " station"),
                                   data['results'][i]['name'],
                                   data['results'][i]['geometry']['location']['lat'],
                                   data['results'][i]['geometry']['location']['lng'],
                                   str(haversine.haversine((temp[0], temp[1]), (data['results'][i]['geometry']['location']['lat'],
                                                                data['results'][i]['geometry']['location']['lng'])) // 0.001),
                                   int(haversine.haversine((temp[0], temp[1]),
                                                           (data['results'][i]['geometry']['location']['lat'],
                                                            data['results'][i]['geometry']['location']['lng'])) / 6.5 * 60)
                                   ])
    pprint.pprint(returndata)
    return returndata