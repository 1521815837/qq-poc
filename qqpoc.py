import requests
import re

def getinform():
    gettoken = requests.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=715030901&daid=73&hide_close_icon=1&pt_no_auth=1&s_url=https%3A%2F%2Fqun.qq.com%2Fmember.html')
    token = gettoken.headers['Set-Cookie']
    tokenre = r'pt_local_token=(.*?);'
    tokenre = re.compile(tokenre)
    tokenlist = re.findall(tokenre,token)
    token = ''.join(tokenlist)
    headers = {'Referer':'https://xui.ptlogin2.qq.com','Cookie': 'pt_local_token='+token}
    getuin = requests.get('https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&r=0.0760575656488639&pt_local_tk='+token,headers=headers)
    getuin = getuin.text
    uinre = r'"uin":"(.*?)"'
    uinre = re.compile(uinre)
    uinlist = re.findall(uinre,getuin)
    uin = ''.join(uinlist)
    clientkey = requests.get('https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin=%s&callback=ptui_getst_CB&r=0.4266647630782271&pt_local_tk=%s'%(uin,token),headers=headers)
    clientkey = clientkey.headers['Set-Cookie']
    clientkeylist = clientkey.split(';')
    i = 0
    for n in clientkeylist:
        if 'clientkey=' in n:
            break
        i = i+1
    clientkey = clientkeylist[i]
    clientkey = clientkey.replace('domain=.ptlogin2.qq.com, clientkey=','')
    return(token,uin,clientkey)

token,uin,clientkey = getinform()

def qqqun():
    headers = {'Referer':'https://xui.ptlogin2.qq.com','Cookie':'pt_local_token='+token+';'+'clientkey='+clientkey+';'}
    url = 'https://ssl.ptlogin2.qq.com/jump?clientuin='+uin+'&keyindex=9&pt_aid=715030901&daid=73&u1=https%3A%2F%2Fqun.qq.com%2Fmember.html%23&pt_local_tk='+token+'&pt_3rd_aid=0&ptopt=1&style=40'
    jumpurl = requests.get(url,headers=headers)
    jumpurl = jumpurl.text
    jumpurl = jumpurl.replace('\'','')
    jumpurl = jumpurl.replace('ptui_qlogin_CB(0, ','')
    jumpurl = jumpurl.replace(', )','')
    return jumpurl

def qqmail():
    headers = {'Referer':'https://xui.ptlogin2.qq.com','Cookie':'pt_local_token='+token+';'+'clientkey='+clientkey+';'}
    url = 'https://ssl.ptlogin2.qq.com/jump?clientuin='+uin+'&keyindex=9&pt_aid=522005705&daid=4&u1=https%3A%2F%2Fmail.qq.com%2Fcgi-bin%2Freadtemplate%3Fcheck%3Dfalse%26t%3Dloginpage_new_jump%26vt%3Dpassport%26vm%3Dwpt%26ft%3Dloginpage%26target%3D&pt_local_tk='+token+'&pt_3rd_aid=0&ptopt=1&style=25'
    jumpurl = requests.get(url,headers=headers)
    jumpurl = jumpurl.text
    jumpurl = jumpurl.replace('\'','')
    jumpurl = jumpurl.replace('ptui_qlogin_CB(0, ','')
    jumpurl = jumpurl.replace(', )','')
    return jumpurl
	
def qz():
    headers = {'Referer':'https://xui.ptlogin2.qq.com','Cookie':'pt_local_token='+token+';'+'clientkey='+clientkey+';'}
    url = 'https://ssl.ptlogin2.qq.com/jump?clientuin='+uin+'&keyindex=9&pt_aid=549000912&daid=5&u1=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_local_tk='+token+'&pt_3rd_aid=0&ptopt=1&style=40&has_onekey=1'
    jumpurl = requests.get(url,headers=headers)
    jumpurl = jumpurl.text
    jumpurl = jumpurl.replace('\'','')
    jumpurl = jumpurl.replace('ptui_qlogin_CB(0, ','')
    jumpurl = jumpurl.replace(', )','')
    return jumpurl

print(qqqun())
print(qqmail())
print(qz())