import requests
def getHTMLTest(url):
    r = requests.get(url,timeout=20)
    
    print(r.status_code)
    print(r.encoding)
    print(r.text)

getHTMLTest('http://baidu.com')
