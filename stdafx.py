from googleParsing import FindStation
from kakaoParsing import Translation
import pprint

def isKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count+=1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count+=1
    return True if k_count>1 else False

class Rect():
    def __init__(self, posx, posy, sizex, sizey, type):
        self.posX = posx
        self.posY = posy
        self.sizeX = sizex
        self.sizeY = sizey
        self.isGraph = type

    def SetPos(self, posx, posy):
        self.posX = posx
        self.posY = posy
    def SetSize(self, sizex, sizey):
        self.sizeX = sizex
        self.sizeY = sizey
    def SetType(self, type):
        self.isGraph = type

    def Update(self):
        if type == True:
            self.left = self.posX - (self.sizeX / 2)
            self.right = self.posX + (self.sizeX / 2)
            self.top = self.posY - self.sizeY
            self.bottom = self.posY
        else:
            self.left = self.posX - (self.sizeX / 2)
            self.right = self.posX + (self.sizeX / 2)
            self.top = self.posY - (self.sizeY / 2)
            self.bottom = self.posY + (self.sizeY / 2)

def _FindRoute(start, end):
    data = FindStation(start, end)
    #print(data['routes'][0]['legs'])
    startTime = (data['routes'][0]['legs'][0]['departure_time']['text'])
    endTime = (data['routes'][0]['legs'][0]['arrival_time']['text'])
    totalLen = (data['routes'][0]['legs'][0]['distance']['text'])
    totalTime = (data['routes'][0]['legs'][0]['duration']['text'])
    Route = []

    if (data['routes'][0]['legs'][0]['steps'][0]['travel_mode'] == 'TRANSIT'):
        if isKorean(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign']):
            Route = [[[start,
                       Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_stop']['name']),
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name'],
                       "한글",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign'] + " 행 열차",
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['departure_time']['text'] + " ~ " +
                       data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_time']['text'],
                       str(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['num_stops']) + " 정거장"],
                      data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['color']]]

        else:
            Route = [[[start, Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_stop']['name']), data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name'], Translation(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign']) + " 행 열차",data['routes'][0]['legs'][0]['steps'][0]['transit_details']['headsign'] + " 행 열차" , data['routes'][0]['legs'][0]['steps'][0]['transit_details']['departure_time']['text'] + " ~ " + data['routes'][0]['legs'][0]['steps'][0]['transit_details']['arrival_time']['text'], str(data['routes'][0]['legs'][0]['steps'][0]['transit_details']['num_stops']) + " 정거장"], data['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['color']]]
    data2 = data['routes'][0]['legs'][0]['steps'][1:]
    for i in data2:
        if i['travel_mode'] == 'TRANSIT':
            if isKorean(i['transit_details']['headsign']):
                Route.append([[Translation(i['transit_details']['departure_stop']['name']), Translation(i['transit_details']['arrival_stop']['name']), i['transit_details']['line']['short_name'], "한글", i['transit_details']['headsign'] + " 행 열차" , i['transit_details']['departure_time']['text'] + " ~ " + i['transit_details']['arrival_time']['text'], str(i['transit_details']['num_stops']) + " 정거장"], i['transit_details']['line']['color']])
            else:
                Route.append([[Translation(i['transit_details']['departure_stop']['name']), Translation(i['transit_details']['arrival_stop']['name']), i['transit_details']['line']['short_name'], Translation(i['transit_details']['headsign']) + " 행 열차", i['transit_details']['headsign'] + " 행 열차" , i['transit_details']['departure_time']['text'] + " ~ " + i['transit_details']['arrival_time']['text'], str(i['transit_details']['num_stops']) + " 정거장"], i['transit_details']['line']['color']])


    returnData = {'startTime': startTime}
    returnData['endTime'] = endTime
    returnData['totalLen'] = totalLen
    returnData['totalTime'] = totalTime
    returnData['Route'] = Route
    returnData['Size'] = int(returnData['Route'].__len__())

    return returnData