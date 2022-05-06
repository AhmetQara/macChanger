from __future__ import print_function
import subprocess
import optparse
import re

def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--inter",dest="interface",help="inter to change!!!")
    parse_object.add_option("-m","--macChange",dest="mac_address",help="new mac add")
    return parse_object.parse_args()


#print(user_inputs.inter)
#print(user_inputs.mac_add)

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        None

print("MacChanger Started!!!")

(user_input,args) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.mac_address:
    print("Success!")
    print("New mac address: ", end='')
    print(final_mac)
else:
    print("Error")

