import paralleldots
import ast
import operator

key = "" #key
paralleldots.set_api_key(key)
def textemo(txt):
    a=str((paralleldots.emotion(txt)).get('emotion'))
    a=ast.literal_eval(a)
    a=a["probabilities"]
    a=max(a.items(), key=operator.itemgetter(1))[0]
    #print(a)
    #a=(((a.split(":")[1]).split(",")[0]).strip()).split("'")[1]
    #print(a["probabilities"])
    if a=="Angry":
        return 2
    if a=="Happy":
        return 5
    if a=="Excited":
        return 5
    if a=="Sad":
        return 3
    if a=="Fear":
        return 1
    if a=="Bored":
        return 4

if __name__=="__main__":
    text = "fine how are you"
    print(textemo(text))