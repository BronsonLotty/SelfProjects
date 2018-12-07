
import urllib.parse
import http.client
import random
import hashlib

appKey = '7fd027c605dc9d20'
secretKey = 'lYfH6hq6mXMLV1PNXNASvpJFsAIpFhrq'


def youdaoTranslate(q):
    q = "你好"
    httpClient = None
    myurl = '/api'
    salt = random.randint(1, 65536)
    sign = appKey + q + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    fromLang = 'AUTO'
    toLang = 'AUTO'
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        #http: // fanyi.youdao.com / translate_o?smartresult = dict & smartresult = rule
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        s = eval(response.read().decode("utf-8"))['translation']
    except Exception as e:
        s = "erro"
    finally:
        if httpClient:
            httpClient.close()
    return s


if __name__ == '__main__':




    myinput = input()
    content = youdaoTranslate(myinput)
    print(content)
'''
i=%E4%BD%A0%E5%A5%BD&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1541994003166&sign=e2d8eeab8f7b953e76a9f429a26b91a0&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
'''