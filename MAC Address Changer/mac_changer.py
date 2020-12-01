import subprocess
import optparse
import re

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])


def get_current_mac(interface):
    #Reading the complete o/p from the ifconfig command of the reqd interface
    out = subprocess.check_output(["ifconfig",interface])
    #Writing the rule to search the MAC address of the said interface from the o/p
    search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(out))
    
    if search_res:
        return search_res.group(0)
    else:
        print("[-] Not successful")
    
# Helper function to get arguements from CLI
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interace",dest="interface",help="Enter the Interface whose MAC Address you want to change")
    parser.add_option("-m","--mac",dest="new_mac",help="Enter the new MAC Address")
    (options, arguements) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC Address, use --help for more info.")
    
    return options

# Driver Code
options = get_args()
current_mac = get_current_mac(options.interface)
print("The Current MAC you are trying to change is: " + str(current_mac))
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC Address changed to: " + str(current_mac))
else:
    print("[-] Unsuccessful. Please use --help for more information")

### Subprocess Call - Insecure Way, prone to Injections
# subprocess.call("ifconfig" + interface + " down", shell=True)
# subprocess.call("ifconfig" + interface + " hw ether" + new_mac, shell=True)
# subprocess.call("ifconfig" + interface + " up", shell=True)
