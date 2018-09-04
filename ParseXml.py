import xml.etree.ElementTree as ET
import requests
import Lawdcd
import naverapi
import json
from pprint import pprint

lawd_cd = 11440 # Lawdcd.getLawdcd_By_User()
deal_ymd = 201210#input('yyyydd형식으로 조회하고 싶은 달을 입력하시오 '
            #         'ex) 201512')
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=nhtTGoiP3P2%2FkkO4i9SnXNBlQOfHzjlUwlClGbvCJuXQt%2BC40F10gmocrV0b%2F9nhhcO%2FSb3kuRkVo%2FSVrzUQew%3D%3D&LAWD_CD='
url += str(lawd_cd) # '11110'
url += '&DEAL_YMD='
url += str(deal_ymd)  # '201512'
response = requests.get(url)
xmlstring=str(response.text)

# exmaple : for coding
# content = '<?xml version="1.0" encoding="iso-8859-1"?><test><Users><fun25><limits><total>0KiB</total><kbps>0</kbps><rps>0</rps><connections>0</connections></limits><usages><total>16738211KiB</total><kbps>237.15</kbps><rps>5.40</rps><connections>0</connections></usages><time_to_refresh>never</time_to_refresh><limit_exceeded_URL>none</limit_exceeded_URL></fun25></Users></test>'
# root = ET.fromstring(content)
# print(root.find("Users").find("fun25").find("usages").find("total").text)

itemlist = ET.fromstring(xmlstring).find("body").find("items").findall("item")
for item in itemlist:
    print(item.find("아파트").text,end=" ")
    print("의 주소는 다음과 같습니다")
    addrstring = Lawdcd.lawcd_to_addrstring(str(lawd_cd)) + item.find("법정동").text + " " +item.find("지번").text
    print(addrstring)
    print("XY 위치는 다음과 같습니다. ")
    print(naverapi.geocode(addrstring))
    print("",end="\n\n")




