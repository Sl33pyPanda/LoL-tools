import subprocess, requests


def getUserAgent():
    return {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/11.15.388.2387 (CEF 74) Safari/537.36'}


def setIcon(port, token, id):
    special_id = [29,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78]
    res = requests.put("https://127.0.0.1:{}/lol-summoner/v1/current-summoner/icon".format(port),
                        auth=requests.auth.HTTPBasicAuth('riot', token),
                        data = { "profileIconId" : id},
                        headers = getUserAgent(),
                        proxies = {'https': 'https://127.0.0.1:8080',
                                   'http': 'http://127.0.0.1:8080'   
                                   },
                        verify=False
                        )
    return res.content



def getApp():
    command = "WMIC PROCESS WHERE name='LeagueClient.exe' GET commandline" #get lol cmd
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read().decode()
    if "No Instance(s)" in output:
        raise IOError("Run lol client first plsss")    
    else:
        ret = {}
        arr = output.split(" --")
        for i in arr[1:]:
            if "=" in i:
                tmp = i.split("=")
                ret[tmp[0]] = tmp[1].split(" ")[0]
            else:
                ret[i] = ""
        return ret 
    return -1


def getInfo(): # just set alias for some names :3
    info = getApp()
    print(info)
    return {"port"  : info["riotclient-app-port"],
            "token" : info["landing-token"],
            "region": info["locale"],
            "client": info["parent-client"],
            "auth"  : info["riotclient-auth-token"]}
            

def main():
    info = getInfo()
    special_id = [29,range(50,78)]
    print(setIcon(info["port"],info["auth"],29))


if __name__ == '__main__':
    main()