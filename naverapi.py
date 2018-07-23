
import urllib.request
import json    # or `import simplejson as json` if on Python < 2.6


def reversegeocode(XYstring):
    client_id = "XORQXLjnF_42QQm3fDA2"
    client_secret = "KTrLgc2JfY"
    encText = urllib.parse.quote(XYstring)
    url = "https://openapi.naver.com/v1/map/reversegeocode?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        obj = json.loads( response_body.decode('utf-8'))
        return (obj['result']['items'][0]['address'])
    else:
        print("Error Code:" + rescode)
print(reversegeocode("127.1141382,36.3599968"))