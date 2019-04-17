import win32com.client as wincl
text1 = wincl.Dispatch("SAPI.SpVoice")


def speak(inp):
    text1.Speak(inp)

