import naverapi
f =open('bubjungdong.txt',"r",encoding="utf-8")
strs = f.readline()

with open('parsed.txt', 'w',encoding="utf-8") as thefile:
    while strs :
        strs = f.readline()
        if strs.find("폐지") is -1:
            print( strs[11:-4],end="" ,file=thefile)
            print(":  ",end="",file=thefile)
            print(naverapi.papago(strs[11:-4])["message"]["result"]["translatedText"],file=thefile)
        else:
            pass