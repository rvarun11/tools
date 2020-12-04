import scapy.all as scapy
import optparse

# Algorithm:
# 1. Create ARP Request directed to broadcast MAC asking for IP.
# 2. Send Packet & Receive the response
# 3. Parse the response and display the result.


def netscan(ip):
    #1.
    # Use scapy.ls(scapy.methodName()) to get the fields and their desc
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast/arp_req
    
    #2.
    #ans stores all the response we are getting, If the idx was 1, we will be getting the unanswered responses.
    # Setting verbose to false will make the output less clutered.
    ans=scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    
    #3.
    #Each element in the ans stores the Sent Request at idx 0, and Response at idx 1. 
    # psrc stores IP address from where the reply is coming, hwsrc stores the reply
    client_list = []
    for i in ans:
        client = {"ip":i[1].psrc,"mac":i[i].hwsrc}
        client_list.append(client)
    
    return client_list
    
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="Enter Target IP Address/Range")
    (options,arguements) = parser.parse_args()
    return options

#Driver Code
options = get_args()
print(netscan(options.target))
