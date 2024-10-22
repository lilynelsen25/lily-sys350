import socket
import getpass
import vm_connect

vcontent = vm_connect.content

def vmsession():
    hostname = socket.gethostname()

    # Getting IP address.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ipaddress = s.getsockname()[0]

    #print hostname & ip address.

    print("Hostname: " + hostname)
    print("IP Address: " + ipaddress)

    currentUser = getpass.getuser()
    #Print current logged in user, vcenter server, and domain

    print("Current Logged in User: " + currentUser)
    print("vCenter Server:" + vm_connect.vcenterhost)

    session = vcontent.sessionManager.currentSession
    domainUser = session.userName
    print("Domain User: " + domainUser)
