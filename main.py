from tkinter import *
import tkinter.messagebox
from jsonParsing import FindStation
import mimetypes


host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
port = "587"

import folium

class tkSubway:
#    def MapView(self, x, y, Info):
#        map_osm = folium.Map(location=[x, y], zoom_start=13)
#        folium.Marker([x, y], popup=Info).add_to(map_osm)
#        map_osm.save('osm.html')
    def SendEmail(self):
        global host, port
        html = ""
        title = str(self.Subject.get())
        senderAddr = str(self.senderAddr.get())
        recipientAddr = "ldy8070@naver.com"
        passwd = str(self.senderPw.get())
        html = str(self.MsgText.get())

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
        pass
    def sendMain(self):
        self.EmailFrame = Frame(self.frame2, bd=2)
        self.EmailFrame.pack(side="left", fill="both", expand=True)

        Label(self.EmailFrame, text="Gmail ID: ").pack()
        self.senderAddr = Entry(self.EmailFrame)
        self.senderAddr.pack()

        Label(self.EmailFrame, text="Gmail PW: ").pack()
        self.senderPw = Entry(self.EmailFrame)
        self.senderPw.pack()

        Label(self.EmailFrame, text="제목").pack()
        self.Subject = Entry(self.EmailFrame)
        self.Subject.pack()

        Label(self.EmailFrame, text="내용").pack()
        self.MsgText = Entry(self.EmailFrame)
        self.MsgText.pack()
        Button(self.EmailFrame, text="보내기", command=self.SendEmail).pack()


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
        if (self.RadioVariety.get() == 6):      #G-mail
            self.sendMain()
            pass

    def __init__(self):
        self.window = Tk()
        self.window.geometry("850x600+500+200")
        #window.resizable(False, False)
        frame1 = Frame(self.window, bd=2, relief="solid")
        frame1.pack(side="top", fill="both", expand=False)
        self.frame2 = Frame(self.window, bd=2, relief="solid")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        self.StationNameEntry = Entry(self.frame2)
        Title = PhotoImage(file="source\\Title.png")
        SubTitle = []
        for i in range(6):
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
        self.radio.append(
            Radiobutton(frame1, image=SubTitle[5], value=6, variable=self.RadioVariety, indicatoron=0, command=self.check))

        self.radio[0].pack(side=LEFT)
        self.radio[1].pack(side=LEFT)
        self.radio[2].pack(side=LEFT)
        self.radio[3].pack(side=LEFT)
        self.radio[4].pack(side=LEFT)
        self.radio[5].pack(side=LEFT)


        self.window.mainloop()
tkSubway()

#test