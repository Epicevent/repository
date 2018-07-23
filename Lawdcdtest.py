
import requests
import math
import naverapi
import json

SidoCodeBook = ({'CODE':11 ,'NAME': '서울특별시'},{'CODE':26 ,'NAME': '부산광역시'},{'CODE':27,'NAME': '대구광역시'},
            {'CODE':28 ,'NAME': '인천광역시'},{'CODE':29 ,'NAME': '광주광역시'},{'CODE':30 ,'NAME': '대전광역시'},
            {'CODE':31, 'NAME': '울산광역시'},{'CODE':36 ,'NAME': '세종특별자치시'},{'CODE':41 ,'NAME': '경기도'},
            {'CODE':42, 'NAME': '강원도'},{'CODE':43 ,'NAME': '충청북도'},{'CODE':44 ,'NAME': '충청남도'},
            {'CODE':45, 'NAME': '전라북도'},{'CODE':46, 'NAME': '전라남도'},{'CODE':47, 'NAME': '경상북도'},
            {'CODE':48, 'NAME': '경상남도'},{'CODE':50, 'NAME': '제주특별자치도'})

def getSidoName(sidoCode):
    for sidoCodeDic in SidoCodeBook:
        if sidoCodeDic['CODE'] == sidoCode:
            return sidoCodeDic['NAME']
    print('존재하지 않는 코드입니다.')
    return '0'
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
    # if GuGunList
    if len(GuGunList)==1:
       return GuGunList[0]['CODE']

    for GuGunDic in GuGunList:
        if (GuGunDic['NAME'] == Name):
            return GuGunDic['CODE']
    return 'NORESULT'


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

def naverGugunNameToRtGugunName (GugunName):
    #청주시 상당구 -> 청주상당구
    index = GugunName.find(' ')
    if index == -1:
        return GugunName

    if GugunName[index -1] == "시" and index>1:
        return GugunName[0:index-1] + GugunName[index+1:len(GugunName)]
    else:
        return GugunName[0:index] + GugunName[index+1:len(GugunName)]
def getSidoList():
    return list(SidoCodeBook)

def codelist(sidocode):
    ret = list()
    SidoList = getSidoList()
    for sidoItem in SidoList :
        if sidocode ==sidoItem['CODE'] :
            gugunlist =getGuGunListBySidoCode(sidocode)
            for gugunItem in gugunlist:
                ret.append(int(gugunItem['CODE']))
            break
    return ret

def addrlist(sidocode):
    ret = list()
    SidoList = getSidoList()
    for sidoItem in SidoList:
        if sidocode == sidoItem['CODE']:
            gugunlist = getGuGunListBySidoCode(sidocode)
            for gugunItem in gugunlist:
                ret.append(sidoItem['NAME']+' '+gugunItem['NAME'])
    return ret


def getAllGuGunList():
    gugunList = list()
    for sidoCodeDic in SidoCodeBook:
        gugunList = gugunList + (getGuGunListBySidoCode(sidoCodeDic['CODE']))
    return gugunList


def getLawdcdListByXY(XYstring):
    retList= list()
    addrList = naverapi.XYtoAddressList(XYstring)
    if len(addrList) == 0 :
        print('주소를 지정할 수 없는 위치입니다. (대한민국내부인지 확인하세요)')
        return  retList
    detailAddrList = naverapi.AddressSearch(addrList[0])
    for detailAddr in detailAddrList:
        sidocode = getSidoCode(detailAddr['sido'])
        Mygugunlist = getGuGunListBySidoCode(sidocode)
        GugunName = naverGugunNameToRtGugunName(detailAddr['sigugun'])
        lawdcd =getLawd_cdByNameInGuGunList(Mygugunlist,GugunName)
        retList.append(lawdcd)
    return retList

def searchLawdcdBySidoCode(sidocode):
    return 0
def searchLawdcdByAddress(addrstring):
    retlist = list()
    obj = naverapi.geocode(addrstring)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    NORESULTCASEsidocodeList = list()
    NORESULTCASEgugunnameList= list()
    NORESULTCASE = bool()
    for i in range (0,numItem):
        item = dict()
        detailAddr = obj['result']['items'][i]['addrdetail']
        addr = obj['result']['items'][i]['address']
        if detailAddr['sido'] == '':
            item['address'] = addr
            item['lawdcd'] = ''
            retlist.append(item)
            continue
        sidocode = getSidoCode(detailAddr['sido'])
        Mygugunlist = getGuGunListBySidoCode(sidocode)
        GugunName = naverGugunNameToRtGugunName(detailAddr['sigugun'])
        lawdcd = getLawd_cdByNameInGuGunList(Mygugunlist, GugunName)
        if lawdcd =='NORESULT' :
            NORESULTCASE = True
            NORESULTCASEsidocodeList.append(sidocode)
            NORESULTCASEgugunnameList.append(GugunName)
        else:
            item['address'] = addr
            item['lawdcd'] = lawdcd
            retlist.append(item)

    if NORESULTCASE and numItem > 0:
        assert len(NORESULTCASEsidocodeList) == len (NORESULTCASEgugunnameList)
        NumNRC = len(NORESULTCASEgugunnameList)
        for i in range(0,NumNRC):
            sidocodeitem = NORESULTCASEsidocodeList[i]
            gugunNameitem= NORESULTCASEgugunnameList[i]
            InSidoAlist = addrlist(sidocodeitem)
            InSidoClist = codelist(sidocodeitem)
            InSidoElemNum= len(InSidoAlist)
            assert (len(InSidoAlist) == len (InSidoClist))
            for i in range (0,InSidoElemNum) :
                itemforNORESULTCASE = dict( )
                ManupulatedSearchingAddress = InSidoAlist[i]
                if ManupulatedSearchingAddress == '충청북도 청주서원구':
                    ManupulatedSearchingAddress = '충청북도 청주시 서원구'
                if ManupulatedSearchingAddress == '충청북도 청주청원구':
                    ManupulatedSearchingAddress = '충청북도 청주시 청원구'
                if gugunNameitem[-1] =="시" and len(gugunNameitem)>2:
                    gugunNameitem= gugunNameitem[0:-1]
                if  ( gugunNameitem not in ManupulatedSearchingAddress):
                    continue
                lawdcdList = searchLawdcdByAddress(ManupulatedSearchingAddress)
                if len(lawdcdList)>0:
                    itemforNORESULTCASE['address'] = lawdcdList[0]['address']
                    itemforNORESULTCASE['lawdcd'] = lawdcdList[0]['lawdcd']
                    retlist.append(itemforNORESULTCASE)
                else :
                    print('다음 이름을 검색하던 중 오류가 발생 하였습니다.' + ManupulatedSearchingAddress)
    return retlist


print( searchLawdcdByAddress('성남'))
