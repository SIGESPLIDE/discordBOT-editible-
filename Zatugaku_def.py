import Zatugaku
import random
def FOKdoubutu():
    global data
    fo   = len(Zatugaku.Zatugaku.Zlist)
    data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]

    while True:
        #print(data[3]) #---デバッグ用---#
        if data[3] == Zatugaku.Zatugaku.Zlist[0][3]:
            break
        data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]
    return data

def FOKseikatu():
    global data
    fo   = len(Zatugaku.Zatugaku.Zlist)
    data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]

    while True:
        #print(data[3]) #---デバッグ用---#
        if data[3] == Zatugaku.Zatugaku.Zlist[15][3]:
            break
        data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]
    return data

def FOKlist():
    global unique_datalist
    fo       = len(Zatugaku.Zatugaku.Zlist)
    data     = Zatugaku.Zatugaku.Zlist[0:fo-1]
    data     = data[0:fo-1]
    datalist = ["None"]

    for i in range(len(Zatugaku.Zatugaku.Zlist)-1):
        datalist.append(data[i][3])
    unique_data = set(datalist)
    unique_datalist = list(unique_data)
    unique_datalist.remove("None")
    unique_datalist.sort()
    #print(unique_datalist) #---デバッグ用---#
    return unique_datalist



