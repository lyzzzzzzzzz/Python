from dns import resolver
import os
import httplib2
 
iplist =[ ]
appdomain = "www.baidu.com"

def get_iplist(domain=""):
    try:
        A = resolver.query(domain,'A')
    except Exception as e:
        print('dns resolver error:'+str(e))
        return
    for i in A:
        iplist.append(i)
    return True

def checkip(ip):
    checkurl = str(ip) +':80'
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)
    conn = httplib2.HTTPConnectionWithTimeout(checkurl)

    try:
        conn.request('GET','/',headers={'Host':appdomain})
        r=conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent == b'<!DOCTYPE html>':
            print(str(ip)+'[OK]')
        else:
            print(str(ip)+'[Error]')
    
if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print('dns resolver error')
