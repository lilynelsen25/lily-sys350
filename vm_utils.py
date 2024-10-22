# Help from Willow O'Hara :3
# More help form Beth Chadbourne
# https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/getallvms.py

import vm_connect
import vm_session
import vm_info

def menu():
    print("[1] VCenter Info")
    print("[2] Session Details")
    print("[3] VM Details")
    print("[0] Exit the Program")

menu()
option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        print()
        print("vCenter Info Selected")
        print()
        vm_connect.vcenterConnect()
        pass
    elif option == 2:
        print()
        print("Session Details Selected")
        print()
        vm_session.vmsession
        pass
    elif option == 3:
        print("List of Selectable VMs:")
        vm_info.vmDetails(vm_info.vmList)
        pass
    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Enter your option:"))

print("Thank you for using this program, goodbye.")
