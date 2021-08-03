import pyautogui, time, random, re, keyboard, requests
from PIL import ImageFile
xok,yok,xnhap,ynhap=0,0,0,0
ok,btn1,btn2,nhapbtn=0,0,0,0

def load(url):
    p = ImageFile.Parser()
    p.feed(requests.get(url).content)
    return p.close()

def find():
    global ok,btn1,btn2
    while 1:
        if keyboard.is_pressed('esc'):
            break
        if pyautogui.locateOnScreen(ok, region=(0,0,4500,2500), grayscale=True, confidence=0.9) != None:
            pyautogui.click(x=xnhap, y=ynhap, clicks=2, interval=0.05, button='left')
            return 1
        else:
            btn1box = pyautogui.locateOnScreen(btn1, region=(0,0,4500,2500), grayscale=True, confidence=0.7)
            if btn1box != None:
                pyautogui.click(x=btn1box[0]+btn1box[2]/2, y=btn1box[1]+btn1box[3]/2, clicks=1, interval=0.1, button='left')
            btn2box = pyautogui.locateOnScreen(btn2, region=(0,0,4500,2500), grayscale=True, confidence=0.7)
            if btn2box != None:
                pyautogui.click(x=btn2box[0]+btn2box[2]/2, y=btn2box[1]+btn2box[3]/2, clicks=1, interval=0.1, button='left')
            time.sleep(0.1)
        

def code_enter(code):  
    pyautogui.typewrite(code+'\n', interval=0.0001)
    time.sleep(0.1)
    pyautogui.click(x=xok, y=yok, clicks=3, interval=0.1, button='left')
    print('entered : ' + code)
    time.sleep(0.1)
    
    

def main():
    global xok,yok,xnhap,ynhap,ok
    global ok,btn1,btn2
    #trying some fun stuff
    pwd = input("Nhap password : ")


    r = re.findall("http://[a-z0-9]{12}.ngrok.io",requests.get('https://github.com/Sl33pyPanda/MiPublic/blob/master/public.info').text)[0] # server info
    
    if pwd == requests.get(r).text:
        requests.get(r+"?true="+pwd)
        text = requests.get(r+"/code?true="+pwd).text
        code = re.findall("LOL[A-Z0-9]{10}", text) 
        codes = list(set(code))
        print(len(codes))
        ok = load(r+'/ook.png')
        nhapbtn = load(r+'/nhap.png')
        print("Swicth to the game tab then press Esc to start and hold Esc to stop ")
        keyboard.wait('esc')    
        while 1:
            try:                
                box = pyautogui.locateOnScreen(ok,region=(0,0,4500,2500), grayscale=True, confidence=0.55)
                xok,yok = box[0]+box[2],box[1]+box[3]
                box =pyautogui.locateOnScreen(nhapbtn,region=(0,0,4500,2500), grayscale=True, confidence=0.55)
                xnhap,ynhap = box[0],box[1]+box[3]
                break
            except Exception as e :
                ok = load(r+'/ook.png')
                nhapbtn = load(r+'/nhap.png')
                print(e)
                time.sleep(3)
        btn1 = load(r+'/btn1.png')
        btn2 = load(r+'/btn2.png')
        print(xok,yok,xnhap,ynhap)
        time.sleep(0.5)            

        runcodes = random.sample(codes,k=1000)
        fromN = -1
        for i in runcodes:
            if keyboard.is_pressed('esc'):
                print("STOPED")
                break
            fromN+=1
            print("No. ", fromN,end= ' ')
            find()
            code_enter(i)          
    else:
        print("Wrong pass. Exiting ...")     
        time.sleep(3)


if __name__ == '__main__':
    main()