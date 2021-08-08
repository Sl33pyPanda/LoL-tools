 
import requests, os, re, subprocess, random, time, datetime

 
s = requests.session()
token = 0


def getToken():
    command = "WMIC PROCESS WHERE name='LeagueClient.exe' GET commandline" #get lol cmd
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read().decode()
    if "token" in output:
        ret = re.findall('--landing-token=([a-z0-9]+)', output)
        return ret[0]        
    else:
        raise IOError("Run as Assmin or LOL client is not running ....")
        

def codeEnter(code):
    for i in range(2):
        res = s.post('https://bargain.lol.garena.vn/api/enter',
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/11.15.388.2387 (CEF 74) Safari/537.36',
                'Token': token,
                'Referer': 'https://bargain.lol.garena.vn/?token=' + token
            },
            json = {"code": code.strip(),"confirm": True if i == 1 else False},
            # proxies = {'https': 'http://localhost:8888'},
            # verify = False
        )

    return res.json()


if __name__ == '__main__':
    try:
        #token = getToken()
        token = "ea0445338023d1c320590226751b208fd8490ef843a4f2ae9fec3d6a24d5a8af"
        print("Token : ", token)

        #https://github.com/Sl33pyPanda/MiPublic/blob/master/lol-botsinhnhat/code/code
        codes = re.findall("LOL[A-Z0-9]{10}", requests.get("https://github.com/Sl33pyPanda/LoL-tools/blob/main/bot-sinhnhat/code/code").text) 
        print("codebase : ",len(codes))
        codes = random.sample(codes,k=1000)
        for code in codes:            
            res = codeEnter(code)
            print(datetime.datetime.now().time(),end= "   ")
            print("Sent : ", (code),end = "")
            if "reward" in res :
                print(" - Successed")
                if res["enter_code_amount"] == 50:
                    print('Done.. exiting')
                    break
            else:
                print(" - Failed")
            if "error" in res:
                if "BAD_REQUEST" in res["error"]:
                    break
            

    except Exception as e:
        print("Error  : ",end="")
        print(e)
