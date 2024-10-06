# Huge thanks to elizabeth chadbourne for help with most of the modules in this assignment,
from pyVmomi import vim
import vm_connect

info = vm_connect.content

def GetInfo(info,InfoType):
    obj = {}
    Container = info.viewManager.CreateContainerView(info.rootFolder, InfoType, True)
    for MInfo in Container.view:
        obj.update({MInfo:MInfo.name})
        return obj
    
    GetVMs = GetInfo(info,[vim.VirtualMachine])

    def vmDetails(VMList):
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("VM Names:")
        for vm in VMList:
            print(vm.name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        searchvm = str(input("Enter VM Name (Leave blank if none):"))

        if(searchvm):
            for vm in VMList:
                if(vm.name == searchvm):
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Name: " + vm.name)
                    print("IP Address: " + vm.guest.ipAddress)
