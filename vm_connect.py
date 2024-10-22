import json
import getpass
from pyVim.connect import SmartConnect
import ssl

with open('vcenter.conf.json') as i:
    vcenter_conf = json.load(i)

# Speicify the json content as an array, then variables

vcenter_info = vcenter_conf['vcenter.lily.local'][0]
vcenterhost = vcenter_info['vcenterhost']
vcenteradmin = vcenter_info['vcenteradmin']

password = getpass.getpass()

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE

si=SmartConnect(host=vcenterhost, user=vcenteradmin, pwd=password, sslContext=s)
content = si.content

def vcenterConnect():
    aboutContent = si.content.about
    print(aboutContent)
    print(aboutContent.fullName)
