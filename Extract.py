import pyautogui as auto
import time
import keyboard
import idextract
txt = idextract.txt
ids = "S190783"
password = "puc@2019"
idpos  = (416,499)
passpos = (445,580)
logpos = (506,667)
notepad = (1032,2)
back = (33,80)




def getGrade(id,i):
    auto.moveTo(idpos)
    auto.doubleClick()
    auto.write(id)
    # time.sleep(0.5)
    auto.moveTo(passpos)
    auto.click()
    auto.write(password)
    auto.moveTo(logpos)
    # time.sleep(0.5)
    auto.click()
    time.sleep(2)
    auto.hotkey("ctrl","a")
    auto.hotkey("ctrl","c")
    auto.moveTo(notepad)
    auto.click()
    # auto.hotkey("alt","tab")
    auto.press("enter")
    auto.press("enter")
    auto.press("enter")
    data  = str(i)+"th record"
    auto.write(data)
    auto.hotkey("ctrl","v")
    auto.hotkey("ctrl","s")
    auto.moveTo(back)
    auto.click();
    # auto.sleep(0.5)
    # auto.hotkey("ctrl","r")
    # time.sleep(2)
for i in range(0,10):
    # getGrade(txt[i])
    a = txt[i][2:9]
    if(a[:4]=="S190"):
    # print(a)
        getGrade(a,i)
    if(keyboard.read_key()=="a"):
        break

# auto.hotkey("ctrl","c")


