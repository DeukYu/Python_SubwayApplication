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


def getnum(string):
   tempstr =''
   for i in range(string.__len__()):
       if string[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
           tempstr += string[i]

   return int(tempstr)