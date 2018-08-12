import urllib.request
import requests
import json    # or `import simplejson as json` if on Python < 2.6
import coord
import MapImageProcess

def staticmap(center,level=12,w=640,h=640,baselayer='default',crs='EPSG:4258'):

    '''
    :param center:(XYstring)이미지의 중심 좌표(X좌표, Y좌표)이다. 이 중심 좌표를 기준으로 요청한 w, h 픽셀 크기로 이미지를 생성한다.
    :param level: (integer) 	네이버지도 서비스에 정의되어 있는 줌 레벨이다. 최소1레벨 최대14레벨까지 지원한다.
    :param w: (integer) 가로 이미지 크기(픽셀 단위)이다. 최소 1 ~ 최대 640 픽셀 지원
    :param h: (integer)  세로 이미지 크기(픽셀 단위)이다. 최소 1 ~ 최대 640 픽셀 지원
    :param baselayer:
                       'default' : 일반 지도
                       'satellite' : 위성 지도
                       'bl_vc_bg' : 주기가 없는 배경 지도
    :param crs :
                     1. EPSG:4326 : WGS84 경위도
                     2. NHN:2048 : UTMK
                     3. NHN:128 : 카텍 TM128
                     4. EPSG:4258 : GRS80 경위도
                     5. EPSG:4162 : Bessel 경위도
                     6. EPSG:2096 : Korea East Belt
                     7. EPSG:2097 : Korea Central Belt
                     8. EPSG:2098 : Korea West Belt
                     9. EPSG:3857 or EPSG:900913 : Google Maps
    :return:요청 변수들에 맞게 한 장의 이미지 파일(png나 jpeg)을 반환합니다.
    '''

    client_id = "XORQXLjnF_42QQm3fDA2"
    myURL = 'http://naver.com'
    url = str('https://openapi.naver.com/v1/map/staticmap.bin?clientId='+ client_id
              +'&url='+ myURL
              + '&center='+center
              + '&level='+str(level)
              + '&w='+str(w)+'&h='+str(h)
              +  '&baselayer='+baselayer
              +  '&crs=' +crs
             )
    try:
        response = requests.get(url=url)
    except:
        print('api요청이 응답하지 않습니다.')
    else:
        image_data = response.content
        return image_data



def geocode(addressString):
    obj = dict()
    client_id = "XORQXLjnF_42QQm3fDA2"
    client_secret = "KTrLgc2JfY"
    encText = urllib.parse.quote(addressString)
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(request)

    except:
        print('api요청이 응답하지 않습니다.')
    else :
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            obj = json.loads(response_body.decode('utf-8'))

        else:
            print("Error Code:" + rescode)
    return obj

def displayLevel(level) :
    if level < 1:
        return 1
    elif level > 16:
        return 16
    else:
        return level



def reversegeocode(XYstring):
    obj = dict()
    client_id = "XORQXLjnF_42QQm3fDA2"
    client_secret = "KTrLgc2JfY"
    encText = urllib.parse.quote(XYstring)
    url = "https://openapi.naver.com/v1/map/reversegeocode?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    try:
        response = urllib.request.urlopen(request)
    except:
        print('api요청이 응답하지 않습니다.')
    else:
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            obj = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    finally:
        return obj



def getDetailAddrList (addressString):
    retlist = list()
    obj = geocode(addressString)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    for i in range (0,numItem):
        retlist.append(obj['result']['items'][i]['addrdetail'])
    return retlist


def XYtoAddressList( XYstring ):
    retlist = list()
    obj=reversegeocode(XYstring)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    for i in range (0, numItem) :
        retlist.append(obj['result']['items'][i]['address'])
    return retlist
def XYtoAddrdetailList( XYstring ):
    retlist = list()
    obj=reversegeocode(XYstring)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    for i in range (0, numItem) :
        retlist.append(obj['result']['items'][i]['addrdetail'])
    return retlist


class NaverCoordiNa (coord.CoordiNa):
    """
    상등조건
    Narverstaticapi를 통한 이미지 (640x640)호출을 하였을때
    이미지가 동일해야한다.
    """
    def __init__(self, level, Coordstring):
        super().__init__(Coordstring)
        self.level = level

    def get_magic_int_xy(self,imagesize ="640x640"):
        # (137953280, 105349120, 1)
        # (71303168, 55492608, 2)
        # (36306944, 28631040, 3)
        # (18272256, 14508032, 4)
        # (9152512, 7288832, 5)
        # (4597760, 3658752, 6)
        # (2295296, 1824256, 7)
        # (1155072, 917248, 8)
        # (575616, 457088, 9)
        # (287808, 228864, 10)
        # (143904, 114432, 11)
        # (71952, 57392, 12)
        # (35976, 28744, 13)
        # (17960, 14372, 14)
        # (9008, 7184, 15)
        # (4505, 3586, 16)
        virtual_direction = (1,1)
        xpos = imagesize.find('x')
        width =imagesize[0:xpos]
        height=imagesize[xpos+1:]
        forloopvar = [int(width),int(height)]
        var_naver_coordina = self.getSameNaverCoordiNa(virtual_direction)
        odrXint = var_naver_coordina.Xint
        odrYint = var_naver_coordina.Yint
        standard_for_compare = staticmap(var_naver_coordina.XYstring,level=var_naver_coordina.level)
        virtual_direction = (-1,-1)
        def forloop(tag, dif):
            if tag == 0:
                var_naver_coordina.Xint += dif * virtual_direction[0]
            else:
                var_naver_coordina.Yint += dif * virtual_direction[1]

        dif = int(pow(2, 16 - var_naver_coordina.level))
        for tag in range(0, 2):
            if virtual_direction[tag] == 0:
                continue
            num_image_change_detection = 0
            while num_image_change_detection <forloopvar[tag]:
                forloop(tag, dif)
                var_naver_coordina.adjustXYstring()
                diffMap = staticmap(var_naver_coordina.XYstring, level=var_naver_coordina.level)
                if diff(diffMap, standard_for_compare):
                    print(str(
                             (100*(var_naver_coordina.level-7)/10)
                              +
                              (100/16)*(num_image_change_detection+tag*forloopvar[0])
                              / (forloopvar[0]+forloopvar[1])
                              )
                          + "%\n")  # for test2.py
                    num_image_change_detection += 1
                    standard_for_compare =diffMap
        magicint =(odrXint - var_naver_coordina.Xint,odrYint - var_naver_coordina.Yint)
        return magicint




    def getSameNaverCoordiNa(self, virtual_direction):
        ret_val = NaverCoordiNa(self.level,self.XYstring)
        standardforCompare = staticmap(ret_val.XYstring, level=ret_val.level)

        def forloop(tag, dif):
            if tag == 0:
                ret_val.Xint += dif * virtual_direction[tag]
            else:
                ret_val.Yint += dif * virtual_direction[tag]

        dif =int(pow(2, 16 - ret_val.level))
        for tag in range(0, 2):
            if virtual_direction[tag] == 0:
                continue
            forloop(tag, dif)
            ret_val.adjustXYstring()
            diffMap = staticmap(ret_val.XYstring, level=ret_val.level)
            while not diff(standardforCompare, diffMap):
                forloop(tag, dif)
                ret_val.adjustXYstring()
                diffMap = staticmap(ret_val.XYstring, level=ret_val.level)
            forloop(tag, -dif)
        ret_val.adjustXYstring()
        return ret_val


def diff(mapcontent1,mapcontent2):
    return mapcontent1 != mapcontent2

if __name__ =="__main__":
    print (XYtoAddrdetailList("126.8397859,37.4991205"))
    print (geocode("서울특별시 구로구 오류동 338"))
