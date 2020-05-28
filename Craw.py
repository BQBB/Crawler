import requests
import urllib.parse
import argparse
import re
paths=[]
saved=open('url.txt','a')
def parse():
    arg=argparse.ArgumentParser()
    arg.add_argument('-t','--target',dest='target',help='-t || --target For pass Target URL')
    return arg.parse_args().target

def get(url):
    try:
        req=requests.session().get(url)
        path_now=re.findall('href="(.*?)"',str(req.content))
        for url_now in path_now:
                     url_now=urllib.parse.urljoin(urlg,url_now)
                     if urlg in url_now and not url_now in paths and not '#' in url_now:
                        paths.append(url_now)
                        print(url_now)
                        saved.write(url_now+'\n')
                        get(url_now)
                     else:
                        pass

        return 1
    except:
        pass
urlg=parse()
if urlg:
    urlg=urlg.strip()
    get(urlg)
else:
    urlg=input('Target : ').strip()
    get(urlg)
