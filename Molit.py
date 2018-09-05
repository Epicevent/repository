import xml.etree.ElementTree as ET
import requests
import Lawdcd
import naverapi
import json
from pprint import pprint


def get_apart_real_trade_list(str_lawdcd, str_deal_ymd):
    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
    url += '?serviceKey=nhtTGoiP3P2%2FkkO4i9SnXNBlQOfHzjlUwlClGbvCJuXQt%2BC40F10gmocrV0b%2F9nhhcO%2FSb3kuRkVo%2FSVrzUQew%3D%3D&LAWD_CD='
    url += str(str_lawdcd) # '11110'
    url += '&DEAL_YMD='
    url += str(str_deal_ymd)  # '201512'
    print(url)
    response = requests.get(url)
    xmlstring=str(response.text)
    itemlist = ET.fromstring(xmlstring).find("body").find("items").findall("item")
    return itemlist


def print_apart_real_trade_list(apart_list):
    for item in apart_list:
        str_lawd_cd = item.find("지역코드").text
        addrstring = Lawdcd.lawcd_to_addrstring(str_lawd_cd) + item.find("법정동").text + " " +item.find("지번").text
        print(addrstring, end=" ")
        print( item.find( "아파트" ).text)
        XYstring =(str(naverapi.geocode(addrstring)['result']['items'][0]['point']['x'])
                 + ', '
                 + str(naverapi.geocode(addrstring)['result']['items'][0]['point']['y']))
        print(XYstring,end="\n\n")

if __name__ == '__main__':
    print_apart_real_trade_list(get_apart_real_trade_list('11140','201808'))


