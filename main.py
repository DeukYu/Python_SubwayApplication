from tkinter import *
import tkinter.messagebox
import tkinter.font
from jsonParsing import FindStation, FindStationFirstLast, Lost_Article
from kakaoParsing import FindAddress2
from googleParsing import _FindRoute, FindNearStation
import webbrowser
from tkinter import ttk
import teller
import noti
import telepot
from datetime import date
from pprint import pprint
import time


host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
port = "587"



import folium

class tkSubway:
    def MapView(self, stationName):
        yx = FindAddress2(stationName + "역")
        map_osm = folium.Map(location=[yx[0], yx[1]], zoom_start=15)
        folium.Marker([yx[0], yx[1]], popup=stationName + "역").add_to(map_osm)
        map_osm.save('osm.html')
        url = 'osm.html'
        webbrowser.open(url)
        #urllib.request.urlretrieve(url, 'osmpng.png')

    def mapviewNear(self, place, placeList):
        placeyx = FindAddress2(place)
        map_osm = folium.Map(location=[placeyx[0], placeyx[1]], zoom_start=14)
        folium.Marker([placeyx[0], placeyx[1]], popup=place).add_to(map_osm)
        for i in placeList:
            folium.Marker([i[2], i[3]], popup=i[1] + " station").add_to(map_osm)
        map_osm.save('osm_small.html')
        url = 'osm_small.html'
        webbrowser.open(url)


    def FirstLastView(self, stationName):
        firstlastDict = FindStationFirstLast(stationName)
        totalCount = firstlastDict['timeTableList'][0]['totalCount']
        totalCountLen = (totalCount + 1) * 20 + 30
        totalCountStr = str(totalCountLen)
        toplevel = Toplevel(self.window)
        toplevel.geometry("450x" + totalCountStr + "+1300+200")
        Label(toplevel, text=stationName + "역 첫차, 막차 정보(평일/토요일/휴일 순)", relief="solid").place(x=10, y=10)
        yValue = 40

        for i in range(totalCount):
            Label(toplevel, text=firstlastDict['timeTableList'][i]['subwayNm']).place(x=10, y=yValue)
            Label(toplevel, text=firstlastDict['timeTableList'][i]['subwayename'] + "방면").place(x=100, y=yValue)
            Label(toplevel, text=firstlastDict['timeTableList'][i]['weekendTranHour']).place(x=250, y=yValue)
            Label(toplevel, text=firstlastDict['timeTableList'][i]['saturdayTranHour']).place(x=300, y=yValue)
            Label(toplevel, text=firstlastDict['timeTableList'][i]['holidayTranHour']).place(x=350, y=yValue)
            yValue += 20

    def SendEmail(self):
        global host, port
        html = ""
        title = str(self.Subject.get())
        senderAddr = str(self.senderAddr.get())
        recipientAddr = "ldy8070@naver.com"
        passwd = str(self.senderPw.get())
        html = str(self.MsgText.get(1.0, tkinter.END))
        print(html)

        import mysmtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart('alternative')

        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        bookPart = MIMEText(html, 'html', _charset='UTF-8')

        msg.attach(bookPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        tkinter.messagebox.showinfo("Gmail보내기", "성공적으로 보냈습니다.")
        self.senderAddr.delete(0, self.senderAddr.index(END))
        self.senderPw.delete(0, self.senderPw.index(END))
        self.Subject.delete(0, self.Subject.index(END))
        self.MsgText.delete(1.0, tkinter.END)

    def sendMain(self):
        self.EmailPhoto = PhotoImage(file="source\\penguin.png")
        self.SendPhoto = PhotoImage(file="source\\sendmail.png")
        self.EmailFrame = Frame(self.frame2, bd=2, bg="#e8f1f8")
        self.EmailFrame.pack(side="left", fill="both", expand=True)

        Label(self.EmailFrame, text="Gmail ID", font=self.font, bg="#e8f1f8").place(x=10, y=10)
        self.senderAddr = Entry(self.EmailFrame, width=40, bg="#c7d3d9")
        self.senderAddr.place(x=95, y=15)

        Label(self.EmailFrame, text="Gmail PW", font=self.font, bg="#e8f1f8").place(x=10, y=45)
        self.senderPw = Entry(self.EmailFrame, width=40, bg="#c7d3d9")
        self.senderPw.place(x=95, y=50)

        Label(self.EmailFrame, text="Title", font=self.font, bg="#e8f1f8").place(x=10, y=80)
        self.Subject = Entry(self.EmailFrame, width=40, bg="#c7d3d9")
        self.Subject.place(x=95, y=85)

        Label(self.EmailFrame, text="내용", font=self.font, bg="#e8f1f8").place(x=10, y=115)
        self.MsgText = Text(self.EmailFrame, width=56, bg="#c7d3d9")
        self.MsgText.place(x=95, y=120)
        Button(self.EmailFrame, image=self.SendPhoto, command=self.SendEmail).place(x=385,y=9)

        imageLabel = Label(self.EmailFrame, image=self.EmailPhoto, bg="#e8f1f8")
        imageLabel.place(x=530, y= 10)

    def FindStation(self):
        self.frame4.destroy()
        self.frame4 = Frame(self.frame2, bd=2, bg="#e8f1f8")
        self.frame4.pack(side="right", fill="both", expand=True)
        self.frame6.destroy()
        self.frame6 = Frame(self.frame3, bd=2, bg="#e8f1f8")
        self.frame6.pack(side="bottom", fill="both", expand=True)
        self.mapview = PhotoImage(file="source\\mapview.png")


        stationName = self.StationNameEntry.get()
        stationInfoDict = FindStation(stationName)
        totalcount = stationInfoDict['stationList'][0]['totalCount']
        yValue = 10
        Label(self.frame4, bg="#e8f1f8", text="지하철 역명 : " + stationInfoDict['stationList'][0]['statnNm'] + "(" + stationInfoDict['stationList'][0]['statnNmEng'] + ")", font=self.font2).place(x=10, y=yValue)
        yValue += 30
        for i in range(totalcount):
            Label(self.frame4, bg="#e8f1f8", text="지하철 호선 : " + stationInfoDict['stationList'][i]['subwayNm'], font=self.font2).place(x=10, y=yValue)
            yValue += 30
            Label(self.frame4, bg="#e8f1f8", text="전역 : " + stationInfoDict['stationList'][i]['statnFnm'] + ", 다음역 : " +stationInfoDict['stationList'][i]['statnTnm'], font=self.font2).place(x=10, y=yValue)
            yValue += 30
        Label(self.frame4, bg="#e8f1f8", text="소속 : " + stationInfoDict['stationList'][0]['operPblinstt'], font=self.font2).place(x=10, y=yValue)
        yValue += 30
        Label(self.frame4, bg="#e8f1f8", text="위치 : " + stationInfoDict['stationList'][0]['adresBass'], font=self.font2).place(x=10, y=yValue)
        yValue += 30
        Label(self.frame4, bg="#e8f1f8", text="전화번호 : " + stationInfoDict['stationList'][0]['telno'], font=self.font2).place(x=10, y=yValue)
        yValue += 30

        scrollbar = tkinter.Scrollbar(self.frame6)
        scrollbar.place(x=390, y=40, height=340)


        self.FistLastView_ListBox = tkinter.Listbox(self.frame6, selectmode='extended', yscrollcommand=scrollbar.set,
                                                    height=16, width=54, bg="#c7d3d9", font=self.font2)
        self.FistLastView_ListBox.place(x=10, y=40)

        scrollbar["command"] = self.FistLastView_ListBox.yview

        #self.FistLastView_ListBox.insert(0, stationName + "역 첫차, 막차 정보(평일/토요일/휴일 순)")
        #Label(toplevel, text=stationName + "역 첫차, 막차 정보(평일/토요일/휴일 순)", relief="solid").place(x=10, y=10)
        firstlastDict = FindStationFirstLast(stationName)
        totalCount = firstlastDict['timeTableList'][0]['totalCount']

        for i in range(totalCount):
            self.FistLastView_ListBox.insert(i, firstlastDict['timeTableList'][i]['subwayNm'] + "       " +
                                             firstlastDict['timeTableList'][i]['subwayename'] + "방면" + "  (  " +
                                             firstlastDict['timeTableList'][i]['weekendTranHour'] + "    /   " +
                                             firstlastDict['timeTableList'][i]['saturdayTranHour'] + "   /   " +
                                             firstlastDict['timeTableList'][i]['holidayTranHour'] + "  )"
                                             )


        Label(self.frame6, text=stationName + "역 첫차, 막차 정보(평일/토요일/휴일 순) 정보", font=self.font, bg="#e8f1f8").place(x=10, y=0)

        Button(self.frame4, image=self.mapview, command=lambda: self.MapView(stationName)).place(x=10, y=yValue)
        #FindStationUseRate(stationName)
    def FindRoute(self):
        if self.frames:
            for i in self.frames:
                i.destroy()
        startName = self.StartStationEntry.get()
        endName = self.EndStationEntry.get()
        data = _FindRoute(startName, endName)
        Label(self.frame6, text="출발 시간 " + data['startTime'], bg="#e8f1f8",font=self.font2).place(x=10,y=10)
        Label(self.frame6, text="도착 시간 " + data['endTime'], bg="#e8f1f8",font=self.font2).place(x=10,y=40)
        Label(self.frame6, text="이동 거리 " + data['totalLen'], bg="#e8f1f8",font=self.font2).place(x=10, y=70)
        Label(self.frame6, text="이동 시간 " + data['totalTime'], bg="#e8f1f8",font=self.font2).place(x=10, y=100)
        route = data['Route']
        print(route)
        tempsize = []
        tempfullsize = 0
        for i in range(data['Size']):
            tempsize.append(data['Route'][i][-1])
            tempfullsize += data['Route'][i][-1]
        for i in range(tempsize.__len__()):
            tempsize[i] = tempsize[i] / tempfullsize
        print(tempsize)
        size = data['Size']
        ysize = []
        for i in range(size):
            if int(400 * tempsize[i]) < 90:
                ysize.append(90)
            else:
                ysize.append(int(400 * tempsize[i]))
        self.frames = []
        for i in range(size):
            frame = Frame(self.frame4, bd=2, height=ysize[i], bg="#e8f1f8")
            self.frames.append(frame)

        for i in self.frames:
            i.pack(side="top", fill="both")
        frame = Frame(self.frame4, bd=2, bg="#e8f1f8")
        self.frames.append(frame)
        self.frames[-1].pack(side="top", fill="both", expand=True)

        for i in range(size):
            Label(self.frames[i], text=route[i][0], bg="#e8f1f8",font=self.font2).place(x=10, y=0)
            Label(self.frames[i], bg=route[i][-2], width=5, height = ysize[i]//10).place(x=10, y=20)
        Label(self.frames[-1], text=route[-1][1], bg="#e8f1f8",font=self.font2).place(x=10, y=0)

        for i in range(size):
            if(route[i][3] == "한글"):
                Label(self.frames[i], text=route[i][2] + ' ' + route[i][4], bg="#e8f1f8",font=self.font2).place(x=60, y=ysize[i]//2 - 30)
            else:
                Label(self.frames[i], text=route[i][2] + ' ' + route[i][3] + "(" + route[i][4] + ")", bg="#e8f1f8",font=self.font2).place(x=60, y=ysize[i]//2 - 30)
            Label(self.frames[i], text=route[i][5], bg="#e8f1f8",font=self.font2).place(x=60, y=ysize[i]//2 - 10)
            Label(self.frames[i], text=route[i][6], bg="#e8f1f8",font=self.font2).place(x=60, y=ysize[i]//2 + 10)

    # 습득물분류: 지갑, 쇼핑백, 서류봉투, 가방, 배낭, 핸드폰, 옷, 책, 파일, 기타
    # 습득물코드: s1(1~4호선), s2(5~8호선), s3(코레일), s4(9호선)
    def ParsingArticle(self):
        self.listbox.delete(0, END)
        if '1~4호선' == self.Combobox2.get():
            Sub_Code = str('s1')
        elif '5~8호선' == self.Combobox2.get():
            Sub_Code = str('s2')
        elif '코레일' == self.Combobox2.get():
            Sub_Code = str('s3')
        elif '9호선' == self.Combobox2.get():
            Sub_Code = str('s4')

        print(Sub_Code)
        LA_Data = Lost_Article(self.Combobox1.get(), Sub_Code)
        totalCount = len(LA_Data['SearchLostArticleService']['row'])
        print(totalCount)

        for i in range(0, totalCount):
            #self.listbox.insert(i, '분실물 ID: ' + LA_Data['SearchLostArticleService']['row'][i]['ID'])
            self.listbox.insert(i * 5, "================================ 분실물 =================================")
            self.listbox.insert((i * 5) + 1, '                          습득 날짜 : ' + LA_Data['SearchLostArticleService']['row'][i]['GET_DATE'])
            self.listbox.insert((i * 5) + 2, '                          습득한 역 ' + LA_Data['SearchLostArticleService']['row'][i]['TAKE_PLACE'])
            self.listbox.insert((i * 5) + 3, '                          습득 물품 ' + LA_Data['SearchLostArticleService']['row'][i]['GET_NAME'])
            self.listbox.insert((i * 5) + 4, "")

    def LostArticle(self):
        self.ArticleFrame1 = Frame(self.frame2, bd=2, relief="solid", height=50, bg="#e8f1f8")
        self.ArticleFrame1.pack(side="top", fill="both")
        self.ArticleFrame2 = Frame(self.frame2, bd=2, relief="solid", bg="#e8f1f8")
        self.ArticleFrame2.pack(side="bottom", fill="both", expand=True)

        self.str1 = StringVar()
        self.str2 = StringVar()

        self.Combobox1 = ttk.Combobox(self.ArticleFrame1, textvariable=self.str1, width=20, font=self.font2)
        self.Combobox1['value'] = ('지갑', '쇼핑백', '서류봉투', '가방', '배낭', '핸드폰', '옷', '책', '파일', '기타')
        self.Combobox1.current(0)
        self.Combobox1.place(x=200,y=13)
        self.Combobox2 = ttk.Combobox(self.ArticleFrame1, textvariable=self.str2, width=20, font=self.font2)
        self.Combobox2['value'] = ('1~4호선', '5~8호선', '코레일', '9호선')
        self.Combobox2.current(0)
        self.Combobox2.place(x=365,y=13)

        scrollbar = tkinter.Scrollbar(self.ArticleFrame2)
        scrollbar.place(x=699,y=15, height=420)
        self.listbox = tkinter.Listbox(self.ArticleFrame2, selectmode='extended', yscrollcommand=scrollbar.set,
                                       height=20, width=80, bg="#c7d3d9", font=self.font2)
        self.listbox.place(x=135,y=15)

        scrollbar["command"] = self.listbox.yview

        Button(self.ArticleFrame1, image=self.search, command=self.ParsingArticle).place(x=530,y=5)

    def NearBySearch(self):
        self.listbox.delete(0, END)
        Place = self.PlaceEntry.get()
        placeList = FindNearStation(Place)
        for i in range(placeList.__len__()):
            if(placeList[i][0] == '한글'):
                self.listbox.insert(i, placeList[i][1] + '  (' + str(placeList[i][2]) + ', ' + str(placeList[i][3]) + ')  거리 : ' + placeList[i][4] + ' m, 걸어서 ' + str(placeList[i][5]) +'분')
            else:
                self.listbox.insert(i, placeList[i][0] + '(' + placeList[i][1] + ')  (' + str(placeList[i][2]) + ', ' + str(placeList[i][3]) + ')  거리 : ' + placeList[i][4] + ' m, 걸어서 ' + str(placeList[i][5]) +'분')
        Button(self.frame2, image=self.smallmapview, command=lambda: self.mapviewNear(Place, placeList)).place(x=620, y=23)


    def check(self):
        #print(self.RadioVariety.get())
        self.frame2.destroy()
        self.frame2 = Frame(self.window, bd=2, relief="solid", bg="#e8f1f8")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        if(self.RadioVariety.get() == 1):
            Label(self.frame2, image=self.Subway).pack()
        if(self.RadioVariety.get() == 2):       #가까운 역 찾기
            Label(self.frame2, text="위치 입력", font=self.font, bg="#e8f1f8").place(x=10, y=10)
            self.PlaceEntry = Entry(self.frame2, bg="#c7d3d9")
            self.PlaceEntry.place(x=13, y=40)
            Button(self.frame2, image=self.search, command=self.NearBySearch).place(x=160, y=24)
            scrollbar = tkinter.Scrollbar(self.frame2)
            scrollbar.place(x=715, y=70, height=400)
            self.listbox = tkinter.Listbox(self.frame2, selectmode='extended', yscrollcommand=scrollbar.set,
                                           height=19, width=100, bg="#c7d3d9",font=self.font2)
            self.listbox.place(x=10, y=70)
            scrollbar["command"] = self.listbox.yview

        if (self.RadioVariety.get() == 3):      #역 정보 검색
            self.frame3 = Frame(self.frame2, bd=2, bg="#e8f1f8")
            self.frame3.pack(side="left", fill="both", expand=True)
            self.frame4 = Frame(self.frame2, bd=2, bg="#e8f1f8")
            self.frame4.pack(side="right", fill="both", expand=True)
            self.frame5 = Frame(self.frame3, bd=2, height=100, bg="#e8f1f8")
            self.frame5.pack(side="top", fill="both")
            self.frame6 = Frame(self.frame3, bd=2, bg="#e8f1f8")
            self.frame6.pack(side="bottom", fill="both", expand=True)
            Label(self.frame5, text="역 명 입력", font=self.font, bg="#e8f1f8").place(x=10, y=10)
            self.StationNameEntry = Entry(self.frame5, bg="#c7d3d9")
            self.StationNameEntry.place(x=13, y=40)
            Button(self.frame5, image=self.search, command=self.FindStation).place(x=160, y=24)
        if (self.RadioVariety.get() == 4):      #역 구간 정보
            self.frame3=Frame(self.frame2, bd=2,width=300, bg="#e8f1f8")
            self.frame3.pack(side="left", fill="both")
            self.frame4 = Frame(self.frame2, bd=2, bg="#e8f1f8")
            self.frame4.pack(side="right", fill="both", expand=True)
            self.frame5 = Frame(self.frame3, bd=2,width=300,height=180, bg="#e8f1f8")
            self.frame5.pack(side="top", fill="both")
            self.frame6 = Frame(self.frame3, bd=2,width=300, bg="#e8f1f8")
            self.frame6.pack(side="bottom", fill="both", expand=True)
            self.frames = []
            Label(self.frame5, text="출발역 입력", font=self.font, bg="#e8f1f8").place(x=10, y=10)
            self.StartStationEntry = Entry(self.frame5, bg="#c7d3d9")
            self.StartStationEntry.place(x=13, y=40)
            Label(self.frame5, text="도착역 입력", font=self.font, bg="#e8f1f8").place(x=10, y=60)
            self.EndStationEntry = Entry(self.frame5, bg="#c7d3d9")
            self.EndStationEntry.place(x=13, y=90)
            Button(self.frame5, image=self.search, command=self.FindRoute).place(x=160, y=72)

        if (self.RadioVariety.get() == 5):      #분실물 검색
            self.LostArticle()
        if (self.RadioVariety.get() == 6):      #G-mail
            self.sendMain()
            pass

    def __init__(self):
        self.window = Tk()
        self.window.geometry("850x600+500+200")
        self.window.resizable(False, False)
        self.font = tkinter.font.Font(self.window, family="KoPubWorld돋움체_Pro Bold",weight="bold", size=12)
        self.font2 = tkinter.font.Font(self.window, family="KoPubWorld돋움체_Pro Bold", size=10)
        frame1 = Frame(self.window, bd=2, relief="solid", bg="#c7d3d9")
        frame1.pack(side="top", fill="both", expand=False)
        self.frame2 = Frame(self.window, bd=2, relief="solid", bg="#e8f1f8")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        self.StationNameEntry = Entry(self.frame2)
        Title = PhotoImage(file="source\\Title.png")
        SubTitle = []
        for i in range(6):
            SubTitle.append(PhotoImage(file="source\\Subtitle_0" + str(i + 1) + ".png"))
        self.Subway = PhotoImage(file="source\\Subway.png")
        self.search = PhotoImage(file="source\\search.png")
        self.smallmapview = PhotoImage(file="source\\smallmapview.png")
        Label(frame1, image=Title).pack(side=LEFT)
        self.RadioVariety = IntVar()
        self.radio = []
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[0], value=1, variable=self.RadioVariety, indicatoron=0, command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))
        self.radio.append(Radiobutton(frame1, image=SubTitle[1], value=2, variable=self.RadioVariety, indicatoron=0,
                                      command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))
        self.radio.append(Radiobutton(frame1, image=SubTitle[2], value=3, variable=self.RadioVariety, indicatoron=0,
                                      command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[3], value=4, variable=self.RadioVariety, indicatoron=0, command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[4], value=5, variable=self.RadioVariety, indicatoron=0, command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[5], value=6, variable=self.RadioVariety, indicatoron=0, command=self.check, bg="#c7d3d9", selectcolor="#dde9ef"))

        self.radio[0].place(x=210,y=22)
        self.radio[1].place(x=315,y=22)
        self.radio[2].place(x=420,y=22)
        self.radio[3].place(x=525,y=22)
        self.radio[4].place(x=630,y=22)
        self.radio[5].place(x=735,y=22)

        # 텔레그램 봇
        today = date.today()
        current_month = today.strftime('%Y%m')

        print('[', today, ']received token :', noti.TOKEN)

        bot = telepot.Bot(noti.TOKEN)
        pprint(bot.getMe())

        bot.message_loop(teller.handle)

        print('Listening...')

        self.window.mainloop()
tkSubway()

