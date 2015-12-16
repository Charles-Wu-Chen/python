__author__ = 'charlesw'


import os
import Cookie
import browsercookie
import re
import urllib2
import requests,cookielib
import json
import pickle
from zhihu import Question

url = "https://www.zhihu.com/question/24269892"
question = Question(url)
answers = question.get_all_answers()
for answer in answers:
    answer.to_txt()
    answer.to_md()

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'w+b') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

get_title = lambda html: re.findall('<title>(.*?)</title>', html, flags=re.DOTALL)[0].strip()


def save_cookies_lwp(cookiejar, filename):
    lwp_cookiejar = cookielib.LWPCookieJar()
    for c in cookiejar:
        args = dict(vars(c).items())
        args['rest'] = args['_rest']
        del args['_rest']
        c = cookielib.Cookie(**args)
        lwp_cookiejar.set_cookie(c)
    lwp_cookiejar.save('obj/' + filename, ignore_discard=True)

def load_cookies_from_lwp(filename):
    lwp_cookiejar = cookielib.LWPCookieJar()
    lwp_cookiejar.load('obj/' + filename, ignore_discard=True)
    return lwp_cookiejar

cj = browsercookie.firefox()
#CookieJar
print cj
save_cookies_lwp(cj,"lwpcookie")
url = 'https://www.zhihu.com/settings/profile'

#requests = requests.Session()
requests.cookies = cookielib.LWPCookieJar('lwpcookie')

#r = requests.get(url, cookies=cj)
#print type(r)
#requests.cookies.save()
#print get_title(r.content)


save_obj(requests.utils.dict_from_cookiejar(cj), "firefox" )

ff = load_obj("firefox")

#r2 = requests.get(url, cookies=ff)
#print get_title(r2.content)


#cj1 = load_cookies_from_lwp("lwpcookie")

#r3 = requests.get(url, cookies=cj1)
#print get_title(r3.content)
#print int(r3.status_code)

#requests = requests.Session()
requests.cookies = cookielib.LWPCookieJar('lwpcookie')
try:
    requests.cookies.load(ignore_discard=True)
except:
    print "error"

rcj = requests.cookies
print (rcj)

url = "https://www.zhihu.com/settings/profile"
r = requests.get(url, cookies=rcj, allow_redirects=False)
status_code = int(r.status_code)
print status_code
print r.content
print get_title(r.content)