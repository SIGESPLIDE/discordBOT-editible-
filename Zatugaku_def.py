import Zatugaku
import random
def FOKdoubutu():
    global data
    fo = len(Zatugaku.Zatugaku.Zlist)
    data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]

    while True:
        #print(data[3]) #---デバッグ用---#
        if data[3] == Zatugaku.Zatugaku.Zlist[0][3]:
            break
        data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]
    return data

def FOKseikatu():
    global data
    fo = len(Zatugaku.Zatugaku.Zlist)
    data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]

    while True:
        #print(data[3]) #---デバッグ用---#
        if data[3] == Zatugaku.Zatugaku.Zlist[15][3]:
            break
        data = Zatugaku.Zatugaku.Zlist[random.randint(0,fo-1)]
    return data



