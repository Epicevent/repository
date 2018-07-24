
import urllib.request
import json    # or `import simplejson as json` if on Python < 2.6

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

if __name__ =="__main__":
    print (XYtoAddrdetailList("125.9057, 37.484451"))
    print (geocode("울릉군"))