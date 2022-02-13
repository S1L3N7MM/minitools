#!/usr/bin/env python

import subprocess as s1l3n7sp
import optparse
import re as s1l3n7regx


def get_arguments():
    s1l3n7Parser = optparse.OptionParser()
    s1l3n7Parser.add_option("-i", "--interface", dest="interface", help="Interface To change its MAC address")
    s1l3n7Parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (opts, arguments) = s1l3n7Parser.parse_args()
    if not opts.interface:
        s1l3n7Parser.error('[-] Please Specify an interface, use --help for more info.')
    elif not opts.new_mac:
        s1l3n7Parser.error('[-] Please Specify a new mac, use --help for more info.')
    return opts


def change_mac(interface, new_mac):
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)
    s1l3n7sp.call(['ifconfig', interface, 'down'])
    s1l3n7sp.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    s1l3n7sp.call(['ifconfig', interface, 'up'])


def get_current_mac(interface):
    ifconfig_result = s1l3n7sp.check_output(['ifconfig', interface])
    mac_address_search_result = s1l3n7regx.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address')


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to" + current_mac)
else:
    print('[-] MAC address did not get changed!')
