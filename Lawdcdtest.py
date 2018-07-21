
import requests

def getSidoCode(strSidoName):

    if type(strSidoName) is not str:
         print('매게변수로 문자열을 넣으셔야 합니다. : getSidoCode')
    if type(strSidoName) is int:
        return strSidoName

    # 서울특별시 11
    # 부산광역시 26
    # 대구광역시 27
    # 인천광역시 28
    # 광주광역시 29
    # 대전광역시 30
    # 울산광역시 31
    # 세종특별자치시 36

    if strSidoName == '서울특별시':
        return 11
    if strSidoName == '부산광역시':
        return 26
    if strSidoName == '대구광역시':
        return 27
    if strSidoName == '인천광역시':
        return 28
    if strSidoName == '광주광역시':
        return 29
    if strSidoName == '대전광역시':
        return 30
    if strSidoName == '울산광역시':
        return 31
    if strSidoName == '세종특별자치시':
        return 36


    # 경기도 41
    # 강원도 42
    # 충청북도 43
    # 충청남도 44
    # 전라북도 45
    # 전라남도 46
    # 경상북도 47
    # 경상남도 48
    # 제주특별자치도 50
    if strSidoName == '경기도':
        return 41
    if strSidoName == '강원도':
        return 42
    if strSidoName == '충청북도':
        return 43
    if strSidoName == '충청남도':
        return 44
    if strSidoName == '전라북도':
        return 45
    if strSidoName == '전라남도':
        return 46
    if strSidoName == '경상북도':
        return 47
    if strSidoName == '경상남도':
        return 48
    if strSidoName == '제주특별자치도':
        return 50
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

