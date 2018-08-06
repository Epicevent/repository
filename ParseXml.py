import xml.etree.ElementTree as ET
import requests
import Lawdcd
import json
from pprint import pprint

lawd_cd = Lawdcd.getLawdcd_By_User()
deal_ymd = input('yyyydd형식으로 조회하고 싶은 달을 입력하시오 '
                     'ex) 201512')
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=nhtTGoiP3P2%2FkkO4i9SnXNBlQOfHzjlUwlClGbvCJuXQt%2BC40F10gmocrV0b%2F9nhhcO%2FSb3kuRkVo%2FSVrzUQew%3D%3D&LAWD_CD='
url += str(lawd_cd) # '11110'
url += '&DEAL_YMD='
url += deal_ymd  # '201512'
response = requests.get(url)
