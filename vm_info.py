# Huge thanks to elizabeth chadbourne for help with most of the modules in this assignment,
from pyVmomi import vim
import vm_connect

def vmDetails(VMList):
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names:")
    vm_connect.si.RetrieveContent()
    datacenter = vm_connect.si.content.rootFolder.childEntity[0]
    VMList = datacenter.vmFolder.childEntity
    for vm in VMList:
        print([vm.name])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    searchvm = str(input("Enter VM Name (Leave blank if none):"))

    if(searchvm):
        for vm in VMList:
            if(vm.name == searchvm):
                memory = int(vm.config.hardware.memoryMB) / 1024
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Name: " + vm.name)
                print(f"IP Address: {vm.guest.ipAddress}")
                print("Power: " + vm.runtime.powerState)
                print(f"CPU: {vm.config.hardware.numCPU}")
                print(f"Memory(GB): {memory}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("Please choose a valid VM.") 
                continue         

def vmList(VMList):
    vm_connect.si.RetrieveContent()
    datacenter = vm_connect.si.content.rootFolder.childEntity[0]
    VMList = datacenter.vmFolder.childEntity
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print("VM Names:")
    for vm in VMList:
        print(vm.name)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
