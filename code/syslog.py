import datetime
import configparser
import os


def checkfile(nm):
    if not os.path.exists(nm):
        f=open(nm,"w+")
        f.close()

def getusr():
    cf=configparser.ConfigParser()
    cf.read("config.ini")
    user=cf['Details']["User"]
    return user


def addtime(text):
    text = text + "," + str(datetime.datetime.now().time()).split('.')[0]
    return text

def adddeplog(text):
    user=getusr()
    id = str(datetime.date.today()).replace("-","")
    with open("./{}/{}_depression.csv".format(user,id),"a+") as f:
        text = addtime(text)
        f.write(text+"\n")
    f.close()

def adddreslog(sc):
    #getfileno()
    user=getusr()
    id = str(datetime.date.today()).replace("-","")
    with open("./{}/{}_depscore.csv".format(user,id),"a+") as f:
        text = addtime(sc)
        f.write(text+"\n")

def addchatlog(txt):
    user=getusr()
    id = str(datetime.date.today()).replace("-", "")
    with open("./{}/{}_chat.csv".format(user,id), "a+") as f:
        text = addtime(txt)
        f.write(text + "\n")
    f.close()

def addtraits(txt):
    user=getusr()
    id = str(datetime.date.today()).replace("-", "")
    with open("./{}/traits.csv".format(user), "a+") as f:
        text = id+","+txt
        f.write(text + "\n")
    f.close()

def getchatlength():
    user=getusr()
    id = str(datetime.date.today()).replace("-", "")
    checkfile("./{}/{}_chat.csv".format(user, id))
    with open("./{}/{}_chat.csv".format(user, id), "r") as f:
        numline = len(f.readlines())
    f.close()
    if numline<10:
        return 0
    if(numline<=25):
        return 1
    elif (numline <= 55):
        return 2
    else:
        return 3

def getreslog():
    user=getusr()
    id = str(datetime.date.today()).replace("-", "")
    checkfile("./{}/{}_depscore.csv".format(user, id))
    with open("./{}/{}_depscore.csv".format(user, id), "r") as f:
        l=f.readlines()
    f.close()
    l.reverse()
    l=l[:7]
    try:
        l = sum(l)//len(l)
    except:
        l=0
    return (l//10 + 1)

def getdislikes():
    user = getusr()
    id = str(datetime.date.today()).replace("-", "")
    checkfile("./{}/traits.csv".format(user))
    with open("./{}/traits.csv".format(user), "a+") as f:
        if(len(f.readlines())>8):
            line=[(i.split(",")[1]) for i in (((f.readlines()).reverse())[:8])]
            traits=[]
            for i in line:
                for k in i.split("-"):
                    traits.append(k)
            count1 = [(i,traits.count(i)) for i in set(traits)]
        else:
            count1=0
    f.close()
    return count1