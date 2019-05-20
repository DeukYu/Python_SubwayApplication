from tkinter import *
from jsonParsing import FindStation
import folium

class tkSubway:
#    def MapView(self, x, y, Info):
#        map_osm = folium.Map(location=[x, y], zoom_start=13)
#        folium.Marker([x, y], popup=Info).add_to(map_osm)
#        map_osm.save('osm.html')
    def FindStation(self):
        self.frame4.destroy()
        self.frame4 = Frame(self.frame2, bd=2)
        self.frame4.pack(side="right", fill="both", expand=True)
        stationName = self.StationNameEntry.get()
        stationInfoDict = FindStation(stationName)
        totalcount = stationInfoDict['stationList'][0]['totalCount']
        yValue = 10
        Label(self.frame4, text="지하철 역명 : " + stationInfoDict['stationList'][0]['statnNm'] + "(" + stationInfoDict['stationList'][0]['statnNmEng'] + ")").place(x=10, y=yValue)
        yValue += 30
        for i in range(totalcount):
            Label(self.frame4, text="지하철 호선 : " + stationInfoDict['stationList'][i]['subwayNm']).place(x=10, y=yValue)
            yValue += 30
            Label(self.frame4, text="전역 : " + stationInfoDict['stationList'][i]['statnFnm'] + ", 다음역 : " +stationInfoDict['stationList'][i]['statnTnm']).place(x=10, y=yValue)
            yValue += 30
        Label(self.frame4, text="소속 : " + stationInfoDict['stationList'][0]['operPblinstt']).place(x=10, y=yValue)
        yValue += 30
        Label(self.frame4, text="위치 : " + stationInfoDict['stationList'][0]['adresBass']).place(x=10, y=yValue)
        yValue += 30
        Label(self.frame4, text="전화번호 : " + stationInfoDict['stationList'][0]['telno']).place(x=10, y=yValue)
        yValue += 30
#        Button(self.frame4, text="지도보기", command=lambda : self.MapView(stationInfoDict['stationList'][0]['subwayXcnts'],
#                                                                       stationInfoDict['stationList'][0]['subwayYcnts'],
#                                                                       stationInfoDict['stationList'][0]['statnNmEng'])).place(x=10, y=yValue)
    def check(self):
        #print(self.RadioVariety.get())
        self.frame2.destroy()
        self.frame2 = Frame(self.window, bd=2, relief="solid")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        if(self.RadioVariety.get() == 1):
            Label(self.frame2, image=self.Subway).pack()
        if(self.RadioVariety.get() == 2):       #가까운 역 찾기
            pass
        if (self.RadioVariety.get() == 3):      #역 정보 검색
            self.frame3 = Frame(self.frame2, bd=2, relief="solid")
            self.frame3.pack(side="left", fill="both", expand=True)
            self.frame4 = Frame(self.frame2, bd=2)
            self.frame4.pack(side="right", fill="both", expand=True)
            Label(self.frame3, text="역 명 입력").place(x=10, y=10)
            self.StationNameEntry = Entry(self.frame3)
            self.StationNameEntry.place(x=13, y=40, height=20)
            Button(self.frame3, text="확인", command=self.FindStation).place(x=160, y=37)
        if (self.RadioVariety.get() == 4):      #역 구간 정보
            pass
        if (self.RadioVariety.get() == 5):      #분실물 검색
            pass

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600+500+200")
        #window.resizable(False, False)
        frame1 = Frame(self.window, bd=2, relief="solid")
        frame1.pack(side="top", fill="both", expand=False)
        self.frame2 = Frame(self.window, bd=2, relief="solid")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        self.StationNameEntry = Entry(self.frame2)
        Title = PhotoImage(file="source\\Title.png")
        SubTitle = []
        for i in range(5):
            SubTitle.append(PhotoImage(file="source\\Subtitle_0" + str(i + 1) + ".png"))
        self.Subway = PhotoImage(file="source\\Subway.png")
        Label(frame1, image=Title).pack(side=LEFT)
        self.RadioVariety = IntVar()
        self.radio = []
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[0], value=1, variable=self.RadioVariety, indicatoron=0, command=self.check))
        self.radio.append(Radiobutton(frame1, image=SubTitle[1], value=2, variable=self.RadioVariety, indicatoron=0,
                                      command=self.check))
        self.radio.append(Radiobutton(frame1, image=SubTitle[2], value=3, variable=self.RadioVariety, indicatoron=0,
                                      command=self.check))
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[3], value=4, variable=self.RadioVariety, indicatoron=0, command=self.check))
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[4], value=5, variable=self.RadioVariety, indicatoron=0, command=self.check))

        self.radio[0].pack(side=LEFT)
        self.radio[1].pack(side=LEFT)
        self.radio[2].pack(side=LEFT)
        self.radio[3].pack(side=LEFT)
        self.radio[4].pack(side=LEFT)


        self.window.mainloop()
tkSubway()

#test