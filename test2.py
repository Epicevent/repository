import naverapi
import Lawdcd

import json
from pprint import pprint


naverCoordiNalist=list()
for i in range(7, 17):
    naverCoordiNalist.append(naverapi.NaverCoordiNa(i,"126.9573739,37.5048980"))

# test result

TestResult=list()
with open('Test2result.txt', 'w') as thefile:
    for TestInput in naverCoordiNalist:
        item =TestInput.get_magic_int_xy()+(TestInput.level,)
        TestResult.append(item)
        print(item,file=thefile)