
class CoordiNa:
    '''
    CoordiNa는 위경도 좌표체계의 상등조건을 추가하기 위해
    만든 것입니다.

    상등조건
    Xint와 Yint가 동일해야 합니다.


    '''
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
        Yfloat =    float (ystr)
        self.Xint = int(Xfloat * self.INVSILON)
        self.Yint = int(Yfloat * self.INVSILON)
        self.adjustXYstring()




    def adjustXYstring(self):
        self.XYstring = (
                str(str(self.Xint)[0:self.INTEGERPART_FOR_X] + '.'
                + str(self.Xint)[3:]) + ','
                + str(self.Yint)[0:self.INTEGERPART_FOR_Y] + '.' +
                str( self.Yint)[2:])



if __name__ == '__main__':
    Coord = CoordiNa(" 126.8111197001, 37.4991234")
    print(str(Coord.Xint))
    print(str(Coord.Xint))
    Coord.adjustXYstring()
    print(Coord.XYstring)