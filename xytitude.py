import naverapi

def diff(img1, img2):
    im1 = img1.load()
    im2 = img2.load()
    if (img1.size[0] != img2.size[0] or img1.size[1] != img2.size[1]):
        return True

    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):
            if(im1[i,j] != im2[i,j]):
                return True
    return False

class XYcoord:
    EPSILON = pow(10, -7)
    INVSILON = int(pow(10, 7))
    INTEGERPART_FOR_X= 3
    INTEGERPART_FOR_Y = 2

    Xint = 0
    Yint = 0

    XYstring = ""
    def __init__(self, XYstr):
        xstr = XYstr[0:XYstr.index(',')]
        ystr = XYstr[XYstr.index(',') + 1:XYstr.__len__()]
        Xfloat = float (xstr)
        Yfloat = float (ystr)
        self.Xint = int(Xfloat * self.INVSILON)
        self.Yint = int(Yfloat * self.INVSILON)
        self.adjustXYstring()
        if (self.XYstring != XYstr):
            print("[XYcoord Class Warning ] : Input String is Modifiyed  ")
        print(self.XYstring)

    def adjustXYstring(self):
        self.XYstring = (
                str(str(self.Xint)[0:self.INTEGERPART_FOR_X] + '.'
                    + str(self.Xint)[3:]) + ','
                + str(self.Yint)[0:self.INTEGERPART_FOR_Y] + '.' +
                str( self.Yint)[2:])


Coord = XYcoord(" 126.8111197001, 37.4991234")
print(str(Coord.Xint))

print(str(Coord.Xint))
Coord.adjustXYstring()
print(Coord.XYstring)