import vm_connect
from pyVmomi import vim

def powerOn():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names:")
    vm_connect.si.RetrieveContent()
    datacenter = vm_connect.si.content.rootFolder.childEntity[0]
    VMList = datacenter.vmFolder.childEntity
    for vm in VMList:
        print([vm.name])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    searchVM = str(input("Enter VM Name to Power On (Leave blank if none):"))
    if(searchVM):
        for vm in VMList:
            if(vm.name == searchVM):
                vm.PowerOn()

def powerOff():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names:")
    vm_connect.si.RetrieveContent()
    datacenter = vm_connect.si.content.rootFolder.childEntity[0]
    VMList = datacenter.vmFolder.childEntity
    for vm in VMList:
        print([vm.name])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    searchVM = str(input("Enter VM Name to Power On (Leave blank if none):"))
    if(searchVM):
        for vm in VMList:
            if(vm.name == searchVM):
                vm.PowerOff()

def reboot():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names:")
    vm_connect.si.RetrieveContent()
    datacenter = vm_connect.si.content.rootFolder.childEntity[0]
    VMList = datacenter.vmFolder.childEntity
    for vm in VMList:
        print([vm.name])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    searchVM = str(input("Enter VM Name to Reboot. (Leave blank if none):"))
    if(searchVM):
        for vm in VMList:
            if(vm.name == searchVM):
                vm.Reset()
            