from tkinter import *

class tkSubway:
    def check(self):
        print(self.RadioVariety.get())
        self.frame2.destroy()
        self.frame2 = Frame(self.window, bd=2, relief="solid")
        self.frame2.pack(side="bottom", fill="both", expand=True)
        if(self.RadioVariety.get() == 1):
            Label(self.frame2, image=self.Subway).pack()
        if(self.RadioVariety.get() == 2):
            pass
        if (self.RadioVariety.get() == 3):
            pass
        if (self.RadioVariety.get() == 4):
            pass
        if (self.RadioVariety.get() == 5):
            pass

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600+500+200")
        #window.resizable(False, False)
        frame1 = Frame(self.window, bd=2, relief="solid")
        frame1.pack(side="top", fill="both", expand=False)
        self.frame2 = Frame(self.window, bd=2, relief="solid")
        self.frame2.pack(side="bottom", fill="both", expand=True)
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