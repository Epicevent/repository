import json
import Lawdcdtest

import json
from pprint import pprint

with open('AllLawdcd.txt') as data_file:
    data = json.load(data_file)

pprint(data) #data는 json 전체를 dictionary 형태로 저장하고 있음

#  Expected results
#
#[ {'CENTER_X': 127.075207502763,
#   'CENTER_Y': 37.4828815893558,
#   'CODE': '11680',
#   'NAME': '강남구'},
#  {'CENTER_X': 127.17632850343,
#   'CENTER_Y': 37.5797387635829,
#   'CODE': '11740',
#   'NAME': '강동구'},
#  {'CENTER_X': 127.035831948963,
#   'CENTER_Y': 37.6178106471746,
#   'CODE': '11305',
#   'NAME': '강북구'}, ...

#make string list(for XYcoord)

stringlist=list()
for GuGunItem in data:
    stringlist.append(str(GuGunItem['CENTER_X'])+", "+str(GuGunItem['CENTER_Y']))

pprint(stringlist)

#save test result

TestResult=list()
for TestInput in stringlist:
    TestResult.append(Lawdcdtest.getLawdcdListByXY(TestInput))

print(TestResult)

ExpectedResult = list()
for GuGunItem in data:
    ExpectedItem = list()
    ExpectedItem.append(GuGunItem['CODE'])
    ExpectedResult.append(ExpectedItem)

print(ExpectedResult)

#Compare Expected Result And Test Result

if len(ExpectedResult) == len(TestResult):
    indexMax = len(ExpectedResult)
else:
    print('TEST 실패')

ErrorIndexList =list()
for i in range (0 , indexMax):
    if len(ExpectedResult[i]) == len(TestResult[i]) :
        jMax = len(ExpectedResult[i])
        for j in range (0,jMax):
            if ExpectedResult[i][j]!=TestResult[i][j]:
                ErrorIndexList.append(i)
    else:
        ErrorIndexList.append(i)

for i in ErrorIndexList:
    print('오류' + str(i) +'\n')
    pprint (data[i])
    pprint (TestResult[i])