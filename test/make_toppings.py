import requests
def getHTMLTest(url):
    r = requests.get(url,timeout=20)

    print(r.status_code)
    print(r.encoding)
    print(r.text)
    print(r.raw.read())
getHTMLTest('https://api.github.com/events')
