from requests_html import HTMLSession
import websockets
import asyncio
import re
import json
import _thread, time

import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

session = HTMLSession()
r = session.get('https://lmssplus.com/chat')

#user = "dafoniw197@activesniper.com"
#passwd = "Passw0rd"

token = "07e29c41e8b27f782167e5ed5d2203cfa4c67b242ca992e9654792691d"

info = json.loads(session.post("https://lmssplus.com/api/v2/user/user/refresh-token", data = {"refresh_token":token}).text)
print("Success" if info["refresh_token"] == token else "Failed")

tmpid = session.get("https://lmssplus.com/api/chat/?EIO=3&transport=polling").text
id =  json.loads(tmpid[tmpid.find('{'):tmpid.find('}')+1])["sid"]
print(id)

# The main function that will handle connection and communication 
# with the serverc
#LOLH5WV4BREVU

c = []
import pyautogui
print("move the mouse to the ok button")
time.sleep(10)
x,y = pyautogui.position() 
print(x,y)

def code_enter(code):  
    '''  
    pyautogui.typewrite(code+'\n', interval=0.0001)
    time.sleep(0.3)
    pyautogui.click(x=x, y=y, clicks=3, interval=0.5, button='left')
    time.sleep(0.3)
    print('entered : ' + code)
    pyautogui.typewrite(['tab']*7, interval=0.05)
    '''

async def listen():
    url = "wss://lmssplus.com/api/chat/?EIO=3&transport=websocket&sid=" + id
    async with websockets.connect(url) as ws:
        await ws.send("2probe")
        msg = await ws.recv()
        print("Connected" if msg == "3probe" else "Cannot connect") 
        await ws.send("5")
        print("starting to find codes ...... ")
        while True:
            await ws.send("3")
            msg = await ws.recv()
            #print(msg)
            codes = re.findall("LOL[A-Z0-9]{10}", msg) 
            if codes:
                #print(codes)
                for code in codes :                    
                    #code_enter(code)
                    print(code)

# Start the connection

while True :
    try:
        asyncio.get_event_loop().run_until_complete(listen())
    except Exception as e:
        print(e)
        info = json.loads(session.post("https://lmssplus.com/api/v2/user/user/refresh-token", data = {"refresh_token":token}).text)
        print("Success" if info["refresh_token"] == token else "Failed")
        tmpid = session.get("https://lmssplus.com/api/chat/?EIO=3&transport=polling").text
        id =  json.loads(tmpid[tmpid.find('{'):tmpid.find('}')+1])["sid"]
        print(id)
        print("Reconnecting")




def retriever():
    global codes
    while 1:
        if codes:
            for code in codes:
                code_enter(code)

#t1 = _thread.start_new_thread(retriever(), ()) 