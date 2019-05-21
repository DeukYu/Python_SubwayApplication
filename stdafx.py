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