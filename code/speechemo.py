from speech.speech import findemo

def speechemo(aud):
    a=(findemo("{}".format(aud))[0]).split("_")[1]
    if a=="angry":
        return 2
    if a=="happy":
        return 5
    if a=="sad":
        return 3
    if a=="fearful":
        return 1
    if a=="calm":
        return 4

if __name__=="__main__":
    print(speechemo("speech/tempaud.wav"))