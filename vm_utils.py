# Help from Willow O'Hara :3
# More (a lot more) help form Beth Chadbourne
# https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/getallvms.py

import vm_connect
import vm_session
import vm_info
import vm_power
import vm_snapshots
import vm_config

def menu():
    print("[1] VCenter Info")
    print("[2] Session Details")
    print("[3] VM Details")
    print("[4] VM Power On")
    print("[5] VM Power Off")
    print("[6] VM Reboot")
    print("[7] Take Snapshot")
    print("[8] Revert Snapshot")
    print("[9] Change CPU Count")
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
    elif option == 4:
        print("List of Selectable VMs:")
        vm_power.powerOn()
        print("Done.")
    elif option == 5:
        print("List of Selectable VMs:")
        vm_power.powerOff()
        print("Done.")
    elif option == 6:
        print("List of Selectable VMs:")
        vm_power.reboot()
        print("Done.")
    elif option == 7:
        print("List of VMs to Snapshot:")
        vm_snapshots.snapshot()
        print("Done.")
    elif option == 8:
        print("List of VMs to Revert:")
        vm_snapshots.restore()
        print("Done.")
    elif option == 9:
        print("List of VMs to Alter:")
        vm_config.CPUChange()
        print("Done.")
    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Enter your option:"))

print("Thank you for using this program, goodbye.")
