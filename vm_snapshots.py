import vm_connect
from pyVmomi import vim

def snapshot():
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
                name = input("Enter snapshot name: ")
                desc = input("Enter snapshot description: ")
                vm.CreateSnapshot_Task(name = name,
                                       description = desc,
                                       memory = False,
                                       quiesce = False)

def restore():
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
                vm.RevertToCurrentSnapshot()
