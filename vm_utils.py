# Help from Willow O'Hara :3
# More help form Beth Chadbourne
# https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/getallvms.py

import getpass
import json
import socket 


# Getting hostname/IP address
def ipaddress():
    hostname = socket.gethostname()


def menu():
    print("[1] VCenter Info")
    print("[2] Session Details")
    print("[3] VM Details")
    print("[4] Exit the Program")

menu()
option = int(input("Enter your option:"))

while option != 4:
    if option == 1:
        
        pass
    elif option == 2:
        file = open('vcenter.conf.json')
        data = json.load(file)
        print(data['vcenter'][0]['vcenterhost'])
        print(data['vcenter'][0]['vcenteradmin'])
        pass
    elif option == 3:
        print("List of Selectable VMs:")

        pass
    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Enter your option:"))
file.close()
print("Thank you for using this program, goodbye.")
