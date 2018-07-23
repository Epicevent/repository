
import requests
import math

SidoCodeBook = ({'CODE':11 ,'NAME': '서울특별시'},{'CODE':26 ,'NAME': '부산광역시'},{'CODE':27,'NAME': '대구광역시'},
            {'CODE':28 ,'NAME': '인천광역시'},{'CODE':29 ,'NAME': '광주광역시'},{'CODE':30 ,'NAME': '대전광역시'},
            {'CODE':31, 'NAME': '울산광역시'},{'CODE':36 ,'NAME': '세종특별자치시'},{'CODE':41 ,'NAME': '경기도'},
            {'CODE':42, 'NAME': '강원도'},{'CODE':43 ,'NAME': '충청북도'},{'CODE':44 ,'NAME': '충청남도'},
            {'CODE':45, 'NAME': '전라북도'},{'CODE':46, 'NAME': '전라남도'},{'CODE':47, 'NAME': '경상북도'},
            {'CODE':48, 'NAME': '경상남도'},{'CODE':50, 'NAME': '제주특별자치도'})

def getSidoCode(strSidoName):

    if type(strSidoName) is not str:
         print('매게변수로 문자열을 넣으셔야 합니다. : getSidoCode')
    if type(strSidoName) is int:
        return strSidoName

    for sidoCodeDic in SidoCodeBook:
        if sidoCodeDic['NAME'] == strSidoName:
            return sidoCodeDic['CODE']
    print('정확한 이름을 입력하셔야 합니다.')


def getGuGunListBySidoCode(SidoCode):
    url = 'http://rt.molit.go.kr/new/gis/getGugunListAjax.do?menuGubun=A&gubunCode=LAND&sidoCode='
    url += str(SidoCode)
    response = requests.get(url)
    jsonDic = response.json()
    GuGunList = jsonDic['jsonList']
    return GuGunList

def printAllGuGunNameInGuGunList(GuGunList):
    if type(GuGunList) is not list:
         print('잘못된 매개변수 입니다. list type을 요구합니다. 현재 타입'+ str(type(GuGunList)))
    print(str(len(GuGunList)) + '개의 결과가 있습니다.')
    for GuGunDic in GuGunList:
        print (GuGunDic['NAME'])

def getLawd_cdByNameInGuGunList(GuGunList, Name):
    if type(GuGunList) is not list:
         print('잘못된 매개변수 입니다. list type을 요구합니다. 현재 타입'+ str(type(GuGunList)))
    for GuGunDic in GuGunList:
        if (GuGunDic['NAME'] == Name):
            return GuGunDic['CODE']



def getLawd_cd_byUser():

    MyGuGunList  = getGuGunListBySidoCode(getSidoCode(
    input('서울특별시\n부산광역시\n대구광역시\n인천광역시\n광주광역시\n대전광역시\n울산광역시\n세종특별자치시\n'
          +'경기도\n강원도\n충청북도\n충청남도\n전라북도\n전라남도\n경상북도\n경상남도\n제주특별자치도\n'
          +'검색하려는 행정구역을 정확히 입력하세요 : '
          )))
    print('검색결과(기초자치단체)입니다.\n')
    printAllGuGunNameInGuGunList(MyGuGunList)

    Lawd_Cd = getLawd_cdByNameInGuGunList(MyGuGunList,
                            input('검색결과(기초자치단체)중 하나를 정확히 입력하세요 '))
    print(str(Lawd_Cd))
    return Lawd_Cd

def getSidoList():
    return list(SidoCodeBook)

def codelist(codePartion):
    ret = list()
    if codePartion == 0:
        return ret
    SidoList = getSidoList()
    digits = int(math.log10(codePartion)) + 1
    _5code = int(codePartion*(math.pow(10, 5-digits)))
    sidoPart = int(_5code/1000) * 1000
    for sidoItem in SidoList :
        sidocode = sidoItem['CODE']

        if sidocode*1000 == sidoPart:
            gugunlist =getGuGunListBySidoCode(sidocode)
            for gugunItem in gugunlist:
                ret.append(int(gugunItem['CODE']))



print(codelist(11))